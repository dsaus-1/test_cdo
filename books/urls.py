from rest_framework.routers import DefaultRouter
from books.apps import BooksConfig
from books.views import BookViewSet

app_name = BooksConfig.name

router = DefaultRouter()
router.register('', BookViewSet, basename='book')

urlpatterns = router.urls