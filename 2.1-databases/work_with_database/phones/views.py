from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')
    else:
        phones_objects = Phone.objects.all().order_by('name')

    context = {
        'phones': phones_objects
    }
    return render(request, 'catalog.html', context)

def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})
