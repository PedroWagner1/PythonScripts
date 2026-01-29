# 🧠 Desafio 1 — Analisador de Vendas CSV (≈ 30 min)


# Você recebeu um arquivo vendas.csv com o seguinte formato:

# data,produto,categoria,quantidade,preco_unitario
# 2024-01-05,Mouse,Periféricos,2,120.50
# 2024-01-06,Teclado,Periféricos,1,230.00
# 2024-01-07,Monitor,Displays,1,1250.00

# Tarefas:


# Use Path para localizar o arquivo CSV.
# Leia o arquivo usando csv.DictReader.
# Converta:

# quantidade → int
# preco_unitario → float
# data → datetime.date

# Calcule:

# Faturamento total
# Faturamento por categoria
# Exiba o resultado no terminal de forma organizada.

# Restrições:

# ❌ Não use pandas
# ✅ Use apenas csv, pathlib, datetime

from pathlib import Path
import os
import csv
from typing import TypedDict
import products


class RegistroCSV(TypedDict):

    data: str
    produto: str
    categoria: str
    quantidade: str
    preco_unitario: str




while True:

    vendas = [] #   Lista de objetos Venda (products.py)
    comandos = ['faturamento', 'faturamento_categoria', 'listar_vendas']

    #   Mensagem de exibição inicial + converte entrada para Path
    print('Bem vindo ao analisador de vendas, insira o nome (ou caminho absoluto) do arquivo:\n\n_> ', end='')
    filename = Path(input('')).absolute()


    #   Guard Clause: Pula o Loop caso arquivo não exista

    if not os.path.exists(filename):
        print('\nO arquivo inserido não existe! Tente Novamente!\n')
        continue

        #   Guard Clause: Pula o Loop caso o argumento seja um diretório
    if os.path.isdir(filename):
        print('\nO argumento deve ser um arquivo, não um diretório!\n')
        continue

        #   Guard Clause: Pula o Loop caso o arquivo não possua .csv ao final
    if not str(filename).endswith('.csv'):
        print('\nO arquivo deve possuir uma extensão .csv válida!\n')
        continue



        #   Abertura do arquivo com context manager:

    with open(filename, 'r', encoding='utf8') as file:

        try:
            iterable = csv.DictReader(file)
        except Exception as e:
            raise Exception(f'erro: {e}')

        for x in iterable:


            #   Adicionando cada registro à lista vendas como objetos Venda
            
            x: RegistroCSV = x  #   Define x como TypedDict
            data = x['data']
            produto = x['produto']
            categoria = x['categoria']
            quantidade = x['quantidade']
            preco_unitario = x['preco_unitario']

            #   Cria objeto Venda passando valores de x            
            venda = products.Venda.criar_instancia(data, produto, categoria, quantidade, preco_unitario)

            vendas.append(venda)    #   Adiciona objeto à lista



        print(f'\nArquivo carregado com sucesso, digite algum comando:\nComandos: {comandos} \n_> ', end='')
        comando = input('')

        if comando not in comandos:
            print('\nComando inexistente, fechando o programa')
            break


            #   Exibição do Faturamento:
        if comando == 'faturamento':
            print('\n\nFaturamento: ', products.Venda.faturamento([x.preco_unitario for x in vendas]), '\n')

            #   Exibição do Faturamento por categoria:
        if comando == 'faturamento_categoria':
            cat = input(f'\nDigite o nome da categoria\nCategorias: {products.Venda.categorias}')
            if not cat.lower() in products.Venda.categorias:
                print('Categoria inexistente!')
                break

            print(f'\nFaturamento para {cat}: {products.Venda.faturamento([x.preco_unitario for x in vendas if x.categoria == cat.lower()])}')


        #   Exibição individual das vendas:
        if comando == 'listar_vendas':
            for x in vendas:
                print(x.listar_venda())