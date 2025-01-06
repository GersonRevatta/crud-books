from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from pymongo import MongoClient
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer, BookEditSerializer
from datetime import datetime
from bson.decimal128 import Decimal128
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from decimal import Decimal
from pymongo.errors import PyMongoError

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return BookEditSerializer
        return super().get_serializer_class()

    @swagger_auto_schema(
        operation_description="Lista todos los libros disponibles.",
        responses={200: BookListSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crea un nuevo libro.",
        request_body=BookEditSerializer,
        responses={201: BookEditSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class AveragePriceByYearView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, year):
        try:
            year = int(year)
        except ValueError:
            return Response(
                {"error": "Invalid year format. Please provide a valid integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            client = MongoClient(settings.MONGO_URI)
            db = client.get_database()
            books_collection = db["books_book"]
        except PyMongoError as e:
            return Response(
                {"error": f"Database connection error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        query = {"year": year, "price": {"$exists": True, "$ne": None}}
        projection = {"_id": 0, "title": 1, "year": 1, "price": 1}

        try:
            books_filtered = list(books_collection.find(query, projection))
        except PyMongoError as e:
            return Response(
                {"error": f"Database query error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        for book in books_filtered:
            if isinstance(book.get("price"), Decimal128):
                book["price"] = float(book["price"].to_decimal())
            elif isinstance(book.get("price"), Decimal):
                book["price"] = float(book["price"])

        if not books_filtered:
            return Response(
                {"message": f"No books found for the year {year}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        total_price = sum(book["price"] for book in books_filtered)
        average_price = round(total_price / len(books_filtered), 2)

        response_data = {
            "year": year,
            "average_price": average_price,
            "books_count": len(books_filtered),
            "books": books_filtered,
        }

        return Response(response_data, status=status.HTTP_200_OK)
