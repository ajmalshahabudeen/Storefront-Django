from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_anonymous_returns_401(self):
        # Every test have three points.
        # AAA (Arrange, Act, Assert)
        
        # Arrange
        
        # Act
        client = APIClient()
        response = client.post('/store/collections/', {'title':'a'})
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_if_user_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title':'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN   
    