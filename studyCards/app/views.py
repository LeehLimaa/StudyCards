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
        novo_conteudo = Conteudo()
        novo_conteudo.nome_conteudo = request.POST.get('nome_conteudo')
        novo_conteudo.descricao_conteudo = request.POST.get('descricao_conteudo')

        try:
            disciplina = Disciplina.objects.get(pk=request.POST.get('disciplina'))
            novo_conteudo.disciplina = disciplina
            novo_conteudo.save()
        except Disciplina.DoesNotExist:
            print("Disciplina não encontrada!")
        except Exception as e:
            print("Erro de integridade:", e)

    conteudos = {
        'conteudos': Conteudo.objects.all(),
        'disciplina': Disciplina.objects.all()
    }
    
    return render(request, 'conteudo/conteudo.html', conteudos)

def cartao(request):
    if request.POST:
        novo_cartao = Cartao()
        novo_cartao.termo = request.POST.get('termo')
        novo_cartao.definicao = request.POST.get('definicao')

        try:
            conteudo = Conteudo.objects.get(pk=request.POST.get('conteudo'))
            novo_cartao.conteudo = conteudo
            novo_cartao.save()
        except Conteudo.DoesNotExist:
            print("conteudo não encontrada!")
        except Exception as e:
            print("Erro de integridade:", e)

    cartaos = {
        'cartaos': Cartao.objects.all(),
        'conteudo': Conteudo.objects.all()
    }
    
    return render(request, 'cartao/cartao.html', cartaos)

def consulta(request):
    consultas = {
         'consultas':Cartao.objects.all()
        }

    return render(request,'consulta/consulta.html', consultas)

def consulta(request):
    cartoes = Cartao.objects.all()
    conteudos = Conteudo.objects.all()
    disciplinas = Disciplina.objects.all()

    cartoes_por_disciplina = {}
    for disciplina in disciplinas:
        nome_disciplina = disciplina.nome_disciplina
        cartoes_por_disciplina[nome_disciplina] = {}

        for conteudo in conteudos.filter(disciplina=disciplina):
            nome_conteudo = conteudo.nome_conteudo
            cartoes_por_disciplina[nome_disciplina][nome_conteudo] = []

        for cartao in cartoes.filter(conteudo__disciplina=disciplina):
            nome_conteudo = cartao.conteudo.nome_conteudo
            cartoes_por_disciplina[nome_disciplina][nome_conteudo].append(cartao)

    context = {
        'cartoes_por_disciplina': cartoes_por_disciplina
    }

    return render(request, 'consulta/consulta.html', context)





