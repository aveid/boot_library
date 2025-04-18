from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'{self.full_name}-{self.birth_date}'


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public_date = models.DateField(null=True)


class Image(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='books', null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')



