from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from products.forms import ProductForm

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def emp(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.uploadedBy = request.user
                obj.save()
                return redirect("../../products/show")
            except:
                pass
        else:
            # Added else statment
            msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse(msg, status=400)
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    products = Product.objects.filter(uploadedBy=request.user)
    return render(request, "show.html", {'products': products})


def edit(request, id):
    product = Product.objects.get(id=id)
    product.category = ['Fruit', 'Vegetable', 'Other']
    return render(request, 'edit.html', {'product': product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    
    if form.is_valid():
        form.save()
        return redirect("../../products/show")
    else:
        # Added else statment
        msg = 'Errors: %s' % form.errors.as_text()
        return HttpResponse(msg, status=400)


def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("../../products/show")
