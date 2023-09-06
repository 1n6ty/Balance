from django.contrib import admin
from django.urls import path

from .views import index, privacy_policy, public_offer, suggestions, buy, buy_failure, buy_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('public_offer/', public_offer, name='public_offer'),
    path('suggestions/', suggestions),
    path('buy/failure', buy_failure),
    path('buy/success', buy_success),
    path('buy/', buy)
]
