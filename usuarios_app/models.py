from django.db import models

class Usuario:
    nome = models.TextField()
    sobrenome = models.TextField()
    email = models.EmailField(max_length = 100)
    telefone = models.CharField(max_length = 11)





