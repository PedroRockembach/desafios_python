from os import system

system("cls")

def notas(*num,sit=True):
    """recebe valores e acha, maior menor e media no retorno

    Args:
        sit (bool, optional): Arguemnto que mostra se media > que 7. Defaults to True.

    Returns:
        _type_: _description_
    """
    
    maior_valor = max(num)
    menor_valor = min(num)
    media = sum(num)/(len(num))
    
    retorno = (
            f'Total de valores = {len(num)}\n'
            f'maior valor = {maior_valor}\n'
            f'menor valor = {menor_valor}\n'
            f'media = {media:.2f}\n'   
            )       
    if sit:
        if media > 7:
            retorno += '\033[32MAPROVADO\033[m'
        else:
            retorno += '\033[31mREPROVADO\033[m'
            
    return retorno
           
teste = notas(5.5, 3.5, 1.5)
print(teste)