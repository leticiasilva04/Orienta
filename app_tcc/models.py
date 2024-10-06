from django.db import models
from django.contrib.auth.models import AbstractUser

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class User(AbstractUser):
    # Papel de cada usuário
    ORIENTADOR = 'orientador'
    ORIENTANDO = 'orientando'
    ADMIN = 'admin'
    
    PAPEL_CHOICES = [
        (ORIENTADOR, 'Orientador'),
        (ORIENTANDO, 'Orientando'),
        (ADMIN, 'Admin'),
    ]

    papel = models.CharField(max_length=15, choices=PAPEL_CHOICES, default=ORIENTANDO)
    imagem_perfil = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    # Adicione os related_names para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app_tcc_user_set',  # Mude o nome conforme necessário
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app_tcc_user_set',  # Mude o nome conforme necessário
        blank=True,
    )

    def __str__(self):
        return self.username

class TCC(models.Model):
    STATUS_CHOICES = [
        ('em_andamento', 'Em andamento'),
        ('aguardando', 'Aguardando'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
        ('concluido', 'Concluído'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    capa_tcc = models.ImageField(upload_to='tcc_covers/', blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    autores = models.ManyToManyField(User, related_name='tccs_autores', limit_choices_to={'papel': 'orientando'})
    orientador = models.ForeignKey(User, related_name='tccs_orientador', on_delete=models.CASCADE, limit_choices_to={'papel': 'orientador'})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em andamento')
    data_inicio = models.DateField()
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo

class Message(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto'),
        ('anexo', 'Anexo')
    ]

    remetente = models.ForeignKey(User, on_delete=models.CASCADE)
    tcc = models.ForeignKey(TCC, on_delete=models.CASCADE)
    conteudo = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='texto')
    titulo_anexo = models.CharField(max_length=255, blank=True)
    tipo_anexo = models.CharField(max_length=50, blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remetente.username} - {self.tcc.titulo}'

class Task(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em progresso', 'Em Progresso'),
        ('concluída', 'Concluída')
    ]

    tcc = models.ForeignKey(TCC, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_entrega = models.DateField()
    atribuida_a = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

        from django.contrib.auth.models import User

def user_is_orientador(user):
    return hasattr(user, 'orientador')

def user_is_aluno(user):
    return hasattr(user, 'aluno')

User.add_to_class("is_orientador", property(lambda u: user_is_orientador(u)))
User.add_to_class("is_aluno", property(lambda u: user_is_aluno(u)))