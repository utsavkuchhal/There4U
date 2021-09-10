from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, blank=True, default="")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null= True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.IntegerField()
    balance = models.IntegerField(default=0)
    is_owner = models.BooleanField(default= False)

    def __str__(self):
        return self.name