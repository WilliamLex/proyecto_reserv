from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nombre", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'
    
class Medico(models.Model):
    nome = models.CharField(verbose_name="Nombre del laboratorio", max_length=200)
    email = models.EmailField(verbose_name="Correo electronico")
    crm = models.CharField(verbose_name="Nombre del responsable CRM", max_length=200)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="El número debe estar en este formato:: \
                    '+593 999999999'.")

    telefone = models.CharField(verbose_name="Telefono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    especialidade = ForeignKey(Especialidade,
                               on_delete=models.CASCADE,
                               related_name='Laboratorios')
    
    def __str__(self):
        return f'{self.nome}'

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible elegir una fecha pasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Elige un día laborable de la semana.')

class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Ingrese una fecha para la agenda", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
        ("6", "12:00 a 13:00"),
        ("7", "13:00 a 14:00"),
        ("8", "14:00 a 15:00"),
        ("9", "15:00 a 16:00"),
        ("10", "16:00 a 17:00"),
        ("11", "17:00 a 18:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico}'