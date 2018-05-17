#Import django libraries
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTests(TestCase):
    """This class contains all the tests for the views of this app."""

    def setUp(self):
        """This method is called before each test."""

        pass

    def create_user(self):
        """This function creates a new user for a testing purpose."""

        User.objects.create_user("test@mail.com", "test@mail.com", "passwd")

    def login_user(self):
        """This function logs in a user for a testing purpose."""

        self.client.login(username="test@mail.com", password="passwd")

    def test_home_get(self):
        """This function tests the 'home' view with a GET HTTP method."""

        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_home_post(self):
        """This function tests the 'home' view with a POST HTTP method."""

        response = self.client.post(reverse('home'), {'research': 'Nutella'})
        assert response.status_code == 302

    def test_search(self):
        """This function tests the 'search' view."""

        response = self.client.get(reverse('search', args=['Nutella']))
        assert response.status_code == 200

    def test_display(self):
        """This function tests the 'display' view."""

        response = self.client.get(reverse('display', args=['Nutella']))
        assert response.status_code == 200

    def test_create_account_get(self):
        """This function tests the 'create_account' view with a GET HTTP
        method."""

        response = self.client.get(reverse('create_account'))
        assert response.status_code == 200

    def test_create_account_post(self):
        """This function tests the 'create_account' view with a POST HTTP
        method."""

        nb_users_1 = User.objects.count()
        response = self.client.post(reverse('create_account'),
                                    {"email": "test.mail@mailtester.com", "password": "passwd"})
        nb_users_2 = User.objects.count()

        assert response.status_code == 302
        assert nb_users_1 + 1 == nb_users_2

    def test_login_get(self):
        """This function tests the 'login' view with a GET HTTP method."""

        response = self.client.get(reverse('login'))
        assert response.status_code == 200

    def test_login_post_wrong_user(self):
        """This function tests the 'login' view with a POST HTTP method and
        a wrong user."""

        response = self.client.post(reverse('login'), {"email": "test@mail.com",
                                                       "password": "passwd", "next":"next"})
        assert response.status_code == 200

    def test_login_post_right_user(self):
        """Thus function tests the 'login' view with a POST HTTP method and
        a right user."""

        self.create_user()
        response = self.client.post(reverse('login'), {"email": "test@mail.com",
                                                       "password": "passwd", "next": "next"})
        assert response.status_code == 302

    def test_logout(self):
        """This function tests the 'logout' view."""

        response = self.client.get(reverse('logout'))
        assert response.status_code == 302

    def test_bookmark_not_yet_logged(self):
        """This function tests the 'bookmark' view when the user is not yet
        logged."""

        response = self.client.get(reverse('bookmark'))
        assert response.status_code == 302

    def test_bookmark_already_logged(self):
        """This function tests the 'bookmark' view when the user is logged."""

        self.create_user()
        self.login_user()
        response = self.client.get(reverse('bookmark'))
        assert response.status_code == 200

    def test_save_product_not_yet_logged(self):
        """This function tests the 'save_product' view when the user is not yet
        logged."""

        response = self.client.get(reverse('save_product', args=['Nutella']))
        assert response.status_code == 302

    def test_save_product_already_logged(self):
        """This function tests the 'save_product' view when the user is logged."""

        self.create_user()
        self.login_user()
        response = self.client.get(reverse('save_product', args=['Nutella']))
        assert response.status_code == 302

    def test_legal_notices(self):
        """This function tests the 'legal_notices' view."""

        response = self.client.get(reverse('legal_notices'))
        assert response.status_code == 200
