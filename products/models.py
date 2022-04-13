import datetime
import math
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    publisher = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posted_product')
    title = models.CharField(max_length=31)
    description = models.TextField()
    target_amount = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    one_time_funding_amount = models.PositiveIntegerField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def sponsor_count(self):
        return self.sponsor_set.count()

    @property
    def achievement_rate(self):
        return f'{math.floor((self.total_amount / self.target_amount) * 100)}%'

    @property
    def d_day(self):
        today = datetime.date.today()
        return (self.deadline-today).days

    @property
    def publisher_name(self):
        return self.publisher.username


class Sponsor(models.Model):
    sponsor = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

@receiver(post_save, sender=Sponsor)
def create_sponsor_total_amount(sender, instance, created, **kwargs):
    if created:
        instance.product.total_amount += instance.product.one_time_funding_amount
        instance.product.save()