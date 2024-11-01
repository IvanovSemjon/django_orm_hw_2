from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    sort_pages = request.GET.get('sort', '')
    if sort_pages == 'max_price':
        phones_objects = phones_objects.order_by('price').reverse()
    elif sort_pages == 'min_price':
        phones_objects == phones_objects.order_by('price')
    elif sort_pages == 'name':
        phones_objects == phones_objects.order_by('name')
    else:
        phones_objects = Phone.objects.all()

    context = {
        'phones': phones_objects,
    }
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
