from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='artigo_images/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
