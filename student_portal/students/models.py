from django.db import models



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address1 = models.TextField()
    address2 = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
