from django.urls import path
from . import views

app_name = 'Laboratorios'

urlpatterns = [
    path('registro/Laboratorios/', views.laboratorio_registro, name='medico_cadastro'),
    path('registro/especialidade/', views.carrera_registro, name='especialidade_cadastro'),
    path('agendar/', views.agenda_registro, name='agendar_consulta'),
    path('agendar/atualizar/<int:pk>/', views.agenda_actualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    path('lab/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/medicos/', views.laboratorio_lista, name="medicos_lista"),
    path('admim/lista/especialidades/', views.carreras_lista, name="especialidade_lista")
    
]