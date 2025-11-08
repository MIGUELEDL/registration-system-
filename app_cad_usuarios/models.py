from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) #cria um número sequencial e não duplicado para o ID do úsuario
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    
