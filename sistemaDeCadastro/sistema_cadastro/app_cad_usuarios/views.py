from django.shortcuts import render
from.models import Usuario

# criação das wiews
def home(request):
    return render (request,'usuarios/home.html')

def usuarios(request):
    # Salvamento do preenchimento do formulário html no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir os usuarios já cadastrados em uma nova página

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuarios 

    return render(request, 'usuarios/usuarios.html', usuarios)

