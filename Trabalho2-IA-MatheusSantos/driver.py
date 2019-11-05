#Aluno: Matheus Barbosa Santos
#Matricula: 170053016

import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal, contexts, pattern

# Compila e carrega os aquivos .krb em algum diretorio em que esta (recursivamente).
engine = knowledge_engine.engine(__file__)

def general(lista):

    engine.reset()      

    start_time = time.time()
    engine.activate('bc_regras')      
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    febre, dia_febre, dia_manchas, dorMuscular, dorArticulacao, intesiDorArtic, edema, conjuntivite, dorCabeca, coceira, hipertrofia, discrasia, acometimento, neonato = lista
    #hipertrofia, discrasia, acometimento, neonato = lista
    
    args = {}

    if febre: args['febre'] = febre
    if dia_febre: args['dia_febre'] = dia_febre
    if dia_manchas: args['dia_manchas'] = dia_manchas
    if dorMuscular: args['dorMuscular'] = dorMuscular
    if dorArticulacao: args['dorArticulacao'] = dorArticulacao
    if intesiDorArtic: args['intesiDorArtic'] = intesiDorArtic
    if edema: args['edema'] = edema
    if conjuntivite: args['conjuntivite'] = conjuntivite
    if dorCabeca: args['dorCabeca'] = dorCabeca
    if coceira: args['coceira'] = coceira
    if hipertrofia: args['hipertrofia'] = hipertrofia
    if discrasia: args['discrasia'] = discrasia
    if acometimento: args['acometimento'] = acometimento
    if neonato: args['neonato'] = neonato
    #if doenca: args['doenca'] = doenca
    try:
        with engine.prove_goal(
               'bc_regras.diagnostico_resultado ($febre, $dia_febre, $dia_manchas, $dorMuscular, $dorArticulacao, $intesiDorArtic, $edema, $conjuntivite, $dorCabeca, $coceira, $hipertrofia, $discrasia, $acometimento, $neonato, $doenca)',
                #'bc_regras.diagnostico_4 ($hipertrofia, $discrasia, $acometimento, $neonato, $doenca)',
               **args
        ) as gen:
            for vars, plan in gen:
                print("Provavelmente é %s" % vars['doenca'])
    except Exception:

        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print('\n done')

import types

def make_pattern(x):
    if isinstance(x, str):
        if x[0] == '$': return contexts.variable(x[1:])
        return pattern.pattern_literal(x)
    if isinstance(x, (tuple, list)):
        return pattern.pattern_tuple(tuple(make_pattern(element)
                                             for element in x))
    return pattern.pattern_literal(x)
