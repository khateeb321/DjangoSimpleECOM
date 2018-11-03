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
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request, "show.html", {'products': products})


def edit(request, id):
    product = Product.objects.get(id=id)
    product.category = ['Fruit', 'Vegetable']
    return render(request, 'edit.html', {'product': product})


def update(request, id):
    cat = ['Fruit', 'Vegetable']
    product = Product.objects.get(id=id)
    # product.category = ['Fruit', 'Vegetable']
    form = ProductForm(request.POST, instance=product)
    selected_item = get_object_or_404(Product, pk=request.POST.get('category'))
    # get the user you want (connect for example) in the var "user"
    product.category = selected_item
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
    return redirect("/show")
