from django.db import models
from django.contrib.auth.models import User #inheriting user id and name for making the items user created associated with him
from django.urls import * 
# Create your models here.
class Book(models.Model):
    def __str__(self): #for making the object named with its name 
        return self.book_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book_name = models.CharField(max_length=225)
    author_name = models.CharField(max_length=225)
    book_genre = models.CharField(max_length=225)
    book_year = models.IntegerField()
    book_cover = models.CharField(max_length=500, default="https://bookstoreromanceday.org/wp-content/uploads/2020/08/book-cover-placeholder.png")
    page_number = models.IntegerField()
    finished_date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
    