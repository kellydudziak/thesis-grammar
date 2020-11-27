from lark import Lark
import fin_stripped, propp_strings, dicts, x
import f_func_test

def load_grammar(file):
    s = str(open(file, 'r').read())
    return Lark(('r"""' + s + '"""'), start='t', cache='false', parser='lalr')

# ? if I store the grammars as load_grammar(file), is that executed each time I call that dict value? Or is the return value stored
grammars = {'moves' : load_grammar('f_moves.txt'), 'funcs' : load_grammar('f_funcs.txt')}
strings = {'propp' : propp_strings.stripped,
           'full' : fin_stripped.full_dict,
           'prepless' : fin_stripped.prepless_dict}

def parse(_print):
    for k,v in strings.items():                 # for each string dict; k = full, prepless, propp, v = the dict of strings
        for k1, v1 in v.items():                # for each string in the dict; k1 = tale number, v1 = string of functions
            for k2, v2 in grammars.items():     # for each grammar; k2 = moves, funcs, v2 = the grammar
                try:
                    p = v2.parse(v1)
                    if _print : print(str(k1) + "\n" + str(p.pretty()))
                    dicts.tales[k][k2]['acc'].append(k1)
                except:
                    dicts.tales[k][k2]['not'].append(k1)

# TODO: separating print trees from accepted lists
parse(True)
x.print_dicts()
