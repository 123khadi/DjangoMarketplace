from django.db import models
from django.contrib.auth.models import User
class EarningTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reward = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title
class UserEarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(EarningTask, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.task.title}"
class EarningService(models.Model):
    title = models.CharField(max_length=100)  # ex: Watch Ad, Referral
    price = models.IntegerField()  # Earning amount
    description = models.TextField()
    def __str__(self):
        return self.title
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    icon = models.CharField(max_length=10, default="🚀")  # emoji ke liye
    tag1 = models.CharField(max_length=20, default="Django")
    tag2 = models.CharField(max_length=20, default="Python")
    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
class Portfolio(models.Model):
    title = models.CharField(max_length=100)  # jaise Hospital Management System
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title