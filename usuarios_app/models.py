from django.db import models

class Usuario:
    nome = models.TextField(min_legth = 1)
    sobrenome = models.TextField(min_legth = 1)
    email = models.EmailField(max_length = 100)
    telefone = models.CharField(max_length = 11)





