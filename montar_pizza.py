def pizza(ingredientes, lista_escolha):
    """ Dá o preço da pizza
    
    :param ingredientes: Dicionario em que a chave é o tipo e o valor é um dicionario com as chaves sendo os ingredientes e os valores sendo os respectivos preços
    :type ingredientes: dict{str:dict{str:float}}
    :param lista_escolhas: listas dos inredienets desejados
    :type lista_ingredientes: list
    
    :return: valor
    :rtype: float
    """
    pass

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
