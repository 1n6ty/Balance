from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Purchases, Services, Rates

@admin.register(Purchases)
class Purchases_admin(admin.ModelAdmin):
    list_display = ('get_full_name', 'date_time', 'rate')
    list_filter = ('rate', ('date_time', DateFieldListFilter))
    search_fields = ('first_name', 'last_name', 'rate', 'phone', 'email')

    @admin.display(description='Имя')
    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return True

@admin.register(Services)
class Services_admin(admin.ModelAdmin):
    list_display = ('get_full_name', )

    @admin.display(description='Пакет услуг')
    def get_full_name(self, obj):
        return f'Пакет услуг №{obj.pk}'
    
@admin.register(Rates)
class Rates_admin(admin.ModelAdmin):
    list_display = ('name', 'cost')