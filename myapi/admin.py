from django.contrib import admin

# Changes begin here....
from .models import Hero

# Include another class
class admin_heroes(admin.ModelAdmin):
    list_display = ('id','name','address','phone','total')
    
# Register your models here.
admin.site.register(Hero,admin_heroes)

