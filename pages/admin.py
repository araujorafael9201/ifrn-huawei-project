from django.contrib import admin

from .models import *

admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Inscricao)

# Register your models here.
