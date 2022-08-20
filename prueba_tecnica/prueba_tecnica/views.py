from django.shortcuts import render
from django.shortcuts import redirect
from prueba_tecnica.api import EasyBrokerAPIManager
import json

def properties_list(request):
    if request.method== 'GET':
        html = "propertieslist.html"

        page_number = request.GET.get('page','')

        if page_number == '':
            return redirect('/?page=1')
        
        if page_number == "NaN":
            return redirect('/?page=2')

        url = "https://api.stagingeb.com/v1/properties?page=" + page_number + "&limit=15&search%5Bstatuses%5D%5B%5D=published"
        auth_token = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        jsonresponse = EasyBrokerAPIManager(auth_token).get_properties(url)

        context = jsonresponse
        return render(request, html, context)

def properties_page(request):
    if request.method== 'GET':
        html = "propertypage.html"        

        public_id = request.GET.get('public_id','')

        url = "https://api.stagingeb.com/v1/properties/" + public_id
        auth_token = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        jsonresponse = EasyBrokerAPIManager(auth_token).get_properties(url)

        context = jsonresponse
        return render(request, html, context)

    if request.method== 'POST':
        html = "propertypage.html"

        name = request.POST.get('leadname')
        print(name)
        phone = request.POST.get('phone')
        print(phone)
        email = request.POST.get('email')
        print(email)
        publicid = request.POST.get('publicid')
        print(publicid)
        message = request.POST.get('message')
        print(message)

        json_data = {
            'name': name,
            'phone': phone,
            'email': email,
            'property_id': publicid,
            'message': message,
            'source': 'mydomain.com',
        }

        auth_token = "l7u502p8v46ba3ppgvj5y2aad50lb9"
        eb_api = EasyBrokerAPIManager(auth_token)

        url = 'https://api.stagingeb.com/v1/contact_requests'
        response = eb_api.post_contact_requests(url, json_data)

        print(response)
        print(response.text)
        url = "https://api.stagingeb.com/v1/properties/" + publicid
        jsonresponse = eb_api.get_properties(url)
        context = jsonresponse

        print("Llega")

        context['response'] =  json.loads(response.text)
        print(context)
        print("Llega")

        return render(request, html, context)