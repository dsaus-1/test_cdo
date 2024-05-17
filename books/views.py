from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, )
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        obj = Book.objects.filter(title=request.data.get('title'),author=request.data.get('author'))

        headers = self.get_success_headers(serializer.initial_data)
        if obj:
            serializer = self.serializer_class(obj[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        self.renderer_classes = (CSVRenderer, )
        return super(ModelViewSet, self).list(request, *args, **kwargs)