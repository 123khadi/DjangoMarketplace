from django.db import models
from django.contrib.auth.models import User

class EarningTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reward = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(blank=True)

    def _str_(self):
        return self.title

class UserEarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(EarningTask, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    def _str_(self):
        return f"{self.user.username} - {self.task.title}"
        from django.db import models

class EarningService(models.Model):
    title = models.CharField(max_length=100) # ex: Watch Ad, Referral
    price = models.IntegerField() # Earning amount
    description = models.TextField()
    def _str_(self):
        return self.title