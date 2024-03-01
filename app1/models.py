from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=200 )
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    


class Login_details(models.Model):
      email=models.EmailField(primary_key=True)
      password = models.CharField(max_length=50)
class Registration(models.Model):
        name = models.CharField(max_length=200 )
        email=models.EmailField(primary_key=True)
        password = models.CharField(max_length=50)
        phone=models.CharField(max_length=50, default='SOME STRING')
class Posts(models.Model):
       title=models.CharField(max_length=200 )
       description=models.CharField(max_length=500)
       date_and_time=models.CharField(max_length=50, primary_key=True)
class TextCheck(models.Model):
    original_text = models.TextField()
    corrected_text = models.TextField()
# models.py


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    # Other fields and methods...
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # Add any additional fields you need for your user model
    confirm_password = models.CharField(max_length=255)


    def __str__(self):
        return f"TextCheck #{self.id}"
