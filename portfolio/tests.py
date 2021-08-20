from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import home, services_offered
from .models import ServiceOffered, ServiceTypes

# Create your tests here.


class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class ServiceOfferedTests(TestCase):

    def setUp(self):
        ServiceOffered.objects.create(name='Development',
                                      description='Both Python and Java Development')

    def test_service_view_success_status_code(self):
        url = reverse('services_offered', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_service_view_not_found_status_code(self):
        url = reverse('services_offered', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_service_url_resolves_service_types_view(self):
        view = resolve('/services/1/')
        self.assertEquals(view.func, services_offered)