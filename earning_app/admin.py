from django.contrib import admin
from .models import Product, Order

# Agar aapke models ka naam alag hai to neeche wale try karo
try:
    from .models import PricingPlan, Portfolio
    admin.site.register(PricingPlan)
    admin.site.register(Portfolio)
except:
    pass

try:
    from .models import Pricing
    admin.site.register(Pricing)
except:
    pass

admin.site.register(Product)
admin.site.register(Order)