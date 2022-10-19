from django.shortcuts import render, redirect
from .models import Product


def index(request):
    if request.method == "POST":
        prodcut_list = request.POST.getlist('product_id')
        for id in prodcut_list:
            product = Product.objects.get(pk=id)
            product.delete()
        return redirect('index')

    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)