#!/usr/bin/env python3

import sys

indent = '    '
indent_level = 0

def iprint(string, end='\n'):
    print('\n'.join((indent * indent_level) + line for line in string.split('\n')), end=end)

try:
    n = int(sys.argv[1])
except:
    print('Usage: {} count'.format(sys.argv[0]))
    exit(1)

iprint('''
#include <stdio.h>

int main() {'''.strip())

indent_level += 1

iprint('int ', end='')
for i in range(1, n + 1):
    print('v_{}, '.format(i), end='')
print('v_tmp;')

iprint(r'fprintf(stderr, "Enter {} values to sort:\n");'.format(n))

for i in range(1, n + 1):
    iprint('scanf(" %d", &v_{});'.format(i))

for unsorted_n in range(n, 0, -1):
    for i in range(1, unsorted_n):
        iprint('if (v_{} > v_{}) {{'.format(i, i + 1))
        indent_level += 1
        iprint('v_tmp = v_{};'.format(i))
        iprint('v_{} = v_{};'.format(i, i + 1))
        iprint('v_{} = v_tmp;'.format(i + 1))
        indent_level -= 1
        iprint('}')

iprint(r'fprintf(stderr, "Result:\n");')

for i in range(1, n + 1):
    iprint(r'printf("%d\n", v_{});'.format(i))

iprint('return 0;')

indent_level -= 1

iprint('}')
iprint('/* https://github.com/hckr/useless-crap/blob/master/verbose-sort/gen.py */')
