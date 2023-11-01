from django.db import models

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_disciplina
    
class Conteudo(models.Model):
    nome_conteudo = models.CharField(max_length=50)
    descricao_conteudo = models.TextField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome_conteudo} - {self.disciplina}'
   
class Cartao(models.Model):
    termo = models.CharField(max_length=100)
    definicao = models.TextField()
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.termo} {self.definicao} {self.conteudo}'
   