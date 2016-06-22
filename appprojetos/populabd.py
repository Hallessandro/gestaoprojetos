from django.db import transaction,IntegrityError
from appprojetos.models import *

me01 = Membros(nome="Bran Stark", matricula="123")
me02 = Membros(nome="Arya Stark", matricula="321")
me03 = Membros(nome="Sansa Stark", matricula="231")
me04 = Membros(nome="Hodor", matricula="122")
me01.save()
me02.save()
me03.save()
me04.save()

pf01 = Professor(nome="Corvo de 3 olhos", matricula=456, area_atuacao="Magias e afins")
pf02 = Professor(nome="Lorde Comandande Jon Snow", matricula=212, area_atuacao="Combate e governo")
pf03 = Professor(nome="Jaqen H'gha", matricula=666, area_atuacao="Ensinar Arya Stark a ser ninguém")
pf01.save()
pf02.save()
pf03.save()

nv01 = Nv_desenvolvimento(estagio="C", descricao="Adicionar alguns dados no Banco", dt_registro="2016-6-12")
nv01.save()

at01 = Atividade(descricao="Fazendo consultas", dt_inicio="2016-1-1", dt_termino="2016-6-1",
                 custo=20, dsvol=nv01)
at01.save()

pj01 = Projeto_pesquisa(titulo="Valar Morghulis", dt_inicio="2016-6-8", dt_termino="2016-6-12",
                        justificativa="A garota tem muitos inimigos",
                        metodologia="Tecnicas aprendidas na casa do preto e branco",
                        resultados_esperados="Eliminar todos os nomes da lista",
                        atividade=at01)
pj01.save()
pj01.membros.add(me02,pf03)

pj02 = Projeto_pesquisa(titulo="Defender a muralha", dt_inicio="2016-6-8", dt_termino="2016-6-12",
                        justificativa="O inverno está chegando",
                        metodologia="Lutar com tudo que tivermos",
                        resultados_esperados="Derrotar os outros",
                        atividade=at01)
pj02.save()
pj02.membros.add(me03, pf02)

pj02 = Projeto_pesquisa(titulo="Aprender a ver o passado, presente e futuro", dt_inicio="2016-6-8", dt_termino="2016-6-12",
                        justificativa="O inverno está chegando",
                        metodologia="Aulas teóricas e práticas com o Corvo de 3 olhos",
                        resultados_esperados="Preparar o Bran para enfrentar o Rei da Noite",
                        atividade=at01)
pj02.save()
pj02.membros.add(me01, pf01, me04)