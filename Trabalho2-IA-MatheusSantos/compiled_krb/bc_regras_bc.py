# bc_regras_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def diagnostico_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('doenca', 'febre', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_regras.diagnostico_1: got unexpected plan from when clause 1"
            with engine.prove('doenca', 'manchas', context,
                              (rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_regras.diagnostico_1: got unexpected plan from when clause 2"
                with engine.prove('doenca', 'dor_muscular', context,
                                  (rule.pattern(5),
                                   rule.pattern(6),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_regras.diagnostico_1: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(7).match_data(context, context,
                            def_doenca(context.lookup_data('doenca1'), context.lookup_data('doenca2'), context.lookup_data('doenca3'))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diagnostico_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('doenca', 'dor_articulacao', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_regras.diagnostico_2: got unexpected plan from when clause 1"
            with engine.prove('doenca', 'intensidade_dor_artic', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_regras.diagnostico_2: got unexpected plan from when clause 2"
                with engine.prove('doenca', 'edema', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_regras.diagnostico_2: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(6).match_data(context, context,
                            def_doenca(context.lookup_data('doenca4'), context.lookup_data('doenca5'), context.lookup_data('doenca6'))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diagnostico_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('doenca', 'conjuntivite', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_regras.diagnostico_3: got unexpected plan from when clause 1"
            with engine.prove('doenca', 'dor_cabeca', context,
                              (rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_regras.diagnostico_3: got unexpected plan from when clause 2"
                with engine.prove('doenca', 'coceira', context,
                                  (rule.pattern(5),
                                   rule.pattern(6),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_regras.diagnostico_3: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(7).match_data(context, context,
                            def_doenca(context.lookup_data('doenca7'), context.lookup_data('doenca8'), context.lookup_data('doenca9'))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diagnostico_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('doenca', 'hipertrofia', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_regras.diagnostico_4: got unexpected plan from when clause 1"
            with engine.prove('doenca', 'discrasia', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_regras.diagnostico_4: got unexpected plan from when clause 2"
                with engine.prove('doenca', 'acometimento', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_regras.diagnostico_4: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(8).match_data(context, context,
                            def_doenca(context.lookup_data('doenca10'), context.lookup_data('doenca11'), context.lookup_data('doenca12'))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def resulta_diagnostico(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'diagnostico_1', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_regras.resulta_diagnostico: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'diagnostico_2', context,
                              (rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(7),
                               rule.pattern(8),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_regras.resulta_diagnostico: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'diagnostico_3', context,
                                  (rule.pattern(9),
                                   rule.pattern(10),
                                   rule.pattern(11),
                                   rule.pattern(12),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_regras.resulta_diagnostico: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'diagnostico_4', context,
                                      (rule.pattern(13),
                                       rule.pattern(14),
                                       rule.pattern(15),
                                       rule.pattern(16),
                                       rule.pattern(17),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_regras.resulta_diagnostico: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(18).match_data(context, context,
                                def_doenca2(context.lookup_data('doenca51'), context.lookup_data('doenca52'), context.lookup_data('doenca53'), context.lookup_data('doenca54'))):
                          context.end_save_all_undo()
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_regras')
  
  bc_rule.bc_rule('diagnostico_1', This_rule_base, 'diagnostico_1',
                  diagnostico_1, None,
                  (contexts.variable('febre'),
                   contexts.variable('dia_febre'),
                   contexts.variable('dia_manchas'),
                   contexts.variable('dorMuscular'),
                   contexts.variable('doenca'),),
                  (),
                  (contexts.variable('febre'),
                   contexts.variable('dia_febre'),
                   contexts.variable('doenca1'),
                   contexts.variable('dia_manchas'),
                   contexts.variable('doenca2'),
                   contexts.variable('dorMuscular'),
                   contexts.variable('doenca3'),
                   contexts.variable('doenca'),))
  
  bc_rule.bc_rule('diagnostico_2', This_rule_base, 'diagnostico_2',
                  diagnostico_2, None,
                  (contexts.variable('dorArticulacao'),
                   contexts.variable('intesiDorArtic'),
                   contexts.variable('edema'),
                   contexts.variable('doenca'),),
                  (),
                  (contexts.variable('dorArticulacao'),
                   contexts.variable('doenca4'),
                   contexts.variable('intesiDorArtic'),
                   contexts.variable('doenca5'),
                   contexts.variable('edema'),
                   contexts.variable('doenca6'),
                   contexts.variable('doenca'),))
  
  bc_rule.bc_rule('diagnostico_3', This_rule_base, 'diagnostico_3',
                  diagnostico_3, None,
                  (contexts.variable('conjuntivite'),
                   contexts.variable('dorCabeca'),
                   contexts.variable('coceira'),
                   contexts.variable('doenca'),),
                  (),
                  (contexts.variable('conjuntivite'),
                   contexts.variable('probabilidade'),
                   contexts.variable('doenca7'),
                   contexts.variable('dorCabeca'),
                   contexts.variable('doenca8'),
                   contexts.variable('coceira'),
                   contexts.variable('doenca9'),
                   contexts.variable('doenca'),))
  
  bc_rule.bc_rule('diagnostico_4', This_rule_base, 'diagnostico_4',
                  diagnostico_4, None,
                  (contexts.variable('hipertrofia'),
                   contexts.variable('discrasia'),
                   contexts.variable('acometimento'),
                   contexts.variable('neonato'),
                   contexts.variable('doenca'),),
                  (),
                  (contexts.variable('hipertrofia'),
                   contexts.variable('doenca10'),
                   contexts.variable('discrasia'),
                   contexts.variable('doenca11'),
                   contexts.variable('acometimento'),
                   contexts.variable('frequencia'),
                   contexts.variable('neonato'),
                   contexts.variable('doenca12'),
                   contexts.variable('doenca'),))
  
  bc_rule.bc_rule('resulta_diagnostico', This_rule_base, 'diagnostico_resultado',
                  resulta_diagnostico, None,
                  (contexts.variable('febre'),
                   contexts.variable('dia_febre'),
                   contexts.variable('dia_manchas'),
                   contexts.variable('dorMuscular'),
                   contexts.variable('dorArticulacao'),
                   contexts.variable('intesiDorArtic'),
                   contexts.variable('edema'),
                   contexts.variable('conjuntivite'),
                   contexts.variable('dorCabeca'),
                   contexts.variable('coceira'),
                   contexts.variable('hipertrofia'),
                   contexts.variable('discrasia'),
                   contexts.variable('acometimento'),
                   contexts.variable('neonato'),
                   contexts.variable('doenca'),),
                  (),
                  (contexts.variable('febre'),
                   contexts.variable('dia_febre'),
                   contexts.variable('dia_manchas'),
                   contexts.variable('dorMuscular'),
                   contexts.variable('doenca51'),
                   contexts.variable('dorArticulacao'),
                   contexts.variable('intesiDorArtic'),
                   contexts.variable('edema'),
                   contexts.variable('doenca52'),
                   contexts.variable('conjuntivite'),
                   contexts.variable('dorCabeca'),
                   contexts.variable('coceira'),
                   contexts.variable('doenca53'),
                   contexts.variable('hipertrofia'),
                   contexts.variable('discrasia'),
                   contexts.variable('acometimento'),
                   contexts.variable('neonato'),
                   contexts.variable('doenca54'),
                   contexts.variable('doenca'),))

def def_doenca(doenca1, doenca2, doenca3):
    if doenca1 == doenca2 and doenca2 == doenca3: return  doenca1 
    if doenca1 == doenca2: return  doenca1 
    if doenca1 == doenca3: return  doenca1
    if doenca2 == doenca3: return doenca2
def def_doenca2(doenca1, doenca2, doenca3, doenca4):
    if doenca1 == doenca2 and doenca2 == doenca3 and doenca3 == doenca4: return  doenca1 
    if doenca1 == doenca2 and doenca2 == doenca3: return  doenca1
    if doenca1 == doenca2 and doenca2 == doenca4: return  doenca1
    if doenca1 == doenca4 and doenca4 == doenca3: return  doenca1
    if doenca4 == doenca2 and doenca2 == doenca3: return  doenca1

Krb_filename = '..\\bc_regras.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 27), (4, 4)),
    ((28, 34), (5, 5)),
    ((35, 41), (6, 6)),
    ((44, 44), (7, 7)),
    ((60, 64), (10, 10)),
    ((66, 72), (12, 12)),
    ((73, 79), (13, 13)),
    ((80, 86), (14, 14)),
    ((89, 89), (15, 15)),
    ((105, 109), (19, 19)),
    ((111, 118), (21, 21)),
    ((119, 125), (22, 22)),
    ((126, 132), (23, 23)),
    ((135, 135), (24, 24)),
    ((151, 155), (27, 27)),
    ((157, 163), (29, 29)),
    ((164, 170), (30, 30)),
    ((171, 179), (31, 31)),
    ((182, 182), (32, 32)),
    ((198, 202), (35, 35)),
    ((204, 213), (37, 37)),
    ((214, 222), (38, 38)),
    ((223, 231), (39, 39)),
    ((232, 241), (40, 40)),
    ((244, 244), (41, 41)),
)
