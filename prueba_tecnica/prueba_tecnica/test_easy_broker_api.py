# Standard library imports...
from unittest.mock import Mock, patch, PropertyMock
import json
# Third-party imports...
from nose.tools import assert_is_not_none, assert_is_none, assert_equal

# Local imports
from prueba_tecnica.easy_broker_api import EasyBrokerAPIManager


def test_easy_broker_api_manager_get_properties():
    #Hacemos un mock de requests.get 
    with patch('prueba_tecnica.easy_broker_api.requests.get') as mock_get:
        # Creamos una respuesta predecible
        json_data = [{
            "public_id": "EB-B5338",
            "property_images": [
                {
                "url": "https://www.easybroker.com/assets/product/logo-be4da843987ccd1c05e26f8703f1787847471b36d08bdb1ec8a91ce4007b0e98.svg",
                "title": "Fitted kitchen with granite countertops"
                }
            ],
            "title": "Locales en Venta Edificio Roble en San Pedro Garza Garcia",
            "description": "This property is very well-lit in a lovely neighborhood overlooking a park.",
            "bedrooms": 0,
        }]


        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = json_data

        eb_api = EasyBrokerAPIManager("Filler")
        response = eb_api.get_properties('Filler')

    assert_is_not_none(response)
    assert_equal(response, json_data)

def test_easy_broker_api_manager_post_contact_requests():
    #Hacemos un mock de requests.post 
    with patch('prueba_tecnica.easy_broker_api.requests.post') as mock_get:
        json_data = {'status': 'successful'}

        mock_get.return_value = json_data

        eb_api = EasyBrokerAPIManager("Filler")
        response = eb_api.post_contact_requests('Filler','Filler')


    assert_is_not_none(response)
    assert_equal(response, json_data)
