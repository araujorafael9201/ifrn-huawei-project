from django.contrib import admin

from .models import *

admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Inscricao)
admin.site.register(Nota)
admin.site.register(Falta)
admin.site.register(Aula)

# Register your models here.
