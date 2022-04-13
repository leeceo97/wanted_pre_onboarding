from django.contrib import admin
from .models import Product, Sponsor

admin.site.register([Product, Sponsor])