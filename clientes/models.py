from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.db import models
from medicos.models import Agenda

class Cliente(models.Model):
    SEXO = (
        ("MAS", "Maculino"),
        ("FEM", "Feminino")
    )
    
    sexo = models.CharField(max_length=9, choices=SEXO,)
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número debe estar en el formato: \
                        '+593 999999999'.")

    telefone = models.CharField(verbose_name="Telefono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    cpf = CPFField(verbose_name="CI",
                    max_length=50,
                    unique=True,)
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.user.name}'
    
class Consulta(models.Model):
    agenda =  OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consulta')
    
    class Meta:
        unique_together = ('agenda', 'cliente')
        
    def __str__(self):
        return f'{self.agenda} - {self.cliente}'
