from django.shortcuts import render

def portfolio_view(request):
    return render(request, 'index.html')

def earning_view(request):
    products = [
        {'name': 'Product 1', 'img': '1.jpeg', 'price': 500},
        {'name': 'Product 2', 'img': '2.jpeg', 'price': 700},
        {'name': 'Product 3', 'img': '3.jpeg', 'price': 900},
    ]
    return render(request, 'product_cart.html', {'products': products})
