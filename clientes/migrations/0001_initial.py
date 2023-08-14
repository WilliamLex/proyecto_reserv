
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('MAS', 'Maculino'), ('FEM', 'Feminino')], max_length=9)),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                         '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=50, unique=True, verbose_name='CPF')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='medicos.agenda')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='clientes.cliente')),
            ],
            options={
                'unique_together': {('agenda', 'cliente')},
            },
        ),
    ]