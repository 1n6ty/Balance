from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

import os
from dotenv import load_dotenv
load_dotenv()

from .models import Rates, Purchases

import re

phone_p = re.compile(r'\+?[0-9]{9,14}$')

import decimal
import hashlib
from urllib import parse

def calculate_signature(*args) -> str:
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()

def check_signature_result(
    order_number: int,
    received_sum: decimal,
    received_signature: str,
    password_1: str,
    shp_email: str,
    shp_id_rate: str,
    shp_name: str,
    shp_phone: str
) -> bool:
    signature = calculate_signature(received_sum, order_number, password_1, f'Shp_email={shp_email}', f'Shp_id_rate={shp_id_rate}', f'Shp_name={shp_name}', f'Shp_phone={shp_phone}')
    if signature.lower() == received_signature.lower():
        return True
    return False

def index(req):
    if req.method == 'GET':
        rates = [[i.pk, i.cost, i.name, [j for j in zip(i.service.services.split('|'), i.mask.split(','))]] for i in Rates.objects.all()]
        
        return render(req, 'index/index.html', {'rates': rates})
    return HttpResponse(status = 404)

def privacy_policy(req):
    if req.method == 'GET':
        return render(req, 'privacy_policy/privacy_policy.html', {'domain': req.build_absolute_uri('/')})
    return HttpResponse(status = 404)

def public_offer(req):
    if req.method == 'GET':
        return render(req, 'public_offer/public_offer.html', {'domain': req.build_absolute_uri('/')})
    return HttpResponse(status = 404)

def suggestions(req):
    if req.method == 'POST':
        if (not req.POST.get('name', None)) or (not req.POST.get('text', None)) or (not req.POST.get('email', None)) or (not req.POST.get('tel', None)):
            return HttpResponse(status = 400)

        if (not phone_p.match(req.POST.get('tel'))):
            return HttpResponse(status = 400)

        send_mail("Пожелания \"Баланс 3.0\"", 
                  f"Имя: {req.POST.get('name')}\nEmail: {req.POST.get('email')}\nНомер телефона: {req.POST.get('tel')}\nКомментарий: {req.POST.get('text')}", 
                  settings.EMAIL_HOST_USER, (os.environ.get('EMAIL_TO'), ))
        return HttpResponseRedirect('/')
    else:
        return HttpResponse(status = 404)

def buy_failure(req):
    if req.method == 'GET':
        for i in req.GET:
            print(i, req.GET.get(i))
        return render(req, 'purchase/purchase.html', {'success': False})
    return HttpResponse(status = 404)

def buy_success(req):
    if req.method == 'GET':
        if (not req.GET.get('OutSum', None)) or (not req.GET.get('InvId', None)) or (not req.GET.get('Shp_email', None)) or (not req.GET.get('Shp_id_rate', None)) or ((not req.GET.get('Shp_name', None))) or (not req.GET.get('Shp_phone', None)) or (not req.GET.get('SignatureValue', None)):
            return HttpResponse(status = 400)
        
        if not check_signature_result(req.GET.get('InvId'), req.GET.get('OutSum'), req.GET.get('SignatureValue'), os.environ.get('merchant_password_1'), req.GET.get('Shp_email'), req.GET.get('Shp_id_rate'), req.GET.get('Shp_name'), req.GET.get('Shp_phone')):
            return HttpResponse(status = 400)
        
        name = req.GET.get('Shp_name').split(' ')
        name = [*name, *['' for i in range(3 - len(name))]]

        Purchases.objects.create(first_name = name[0], 
                                last_name = name[1], 
                                middle_name = name[2], 
                                rate = f"{Rates.objects.get(pk = int(req.GET.get('Shp_id_rate'))).name} / {req.GET.get('OutSum')}",
                                phone = req.GET.get('Shp_phone'),
                                email = req.GET.get('Shp_email'))
        
        #send_mail(req.POST.get('name', ''), req.POST.get('text', '') + req.POST.get('email', ''), settings.EMAIL_HOST_USER, (os.environ.get('EMAIL_TO'), ), fail_silently=True) TODO Refractor

        return render(req, 'purchase/purchase.html', {'success': True})
    return HttpResponse(status = 404)

def buy(req):
    if req.method == 'GET':
        for i in req.GET:
            print(i, req.GET.get(i))
        return HttpResponse('Hello', status = 200)
    if req.method == 'POST':
        if (not req.POST.get('name', None)) or (not req.POST.get('email', None)) or (not req.POST.get('tel', None)) or (not req.POST.get('id_rate', None)):
            return HttpResponse(status = 400)
        
        if not Rates.objects.filter(pk = int(req.POST.get('id_rate'))).exists():
            return HttpResponse(status = 400)

        rate = Rates.objects.get(pk = int(req.POST.get('id_rate')))

        data = {
            'MerchantLogin': os.environ.get('merchant_login'),
            'OutSum': int(rate.cost), # cost
            'InvId': 0, # invoice number
            'Description': 'test purchase',
            'SignatureValue': calculate_signature(
                os.environ.get('merchant_login'),
                int(rate.cost), # cost
                0, # invoice number
                os.environ.get('merchant_password_1'),
                f'Shp_email={req.POST.get("email")}',
                f'Shp_id_rate={req.POST.get("id_rate")}',
                f'Shp_name={req.POST.get("name")}',
                f'Shp_phone={req.POST.get("tel")}'
            ),
            'IsTest': 1,
            'Email': req.POST.get("email"),
            'Shp_email': req.POST.get("email"),
            'Shp_id_rate': req.POST.get('id_rate'),
            'Shp_name': req.POST.get("name"),
            'Shp_phone': req.POST.get("tel")
        }

        return HttpResponseRedirect(os.environ.get("robokassa_payment_url") + '?' + parse.urlencode(data))
    return HttpResponse(status = 404)