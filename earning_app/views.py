from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, Portfolio
import requests
# --- WhatsApp Config ---
WAAPI_TOKEN = "kombTGr9xbn4o8q7BgnHBXcFKL536htSSKCWoEk5bcd89558"
INSTANCE_ID = 104456
MY_NUMBER = "923325710034@c.us"  # Aapka number
def index(request):
    return render(request, 'index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/product-cart/')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')
def get_started(request):
    return redirect('/product-cart/')
@login_required(login_url='/login/')
def product_cart(request):
    products = Product.objects.all()
    return render(request, 'product_cart.html', {'products': products})

@login_required(login_url='/login/')
def dashboard(request):
    my_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'orders': my_orders})

# --- Main Order Function with WhatsApp ---
@login_required(login_url='/login/')
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.create(user=request.user, product=product)

    # WhatsApp Notification via WaAPI
    try:
        url = f"https://waapi.app/api/v1/instances/{INSTANCE_ID}/client/action/send-message"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {WAAPI_TOKEN}"
        }
        payload = {
            "chatId": MY_NUMBER, # @c.us already added hai upar
            "message": f"🔥 NEW ORDER\n\nProduct: {product.name}\nPrice: ${product.price}\nCustomer: {request.user.username}\nEmail: {request.user.email}"
        }
        response = requests.post(url, json=payload, headers=headers)
        print("WaAPI Response:", response.text)
    except Exception as e:
        print("WhatsApp Error:", e)

    return render(request, 'order_success.html', {'product': product})
# --- NEW PAGES ---
def services_view(request):
    services = Product.objects.all()
    return render(request, 'services.html', {'services': services})
def portfolio_view(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})
def pricing_view(request):
    products = Product.objects.all()
    return render(request, 'pricing.html', {'products': products})
@login_required
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Order.objects.create(user=request.user, product=product)
    return render(request, 'order_success.html', {'product': product})
def services_view(request):
       return render(request, 'service.html')