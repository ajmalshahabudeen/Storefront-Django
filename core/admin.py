from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin
from store.models import Product
from core.models import User
from tags.models import TaggedItem

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]
    
    
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
