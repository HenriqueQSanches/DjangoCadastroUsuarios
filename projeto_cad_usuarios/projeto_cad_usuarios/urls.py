from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # 1º ROTA, 2º VIEW RESPONSÁVEL, 3º Nome de Referencia #
    path('', views.index, name='index'),

    # Rota para CADASTRO de usuários #
    path('usuarios/home', views.home, name='home'),

    # ROTA para VISUALIZAÇÃO de usuários RECEM ADICIONADOS #
    path('usuarios/', views.usuarios, name='usuarios'),

    # Rota para DELETAR usuários #
    path('usuarios/deletar', views.remover, name='deletar'),

    # Rota para VISUALIZAR a TABELA COMPLETA #
    path('usuarios/visualizar_usuarios', views.visualizarUsuarios, name='visualizar_usuarios'),

    # Rota para REMOÇÃO de TODOS os usuários CADASTRADOS #
    path('usuarios/usuarios', views.excluir_usuarios, name='excluir_usuarios'),

    # Rota para REMOVER usuário por ID #
    path('usuarios/excluir-por-id', views.excluir_por_id, name='excluir_por_id'),

    # Rotas para INFORMAR erro de ID inválida #
    path('usuarios/erro_ao_deletar', views.excluir_por_id, name='erro_ao_deletar'),
    path('usuarios/erro_deletar', views.erro_deletar, name='erro_deletar'),

    # Rota para ATUALIZAR usuário por ID #
    path('usuarios/atualizar', views.atualizar_por_id, name='atualizar_por_id')
]

