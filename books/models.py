from django.db import models


def get_upload_path(instance, filename):
    return f'books/{filename}'

class Book(models.Model):


    title = models.CharField(max_length=250, verbose_name='Book title')
    author = models.CharField(max_length=250, verbose_name='Author')
    book = models.FileField(upload_to=get_upload_path, max_length=250, verbose_name='Book file')

    class Meta:
        unique_together = ('title', 'author')

        verbose_name = 'Book'
        verbose_name_plural = 'Books'