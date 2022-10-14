def pizza(ingredientes, lista_escolha):
    """ Dá o preço da pizza
    
    :param ingredientes: Dicionario em que a chave é o tipo e o valor é um dicionario com as chaves sendo os ingredientes e os valores sendo os respectivos preços
    :type ingredientes: dict{str:dict{str:float}}
    :param lista_escolhas: listas dos inredienets desejados
    :type lista_ingredientes: list
    
    :return: valor
    :rtype: float
    
    >>> ingredientes = {"massa":{"fina":3.4, "grossa":5.6}, "queijo":{"cheddar":5, "prato":3}, "cobertura":{"frango":4, "presunto":10}}
    >>> pizza(ingredientes, ["frango", "fina", "prato"])
    31.0

    >>> pizza(ingredientes, ["pepperoni", "prato", "grossa"])
    Os ingredientes não estão disponíveis!
    0
    """
    if not isinstance(ingredientes, dict):
        print("Dicionário de ingredientes em formato inválido!")
    if not isinstance(lista_escolha, list):
        print("Dicionário de escolhas em formato inválido!")

    ingredientes_valores = map(lambda tipo: list(tipo.items()), ingredientes.values())
    ingredientes_valores = [ingrediente for lista_tipo in ingredientes_valores for ingrediente in lista_tipo]
    ingredientes_nomes = [ingredientes[0] for ingredientes in ingredientes_valores]
    valor_pizza = 0

    if set(lista_escolha).issubset(ingredientes_nomes):
        for ingrediente in ingredientes_valores:
            if ingrediente[0] in ingredientes_nomes:
                valor_pizza += ingrediente[1]
    else:
        print("Os ingredientes não estão disponíveis!")
    return valor_pizza

def cadastrar(tipo, custo, nome, ingredientes):
    """Cadatra um novo ingrediente de determinado tipo na lista de ingredientes
    
    :param tipo: Tipo de ingrediente, pode ser 'molho', 'queijo', 'cobertura', 'massa'
    :type tipo: str
    :param custo: custo 
    :type custo: float
    :param nome: Nome do ingrediente
    :type nome: str
    :param ingredientes: Dicionario em que a chave é o tipo e o valor é um dicionario com as chaves sendo os ingredientes e os valores sendo os respectivos preços
    :type ingredientes: dict{str:dict{str:float}}
    
    :return: Retorna o dicionario com o novo item 
    :rtype: dict{str:dict{str:float}}
    
    >>> ingredientes = {'massa': {}, 'molhos': {'tomate': 4.0, 'branco': 3.0},'queijo': {'mozzarela': 6.0}, 'cobertura': {'calabresa': 8.0}}
    >>> cadastrar('massa', 9.9, 'fina', ingredientes)
    {'massa': {'fina': 9.9}, 'molhos': {'tomate': 4.0, 'branco': 3.0}, 'queijo': {'mozzarela': 6.0}, 'cobertura': {'calabresa': 8.0}}
    
    
    """
    ingredientes[tipo][nome] = float(custo)
    return ingredientes

def remover(tipo, custo, nome, ingredientes):
    """Remove um ingrediente da lista de ingredientes
    
    :param tipo: Tipo de ingrediente, pode ser 'molho', 'queijo', 'cobertura', 'massa'
    :type tipo: str
    :param custo: custo 
    :type custo: float
    :param nome: Nome do ingrediente
    :type nome: str
    :param ingredientes: Dicionario em que a chave é o tipo e o valor é um dicionario com as chaves sendo os ingredientes e os valores sendo os respectivos preços
    :type ingredientes: dict{str:dict{str:float}}
    
    :return: Retorna o dicionario sem o item inserido
    :rtype: dict{str:dict{str:float}}
    
    >>> ingredientes = {'massa': {'fina': 9.9}, 'molhos': {'tomate': 4.0, 'branco': 3.0},'queijo': {'mozzarela': 6.0}, 'cobertura': {'calabresa': 8.0}}
    >>> remover('massa', 0, 'fina', ingredientes)
    {'massa': {}, 'molhos': {'tomate': 4.0, 'branco': 3.0}, 'queijo': {'mozzarela': 6.0}, 'cobertura': {'calabresa': 8.0}}
    
    """
    ingredientes[tipo].pop(nome)
    return ingredientes


def listar(tipo ='todos', ingredientes):
    """Retorna toda lista de ingredientes disponiveis
    
    :param tipo: Tipo de ingrediente, pode ser 'molho', 'queijo', 'cobertura', 'massa' ou por default 'todos'
    :type tipo: str
    :param ingredientes: Dicionario em que a chave é o tipo e o valor é um dicionario com as chaves sendo os ingredientes e os valores sendo os respectivos preços
    :type ingredientes: dict{str:dict{str:float}}
    
    :return: Retorna o dicionario sem o item inserido
    :rtype: dict{str:dict{str:float}}
    
    """
    if tipo == 'todos':
        return ingredientes
    else:
        return ingredientes[tipo]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
