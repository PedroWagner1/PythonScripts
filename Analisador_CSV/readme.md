#   Analisador de Vendas em Arquivo CSV

    Este programa foi escrito para a resolução de um exercício de aprendizagem ativa após minhas aulas a respeito
    da biblioteca csv no curso de Python que estou atualmente realizando (29/01/2026)

    O exercício pede para que se receba um arquivo csv com a estrutura: 
    
    data,produto,categoria,quantidade,preco_unitario

    e converta quantidade, preco unitario e data para seus respectivos valores, exiba o faturamento total e faturamento por categoria

#   Resolução:

    Pela proposta do exercício, achei uma boa oportunidade de aplicar POO, justamente por estarmos tratando de vendas, objeto este semânticamente ideal para se colocar em uma classe, na minha opinião. Para além disto decidi criar um programa agradável ao usuário, que permita que ele insira um arquivo (em caminho dinâmico ou absoluto) e então ele mesmo selecione quais operações realizar.


#   Semântica Obrigatória do Arquivo CSV:

    O programa foi desenvolvido pensando em arquivos CSV's especificamente com a estrutura:

    data,produto,categoria,quantidade,preco_unitario

    Qualquer arquivo CSV fora desta estrutura provavelmente deverá retornar erros.



#   Estrutura:

    O programa é composto por dois arquivos: main.py e products.py


<h2><bold>Main.py</bold></h2>

    O arquivo main.py é o arquivo principal que possui o fluxo efetivo do código, é nele que se roda o fluxo de trabalho do código e as funcionalidades do módulo products. 
    
    Ao iniciar o programa, o usuário se depara com um input referente ao nome do arquivo no qual se deseja consultar. O input do usuário é convertido para um valor Path(), objeto importado de pathlib que preserva compatibilidade de caminhos de diretórios e arquivos para diferentes sistemas operacionais, já executando o método absolute() de Path que armazena o valor absoluto efetivo para aquele arquivo. Decidi referenciar absolute() diretamente para preservar possíveis erros.
    
    
    Ao colocar o nome do arquivo, três verificações são feitas para proteger o fluxo de operação:

    1. utiliza-se os.path.exists() para verificar se o valor colocado no campo do input é reconhecido como um arquivo ou diretório existente no sistema operacional.

    2. (só é executado se passo 1 verificar integridade), utiliza-se os.path.isdir() para verificar se o valor inserido é um diretório. Caso o valor seja um diretório, o programa informará ao usuário o erro e dará um continue no loop, forçando uma nova inicialização.

    3. (só executado se passo 2 verificar integridade) O arquivo path é convertido para uma string diretamente através de str(), utiliza-se o método de string .endswith('.csv') para verificar se o arquivo possui a extensão .csv, caso ele NÃO possua (operador NOT) o sistema informará o erro e executará um continue no loop forçando um novo laço.



    Após as 3 verificações serem feitas, caso todas elas verifiquem integridade, isso significa que nós temos um arquivo válido e existente no sistema operacional com a extensão .csv . A análise de requisitos para a continuação do programa foi feita, agora começando efetivamente a lógica mais funcional do código.


    Utiliza-se um context manager para abrir o Path() do arquivo inserido pelo usuário (file), logo após é adicionado uma estrutura try: except: para tentar a execução de csv.DictReader(file), caso ocorra qualquer erro nesta tentativa, o programa lançará uma exceção exibindo a mensagem deste erro.

    Caso nenhum erro ocorra, isto significa então que nós possuimos um iterável de dicionários 'coluna': 'valor' para cada registro no arquivo CSV.

    Considerando isto, é feito uma estrutura de repetição for neste iterable

    Para cada elemento sendo tratado em cada iteração, nós definimos x: RegistroCSV = x . RegistroCSV é um TypedDict feito exclusivamente pensando na referência das chaves do objeto no IDE.

    Após isto é armazenado cada valor de cada coluna do registro em suas respectivas variáveis, e então é chamada a factory method criar_instancia da classe Vendas do módulo products, passando como argumentos posicionais as variáveis criadas, criando assim um objeto Vendas válido em uma variável, e adicionando o valor desta variável à lista vendas do módulo principal. Com isto nós teremos todos os objetos Vendas para cada registro no arquivo CSV armazenados em uma lista, podendo ser iterada para a execução das operações.

    Após isto é exibido ao usuário que escolha algum comando, os comandos são:

    faturamento , faturamento_categoria , listar_vendas

    Após o input do usuário é feita 4 verificações:


    1. Caso o comando não exista, o programa informa este fato e quebra o loop

    2. Caso o comando for faturamento, o programa então exibe o faturamento total, utilizando o método estático
        faturamento da classe Vendas, passando como argumento uma lista e utilizando list comprehension para considerar x.preco para cada x em vendas (lista de objetos Vendas)

    3.  Caso o comando for faturamento_categoria, o programa então pede um input do usuário e exibe o faturamento com a mesma lógica da verificação 2, porém adicionando um filter ao final do list comprehension que omite x caso x.categoria for diferente do input fornecido pelo usuário.

    4. Caso o comando for listar_vendas, o programa então realiza um for em vendas (lista de objetos Vendas) e 
        executa o método de instância listar_venda() para cada elemento da iteração



<h2> products.py </h2>

    products.py é o módulo que possui toda a lógica de verificação dos valores do CSV fornecido (através de @property e setter's), implementação das lógicas de visualização de pedido, lógica de cálculo de faturamento, conversões de valores do CSV para datetime, float e int. É um arquivo semanticamente sólido e muito bem desenvolvido em design na minha opinião.


#   Resumo

    Mais um programa que eu desenvolvo especificamente para finalizar meu aprendizado ativo diário de Python, espero que os desenvolvedores e entusiastas que possivelmente vejam este código se alegrem, eu demorei aproximadamente cerca de 1h para desenvolvê-lo, pois tive que tirar tudo do zero da minha cabeça na solução, não tive nenhum tipo de direcionamento ou sequer consultei documentação. Apenas realizei a prática do conteúdo estudado no início do dia e do meu conhecimento na linguagem (POO, intermediario, bibliotecas)