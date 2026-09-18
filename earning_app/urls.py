from django.urls import path
from . import views
urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('earning/', views.earning_view, name='earning'),
]
