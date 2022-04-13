from django.db import models



class Product(models.Model):
    publisher = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posted_product')
    title = models.CharField(max_length=31)
    description = models.TextField()
    target_amount = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    sponsors = models.ManyToManyField(
        'accounts.User',
        through='products.Sponsor',
        through_fields=('product', 'sponsor'),
    )
    deadline = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

class Sponsor(models.Model):
    sponsor = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    funding_amount = models.PositiveIntegerField()