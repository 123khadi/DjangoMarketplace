from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get-started/', views.get_started, name='get_started'),
    path('product-cart/', views.product_cart, name='product_cart'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('pricing/', views.pricing_view, name='pricing'),
   path('buy/<int:product_id>/', views.buy_now, name='buy_now'), 
    
]