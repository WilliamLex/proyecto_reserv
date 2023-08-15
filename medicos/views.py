from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medico, Agenda, Especialidade


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "No tienes permisos!"
        )
        return redirect("accounts:index")

class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'Laboratorios/registro.html'
    fields = ['nome', 'crm', 'email', 'telefone', 'especialidade']
    success_url = reverse_lazy('medicos:medicos_lista')
    
class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Laboratorios/medicos_list.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')
    
class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'Laboratorios/registro.html'
    fields = ['nome',]
    success_url = reverse_lazy('Laboratorios:especialidade_lista')
    
class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Laboratorios/especialidade_list.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'Laboratorios/agenda_registro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('Laboratorios:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'Laboratorios/agenda_registro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('Laboratorios:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('Laboratorios:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "¡Reserva eliminada exitosamente!")
        return reverse_lazy('Laboratorios:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'Laboratorios/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')
    
laboratorio_registro = MedicoCreateView.as_view()
laboratorio_lista = MedicoListView.as_view()
carrera_registro = EspecialidadeCreateView.as_view()
carreras_lista = EspecialidadeListView.as_view()
agenda_registro = AgendaCreateView.as_view()
agenda_actualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()

