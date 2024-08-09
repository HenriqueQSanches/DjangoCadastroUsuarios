from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')


def index(request):
    return render(request, 'usuarios/index.html')


def remover(request):
    return render(request, 'usuarios/deletar.html')


def erro_deletar(request):

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/erro_deletar.html', usuarios)



def visualizarUsuarios(request):

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/visualizar_usuarios.html', usuarios)

def usuarios(request):

    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios);
    

def excluir_usuarios(request):
    if request.method == 'POST':

        usuarios = {
            'usuarios': Usuario.objects.all().delete()
        }

        return render(request, 'usuarios/usuarios_deletados.html', usuarios);


def excluir_por_id(request):

    usuarios = {
        'usuario': Usuario.objects.all() 
    }

    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
            usuario.delete()
            return redirect('visualizar_usuarios')
        except Usuario.DoesNotExist:

            usuarios = {
                'usuarios': Usuario.objects.all()
            }

            return render(request, 'usuarios/erro_deletar.html', usuarios)
        except ValidationError:

            usuarios = {
                'usuarios': Usuario.objects.all()
            }

            return render(request, 'usuarios/erro_deletar.html', usuarios)
        except Exception as e:

            usuarios = {
                'usuarios': Usuario.objects.all()
            }

            return render(request, 'usuarios/erro_deletar.html', usuarios)


def erro_ao_deletar(request):

    return render(request, 'usuarios/erro_deletar.html', usuarios)


def atualizar_por_id(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
            usuario.nome = nome
            usuario.idade = idade
            usuario.save()
            mensagem = "Usuário atualizado com sucesso."
            sucesso = True
        except Usuario.DoesNotExist:
            mensagem = "Usuário não encontrado."
            sucesso = False
        except ValidationError:
            mensagem = "Erro de validação. Verifique os dados inseridos."
            sucesso = False
        except Exception as e:
            mensagem = f"Ocorreu um erro: {str(e)}"
            sucesso = False

    else:
        mensagem = None
        sucesso = None

    usuarios = {
        'usuarios': Usuario.objects.all(),
        'mensagem': mensagem,
        'sucesso': sucesso
    }

    return render(request, 'usuarios/atualizar.html', usuarios)
