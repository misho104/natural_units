import unittest
import os
import re
import pathlib
import shutil
import subprocess
import sys
import math

PROGRAM_CANDIDATES = [os.environ.get('UNITS_BIN'), 'gunits', 'units']


def find_program():
    for c in PROGRAM_CANDIDATES:
        if c:
            program = shutil.which(c)
            if program:
                break
    if not program:
        raise RuntimeError('Cannot find units program.')

    proc = subprocess.Popen([program, '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    if re.search(r'\AGNU Units version 2\.\d+', out.decode()):
        return program
    elif 'illegal option' in err.decode():
        raise RuntimeError('Found BSD Units; GNU Units is required.')
    else:
        raise RuntimeError(
            'Version check failed; GNU units version >= 2.00 is required.\n\n'
            f'# STDOUT\n{out.decode()}\n'
            f'# STDERR\n{err.decode()}\n')


class TestNaturalUnits(unittest.TestCase):
    PROGRAM = ''
    DEFINITION = ''

    def run_units(self, from_exp, to_exp):
        self.proc = subprocess.Popen([self.PROGRAM, '-t', '-d15', '-f', self.DEFINITION,
                                      from_exp,
                                      to_exp or '1'],
                                     stdout=subprocess.PIPE)
        result_str = self.proc.communicate()[0].decode()
        return float(result_str)

    def c(self, from_exp, to_exp, expected, d=None):
        # d for digits
        digits = d or self.digits
        actual = self.run_units(from_exp, to_exp)
        self.assertAlmostEqual(expected, actual, places=digits - int(math.log10(expected)) - 1)

    def setUp(self):
        if not self.PROGRAM or not self.DEFINITION:
            raise RuntimeError('PROGRAM/DEFINITION is not specified.')
        self.digits = 7

    def test_exact_values(self):
        self.digits = 15
        self.c('c',        '',    1)
        self.c('h',        '2pi', 1)
        self.c('hbar',     '',    1)
        self.c('kB',       '',    1)
        self.c('mu0',      '',    1)
        self.c('epsilon0', '',    1)

    def test_peskin_appendix(self):
        self.digits = 4
        self.c('1GeV',     'g',     1.783e-24)
        self.c('1/GeV',    'fm',    0.1973)
        self.c('1/GeV^2',  'mbarn', 0.3894)
        self.c('1V e/m',   'GeV^2', 1.973e-25)
        self.c('1tesla e', 'GeV^2', 5.916e-17)

    def test_universal_constants(self):
        # https://physics.nist.gov/cgi-bin/cuu/Category?view=pdf&Universal.x=124&Universal.y=14
        self.c('c',        'm/s',        299792458, d=8)
        self.c('mu0',      'N/A^2',      12.566370614e-7, d=9)
        self.c('epsilon0', 'F/m',        8.854187817e-12, d=8)
        self.c('G_N',      'm^3/kg/s^2', 6.67408e-11, d=5)
        self.c('G_N',      '/GeV^2',     6.70861e-39, d=5)
        self.c('h',        'J s',        6.626070040e-34, d=8)
        self.c('hbar',     'eV s',       6.582119514e-16, d=8)
        self.c('M_pl',     'kg',         2.176407e-8, d=5)
        self.c('M_pl',     'GeV',        1.220910e19, d=5)
        self.c('M_pl',     'K',          1.416808e32, d=5)
        self.c('1/M_pl',   'm',          1.616229e-35, d=5)
        self.c('1/M_pl',   's',          5.39116e-44, d=5)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} PATH_TO_UNITS_FILE', file=sys.stderr)
        exit(1)
    try:
        program = find_program()
    except RuntimeError as e:
        print(f'RuntimeError: {e}', file=sys.stderr)
        exit(1)

    definition = pathlib.Path(sys.argv[1])
    if not definition or not definition.exists():
        print(f'{definition} not found.', file=sys.stderr)
        exit(1)
    TestNaturalUnits.PROGRAM = program
    TestNaturalUnits.DEFINITION = str(definition)
    unittest.main(argv=['TestNaturalUnits'])
