from django.urls import path
from .views import  index, salas, reservarHorario, professores, turmas, disciplinas, seletor_turmas, atualizar_professor, deletar_professor, atualizar_disciplina, atualizar_sala, deletar_disciplina, criar_disciplina, criar_sala, deletar_sala
urlpatterns = [
    path("", index, name = "index"),
    path("salas", salas, name = "salas"),
    path("reservarHorario/<int:id>", reservarHorario, name = "reservarHorario"),
    path("professores", professores, name = "professores"),
    path("seletor_turmas", seletor_turmas, name = "seletor_turmas"),
    path("turmas", turmas, name = "turmas"),
    path("disciplinas", disciplinas, name = "disciplinas"),
    path('update/professor/<int:id>/', atualizar_professor, name='atualizar_professor'),
    path('update/disciplina/<int:id>/', atualizar_disciplina, name='atualizar_disciplina'),
    path('update/sala/<int:id>/', atualizar_sala, name='atualizar_sala'),
]
