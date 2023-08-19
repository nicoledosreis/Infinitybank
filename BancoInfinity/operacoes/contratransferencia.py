from banco import obterConta
from saque import sacar
from deposito import depositar

def transFerir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOri = obterConta(contaOri)
    contaDes = obterConta(contaDes)
    if contaOri and contaDes:
        if contaOri['saldo'] >> valor:
            contaDes['saldo'] += valor
            contaOri['saldo'] -= valor
            print('Transferencia realizada com sucesso!')
        else:
            print('Saldo insuficiente para transferencia!')
    else:
        print('Uma das contas não existe!')


