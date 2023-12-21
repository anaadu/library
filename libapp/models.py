from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=200)
    cat=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.FloatField()
    status=models.CharField(max_length=100)

class IssueBooks(models.Model):

    Student_name=models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, blank=True) 
    book_name=models.CharField(max_length=200)
    issued_date = models.DateField()
    