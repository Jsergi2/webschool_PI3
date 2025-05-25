from django.db import models
from django.contrib.auth.models import User
from secretaria.models import Cadastro_Aluno, Cadastro_Professor, Turma
from django.utils import timezone

class Presenca(models.Model):
    aluno = models.ForeignKey(Cadastro_Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor = models.ForeignKey(Cadastro_Professor, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField(default=timezone.now)
    presente = models.BooleanField(default=False)
    observacao = models.TextField(blank=True, null=True)
    usuario_registro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="presencas_registradas")

    class Meta:
        unique_together = ('aluno', 'data', 'turma')
        ordering = ['-data']
        verbose_name = "Registro de Presença"
        verbose_name_plural = "Registros de Presença"

    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        return f"{self.aluno.nome} - {self.turma} - {status} em {self.data.strftime('%d/%m/%Y')}"
