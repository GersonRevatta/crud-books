from django.core.management.base import BaseCommand
from books.models import Book
from django.utils.timezone import datetime

class Command(BaseCommand):
    help = "Seed database with initial books data"

    def handle(self, *args, **kwargs):
        books = [
            {"title": "1984", "author": "George Orwell", "published_date": datetime(1949, 6, 8), "genre": "Dystopian", "price": 19.99},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": datetime(1960, 7, 11), "genre": "Southern Gothic", "price": 14.99},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": datetime(1925, 4, 10), "genre": "Tragedy", "price": 10.99},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "published_date": datetime(1813, 1, 28), "genre": "Romantic Fiction", "price": 12.99},
            {"title": "The Hobbit", "author": "J.R.R. Tolkien", "published_date": datetime(1937, 9, 21), "genre": "Fantasy", "price": 25.99},
        ]

        for book in books:
            Book.objects.get_or_create(
                title=book["title"],
                author=book["author"],
                published_date=book["published_date"],
                genre=book["genre"],
                price=book["price"],
            )
        self.stdout.write(self.style.SUCCESS("Seed data added successfully!"))
