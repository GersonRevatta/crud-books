from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book

User = get_user_model()

class BookViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword", email="test@gmail.com")
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.book1 = Book.objects.create(title="Book 1", year=2021, price=100)
        self.book2 = Book.objects.create(title="Book 2", year=2022, price=150)

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book 1")

    def test_create_book(self):
        data = { "title": "New Book", "price": 200, "published_date": "2023-04-03", "price": "143.99", "author": "Author" }
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book(self):
        data = { "title": "Updated Book", "price": 120, "published_date": "2023-04-03", "price": "143.99", "author": "Author" }
        response = self.client.put(f"/api/books/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
