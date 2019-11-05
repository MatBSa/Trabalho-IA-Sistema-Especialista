#Aluno: Matheus Barbosa Santos
#Matricula: 170053016

import driver

def define_febre(temperatura):
    if temperatura >= 38: return 'alta'
    if temperatura <= 36.5: return 'sem'
    if 36.5 < temperatura < 38: return 'sub_febril'


def verifica_acima_4(dia):
    if dia > 5:
        dia = 10
        return dia
    if dia <= 5: return dia

def informaSintoma():
    
    temperatura = float(input('Informe a temperatura corporal:\n'))
    febre = define_febre(temperatura)

    dia_febre = int(input('Informe o dia em que começou a febre(se não teve febre, coloque dia = 0):\n'))
    
    dia_manchas = int(input('Informe o dia em que comecou a aparecer manchas na pele:\n'))
    dia_manchas = verifica_acima_4(dia_manchas)
    
    dorMuscular = int(input('Informe a frequencia de dor muscular(de 1 a 3):\n'))
    
    dorArticulacao = int(input('Informe a frequencia de dor na articulacao(de 1 a 3):\n'))
    
    intesiDorArtic = input('Informe a intensidade da dor na articulacao(leve/moderada/intensa):\n')
    
    edema = input('Informe a intensidade do edema da articulacao(nao/leve/moderada/intensa):\n')
    
    conjuntivite = input('Possui conjuntivite(s/n):\n')
    
    dorCabeca = int(input('Informe a intensidade da dor de cabeca(de 1 a 3):\n'))
    
    coceira = input('Informe a intensidade da coceira(leve/moderada/intensa):\n')
    
    hipertrofia = input('Informe a intensidade da hipertrofia ganglionar(leve/moderada/intensa):\n')
    
    discrasia = input('Informe se há e a intensidade da dicrasia hemorragica(ausente/leve/moderada):\n')
    
    acometimento = input('Informe se possui acometimento neurologico(s/n):\n')

    neonato = input('Informe se o paciente é neonato paciente(s/n):\n')

    lista = [febre, dia_febre, dia_manchas, dorMuscular, dorArticulacao, intesiDorArtic, edema, 
                conjuntivite, dorCabeca, coceira, hipertrofia, discrasia, acometimento, neonato]

    #lista = [hipertrofia, discrasia, acometimento, neonato]
    return lista

def main():

    lista = informaSintoma() 

    driver.general(lista)

    
    
