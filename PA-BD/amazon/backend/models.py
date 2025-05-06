from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
class Item(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.preco}'