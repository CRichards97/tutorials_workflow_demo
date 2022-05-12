from django.test import TestCase
from tutorials.models import Tutorial
from django.urls import reverse
import pytest

# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
    
@pytest.mark.django_db
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()