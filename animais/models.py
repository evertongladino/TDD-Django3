from django.db import models

class Animal(models.Model):
    nome_animal = models.CharField(max_length=100)
    predador = models.CharField(max_length=4)
    venenoso = models.CharField(max_length=4)
    domestico = models.CharField(max_length=4)
