# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_regras.krb'):
           [1571105171.1699395, 'bc_regras_bc.py'],
         ('', '', 'doenca.kfb'):
           [1571105171.1819203, 'doenca.fbc'],
         ('', '', 'regras.krb'):
           [1571105171.1899126, 'regras_bc.py'],
        },
        compiler_version)

