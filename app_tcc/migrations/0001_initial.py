# Generated by Django 5.1.1 on 2024-09-30 01:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('papel', models.CharField(choices=[('orientador', 'Orientador'), ('orientando', 'Orientando'), ('admin', 'Admin')], default='orientando', max_length=15)),
                ('imagem_perfil', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tcc.curso')),
                ('groups', models.ManyToManyField(blank=True, related_name='app_tcc_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='app_tcc_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('capa_tcc', models.ImageField(blank=True, null=True, upload_to='tcc_covers/')),
                ('status', models.CharField(choices=[('em_andamento', 'Em andamento'), ('aguardando', 'Aguardando'), ('aprovado', 'Aprovado'), ('reprovado', 'Reprovado'), ('concluido', 'Concluído')], default='em andamento', max_length=20)),
                ('data_inicio', models.DateField()),
                ('data_entrega', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tcc.curso')),
                ('autores', models.ManyToManyField(limit_choices_to={'papel': 'orientando'}, related_name='tccs_autores', to='app_tcc.user')),
                ('orientador', models.ForeignKey(limit_choices_to={'papel': 'orientador'}, on_delete=django.db.models.deletion.CASCADE, related_name='tccs_orientador', to='app_tcc.user')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em progresso', 'Em Progresso'), ('concluída', 'Concluída')], default='pendente', max_length=20)),
                ('data_entrega', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tcc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tcc.tcc')),
                ('atribuida_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tcc.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('tipo', models.CharField(choices=[('texto', 'Texto'), ('anexo', 'Anexo')], default='texto', max_length=10)),
                ('titulo_anexo', models.CharField(blank=True, max_length=255)),
                ('tipo_anexo', models.CharField(blank=True, max_length=50)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('tcc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tcc.tcc')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tcc.user')),
            ],
        ),
    ]
