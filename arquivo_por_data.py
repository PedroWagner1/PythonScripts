# Crie um script que:

# Percorra recursivamente um diretório usando os.walk
# Para cada arquivo:


# Obtenha a data de última modificação via os.stat
# Converta o timestamp em datetime
# Compare com a data atual
# Liste apenas arquivos modificados nos últimos X dias


# Exiba:
# Nome do arquivo
# Caminho completo
# Data formatada (strftime) no padrão brasileiro

# 📌 Extra opcional: permita definir o valor de X via sys.argv.



import sys
import os
from datetime import datetime


if len(sys.argv) <= 2:
    print(f'\nUsage: {os.path.basename(__file__)} (days) (path) \nExample: {os.path.basename(__file__)} 21 /home/user\n')
    sys.exit()



#   Verifica se days é um número convertível para numérico:

try:
    days = int(sys.argv[1])
except ValueError:
    raise ValueError('days must be an integer value')


#   Verifica se path existe no S.O

if not os.path.exists(sys.argv[-1]):
    raise ValueError('the path entered does not exist in the system.')

#   Verifica se path é um diretório
if not os.path.isdir(sys.argv[-1]):
    raise ValueError('the path entered does not a directory')



path = os.path.join(sys.argv[-1])
days = int(sys.argv[-2])
main_files = {}

for root, dirs, files in os.walk(path):
    
    for x in files:
        
        fpath = root + '/' + x if os.name == 'posix' else root + '\\' + x

        try:

            stat = os.stat(fpath)
        except FileNotFoundError:
            ...

        modification_time = stat.st_mtime

        modification_date = datetime.fromtimestamp(modification_time)

        effective = datetime.now() - modification_date
       
        #   Condição para descartar arquivos modificados há mais de x dias:

        if effective.days > days:
            continue
        else:
            main_files[x] = {'path': fpath, 'date': modification_date.strftime('%d/%m/%Y %H:%M:%S') }


for x in main_files.keys():
  
  print(f'\nArquivo: {x}\nData Modificação: {main_files[x]['date']}\nCaminho: {main_files[x]['path']}\n')