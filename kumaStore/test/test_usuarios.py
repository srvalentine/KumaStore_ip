import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

@pytest.mark.django_db
def test_user_registration():
    client = Client()
    
    user_data = {
        'username': 'newuser',
        'password1': 'complexpassword123',
        'password2': 'complexpassword123',
    }

    response = client.post(reverse('registrar'), data=user_data)
    
    assert response.status_code == 302

    user = User.objects.filter(username='newuser').first()
    assert user is not None
    assert user.username == 'newuser'
    assert user.check_password('complexpassword123')