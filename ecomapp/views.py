from django.shortcuts import render
from ecomapp.models import Category, Product



def base_view(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    context = {
        'categories': categories,
        'product': product

    }
    return render(request, 'base.html', context)




def  product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()

    context = {
        "product": product,
        'categories': categories,

    }

    return render(request, 'product.html', context)

def  category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    product_of_category = Product.objects.filter(category=category)

    context = {
        "category": category,
        "product_of_category": product_of_category
    }

    return render(request, 'category.html', context)


