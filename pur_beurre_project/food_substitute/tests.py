#Import django libraries
from django.test import TestCase
from django.urls import reverse

class ViewsTests(TestCase):
    """This class contains all the tests for the views of this app."""

    def setUp(self):
        """This method is called before each test."""

        pass

    def test_home_get(self):
        """This function tests the 'home' view with a GET HTTP method."""

        response = self.client.get('')
        assert response.status_code == 200

    def test_home_post(self):
        """This function tests the 'home' view with a POST HTTP method."""

        response = self.client.post('', {'research': 'Nutella'})
        assert response.status_code == 302

    def test_search(self):
        """This function tests the 'search' view."""

        response = self.client.get(reverse('search', args=['Nutella']))
        assert response.status_code == 200

    def test_display(self):
        """This function tests the 'display' view."""

        response = self.client.get(reverse('display', args=['Nutella']))
        assert response.status_code == 200
