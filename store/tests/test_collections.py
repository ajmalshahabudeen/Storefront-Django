from django.contrib.auth.models import User
from rest_framework import status
# from rest_framework.test import APIClient
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection): # closure concept
        return api_client.post('/store/collections/', collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_anonymous_returns_401(self, create_collection):
        # Every test have three points.
        # AAA (Arrange, Act, Assert)
        
        # ---- Arrange ----
        
        # ---- Act ----
        # client = APIClient()
        # response = api_client.post('/store/collections/', {'title':'a'})
        response = create_collection({'title':'a'})
        
        # ---- Assert ----
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_not_admin_returns_403(self, create_collection, authenticate):
        # client = APIClient()
        # api_client.force_authenticate(user={})
        authenticate() #-- Arrange
        
        response = create_collection({'title':'a'}) #-- Act
        
        assert response.status_code == status.HTTP_403_FORBIDDEN  #-- Assert 
    
    def test_if_data_is_invalid_returns_400(self, create_collection, authenticate):
        # client = APIClient()
        # api_client.force_authenticate(user=User(is_staff=True))
        authenticate(is_staff=True) #-- Arrange
        
        response = create_collection({'title':''}) #-- Act
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST  #-- Assert  
        assert response.data['title'] is not None                   #-- Assert 
    
    def test_if_data_is_valid_returns_200(self, create_collection, authenticate):
        # client = APIClient()
        # api_client.force_authenticate(user=User(is_staff=True))
        authenticate(is_staff=True) #-- Arrange
        
        response = create_collection({'title':'a'}) #-- Act
        
        assert response.status_code == status.HTTP_201_CREATED  #-- Assert 
        assert response.data['id'] > 0                          #-- Assert 