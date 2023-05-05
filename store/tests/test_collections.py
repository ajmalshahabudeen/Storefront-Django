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
    