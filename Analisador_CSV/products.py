# data,produto,categoria,quantidade,preco_unitario
# 2024-01-05,Mouse,Periféricos,2,120.50
# 2024-01-06,Teclado,Periféricos,1,230.00
# 2024-01-07,Monitor,Displays,1,1250.00

from datetime import datetime

class Venda:

    categorias = ['periféricos', 'displays', 'gabinetes']

    def __init__(self, data, produto, categoria, quantidade, preco_unitario):

        self.data = data
        self.produto = produto
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario


    #   Setter para data: Tratamento para conversão em datetime
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, valor):

        try:
            valor = datetime.strptime(valor, '%Y-%m-%d')
            self._data = valor
        except ValueError:
            raise ValueError(f'A data {valor} informada não corresponde a uma formatação válida de datetime (%Y-%m-%d)')
        
    

    #   Setter para tratamento de Categoria:

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):

        if not valor.lower() in Venda.categorias:
            raise ValueError(f'{valor} não é uma categoria válida!\n Categorias: {Venda.categorias}')

        self._categoria = valor.lower()


    
    #   Setter para tentar converter quantidade em inteiro

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        try:
            valor = int(valor)
            self._quantidade = valor
        except ValueError:
            raise ValueError('A quantidade não é um numérico inteiro válido')
        
        if valor <= 0:
            raise ValueError('Quantidade não deve ser nula ou negativa!')
        


    #   Setter para converter preco_unitario em float:

    @property
    def preco_unitario(self):
        return self._preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, valor):
        try:
            valor = float(valor)
            self._preco_unitario = valor
        except ValueError:
            raise ValueError('O preco deve ser um número válido!')
        
        if valor <= 0:
            raise ValueError('O preço não deve ser nulo ou negativo!')
        


    #   Factory Method para retornar instância (utilizado no main)

    @classmethod
    def criar_instancia(cls, data, produto, categoria, quantidade, preco_unitario):

        return cls(data, produto, categoria, quantidade, preco_unitario)



    #   Função para exibir faturamento total:
    @staticmethod
    def faturamento(lista):
        return sum(lista)
    

    #   Método para listar informações da venda:
    def listar_venda(self):
        return f'''
    Categoria: {self.categoria}
    Produto: {self.produto}
    Quantidade: {self.quantidade}
    Preco: {self.preco_unitario}
'''

        


