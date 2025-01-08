from django.db import models

# Create your models(classes) here.

class Topic(models.Model): # Herda de Model
    """Um tópico que o usuário está aprendendo"""
    # Atributos
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # Método que representa as instancias de Topic em texto
    def __str__(self):
        """"Retorna uma representacao de string do modelo"""
        return self.text
    
class Entry(models.Model):
    """"Algo específico aprendido sobre um tópico"""
    # Atributos
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ID
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' # Configuracao do modelo

    def __str__(self):
        """"Retorna uma string simples representando a entrada"""
        return f"{self.text[:50]}"

