from django.shortcuts import render

def properties_list(request):
    html = "propertieslist.html"
    return render(request, html)

def properties_page(request):
    html = "propertypage.html"
    return render(request, html)