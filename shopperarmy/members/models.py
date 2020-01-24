from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    # gender is a one char string of (M/F/O) male, female, other
    # although sqlite will not enforce this
    gender = models.CharField(max_length=1, null=True)

    # country is a string
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username + ' from ' + self.country

if __name__ == "__main__":
    # Was not sure what, "Create a command that creates a Member object..." 
    # meant but here is what I think it means
    me = Member(username="me", email="me@mail.com", country="Meville", gender="O")