from django.shortcuts import render
from django.shortcuts import redirect
from prueba_tecnica.api import EasyBrokerAPIReader

def properties_list(request):
    if request.method== 'GET':
        html = "propertieslist.html"

        page_number = request.GET.get('page','')

        if page_number == '':
            return redirect('/?page=1')

        url = "https://api.stagingeb.com/v1/properties?page=" + page_number + "&limit=15&search%5Bstatuses%5D%5B%5D=published"
        auth_token = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        jsonresponse = EasyBrokerAPIReader(auth_token).get_properties(url)

        context = jsonresponse
        return render(request, html, context)

def properties_page(request):
    if request.method== 'GET':
        html = "propertypage.html"        

        public_id = request.GET.get('public_id','')

        url = "https://api.stagingeb.com/v1/properties/" + public_id
        auth_token = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        jsonresponse = EasyBrokerAPIReader(auth_token).get_properties(url)

        context = jsonresponse
        return render(request, html, context)