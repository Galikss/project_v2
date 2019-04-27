from django.shortcuts import render

from search.documents import ProductDocument

def search(request):

    q = request.GET.get("q")

    if q:
        products = ProductDocument.search().query("match", title=q)
    else:
        products = ''


    return render (request, search/search.html, {'products': products})