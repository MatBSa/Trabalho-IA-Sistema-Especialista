# regras_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def febre(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'get_celsius', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "regras.febre: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'get_celsius', context,
                              (rule.pattern(0),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "regras.febre: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('regras')
  
  bc_rule.bc_rule('febre', This_rule_base, 'febre',
                  febre, None,
                  (contexts.variable('temperatura'),
                   contexts.variable('dia'),),
                  (),
                  (contexts.variable('fahrenheit'),
                   contexts.variable('unit'),
                   contexts.variable('celsius'),))

def to_celsius(f):
    if temperatura < 38 and 4 <= dia <= 7: return 'dengue'
    if temperatura < 38 and 1 <= dia <= 2: return 'zika'
    if temperatura < 38 and 2 <= dia <= 3: return 'chikungunya'

Krb_filename = '..\\regras.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 27), (4, 4)),
    ((28, 35), (5, 5)),
)
