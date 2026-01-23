# Crie um programa que:


# Receba um diretório via argumento de linha de comando
# Percorra todos os arquivos recursivamente
# Separe os arquivos em pastas com base:

# Na extensão (.txt, .jpg, .pdf, etc.)
# Crie as pastas automaticamente se não existirem


# Mova os arquivos para cada pasta


import sys
import os
import shutil

#   Output padrão para falta de argumentos:

if len(sys.argv) <= 1:
    print(f'\nUsage: {os.path.basename(__file__)} /path/to/directory\n')
    sys.exit()


#   Verifica se argumento passado é um diretório válido

if not os.path.isdir(sys.argv[-1]):
    raise ValueError('O último argumento passado não é um diretório válido')


#   Se o S.O for ms-dos (windows) adiciona \ ao final do caminho caso contrário adiciona / (Linux / MacOS)
path = sys.argv[-1] + '/' if os.name == 'posix' else sys.argv[-1] + '\\'

dirs = ['text', 'images', 'pdf']


for x in dirs:
    #   Cria as pasas images, pdf e text caso não existam
    if not os.path.exists(path + x):    
        try:
            os.mkdir(path + x)
        except FileNotFoundError:
            raise ValueError('Diretório não encontrado')
        
    
arquivos = os.listdir(path)
arquivos_c = []

#   Itera nos arquivos de path para extrair os arquivos com as extensões
for x in arquivos:
    if not os.path.isdir(path + x):
        arquivos_c.append(x)




for x in arquivos_c:

    if x.endswith('.txt'):
        print(f'arquivo {x} movido para {path + 'text'}')
        shutil.move(path + x, path + 'text')

    if x.endswith('.jpg'):
        print(f'arquivo {x} movido para {path + 'images'}')
        shutil.move(path + x, path + 'images')

    if x.endswith('.pdf'):
        print(f'arquivo {x} movido para {path + 'pdf'}')
        shutil.move(path + x, path + 'pdf')

