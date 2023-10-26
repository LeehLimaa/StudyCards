from django.shortcuts import render
from . models import*

def disciplina(request):
    if request.POST:
        nova_disciplina = Disciplina()
        nova_disciplina.nome_disciplina = request.POST.get('nome_disciplina')
    try:
        nova_disciplina.save()
    except Exception as e:
        print("Erro de integridade:", e)

    disciplinas = {
        'disciplinas': Disciplina.objects.all()
    }

    return render(request, 'disciplina/disciplina.html', disciplinas)

def conteudo(request):
    if request.POST:
        nova_conteudo = conteudo()
        nova_conteudo.nome_conteudo = request.POST.get('nome_conteudo')
    try:
        disciplina = Disciplina.objects.get(pk=request.POST.get('disciplina'))
        nova_conteudo.disciplina = disciplina
        nova_conteudo.save()
    except Disciplina.DoesNotExist:
        print("Disciplina não encontrada!")
    except Exception as e:
        print("Erro de integridade:", e)

    conteudos = {
        'disciplina': Disciplina.objects.all()
    }
    
    return render(request, 'conteudo/conteudo.html', conteudos)




