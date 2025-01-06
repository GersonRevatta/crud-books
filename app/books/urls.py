from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import BookViewSet, AveragePriceByYearView

router = DefaultRouter()
router.register('', BookViewSet, basename='book')

urlpatterns = router.urls + [
    path('average-price/<int:year>/', AveragePriceByYearView.as_view(), name='average-price'),
]
