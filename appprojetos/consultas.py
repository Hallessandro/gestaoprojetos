from appprojetos.models import *

# a. Listar todos os projetos com seus respectivos membros
for pj in Projeto_pesquisa.objects.all():
    print("Projeto: {0:s} - Membros {1:s}".format(pj.titulo, pj.membros))
    #Não tá funcionando

# b. Listar todas as atividades que tenham sido executadas no mês de maio de 2015
print(Atividade.objects.filter(dt_inicio__month="05"))

# c. Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A
print(Membros.objects.filter(nome__startswith="A"))

# d. Listar o custo total de cada projeto
    print(Projeto_pesquisa.objects.filter(pj.atividade.descricao))