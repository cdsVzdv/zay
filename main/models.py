from django.db import models

# Create your models here.

class Kirish(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Kirish1(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Catigory(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class Product(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi
        
class Featured_Product(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class Featured_Product1(models.Model):
    rasm = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=100)
    pulli = models.CharField(max_length=100)
    haqida = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class About_kirish(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Shop_kirish(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.TextField()
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Shop_kiyimlar(models.Model):
    nomi = models.CharField(max_length=100)
    razmerlari = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='media/')
    pulli = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Contact_kirish(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.TextField()
    def __str__(self):
        return self.nomi

class Sms(models.Model):
    ismiz = models.CharField(max_length=100)
    gmail_ismi = models.CharField(max_length=100)
    ishi = models.CharField(max_length=100)
    xabar = models.CharField(max_length=100)
    def __str__(self):
        return self.ismi  