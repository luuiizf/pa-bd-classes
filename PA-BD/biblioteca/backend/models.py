from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano_publicacao = models.DateField()
    genero = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Autor(models.Model):
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()

    def __str__(self):
        return f"{self.livro} - {self.usuario}"

class Reserva(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_reserva = models.DateField()

    def __str__(self):
        return f"{self.livro} - {self.usuario}"

class Multa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.valor}"

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
