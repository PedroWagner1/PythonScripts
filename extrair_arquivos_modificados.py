# Crie um script que:


#   Receba um diretório base (hardcoded ou via sys.argv)
#   Liste apenas arquivos (ignore diretórios)


#    Para cada arquivo:


    # Obtenha a data da última modificação usando os.path.getmtime
    # Converta o timestamp para datetime


# Exiba somente os arquivos modificados nos últimos 7 dias


# Mostre:
# Nome do arquivo
# Data formatada (dd/mm/yyyy HH:MM)


# Ordene a saída do mais recente para o mais antigo


# 📌 Restrições:
# Use os, os.path, datetime
# Não use bibliotecas externas para varrer diretórios


import sys
import os
from datetime import datetime, timedelta


files = []

#   =====   Tratamentos =====

    #   Caso o usuário não tenha passado argumentos na chamada do arquivo
if len(sys.argv) <= 1:    
    print('\n!!!   Missing Arguments   !!!\n\nUsage: extract.py /path/to/directory')
    sys.exit()



if not os.path.exists(sys.argv[1]):     #   Caso o argumento passado após a execução do módulo não for existente no S.O como um path valido:
    raise ValueError('The argument passed is not a valid path!')



#   Lança erro caso o path passado não seja um diretório
try:
    os.listdir(sys.argv[1])
except NotADirectoryError:
    raise NotADirectoryError('The argument passed is not a Directory')


#   Lança erro caso não haja arquivos no diretório
if len(os.listdir(sys.argv[1])) == 0:
    raise ValueError('There are no files in the directory')





#    ===     Código Efetivo:   === 


dir_name = sys.argv[1]
temp_files = os.listdir(sys.argv[1])



for x in temp_files:

    if os.path.isdir(dir_name + x):
        ...
    else:
        
        #   Except serve para tratar links simbólicos
        try:
            timestamp = os.path.getmtime(dir_name + x)
        except FileNotFoundError:
            continue

        date = datetime.fromtimestamp(timestamp)

        mod_time = datetime.now() - date


        #   Se os dias entre o horário atual e a modificação do arquivo for maior ou igual a 7:
        if mod_time.days >= 7:
            continue

        f_date = date.strftime('%d/%m/%Y %H:%M')

        files.append([x, f_date])



ordened_file = sorted(files, key=lambda x: datetime.strptime(x[1], '%d/%m/%Y %H:%M'), reverse=True)


for x in ordened_file:
    
    print(f'\nArquivo: {x[0]}\nData de Modificação: {x[1]}')

