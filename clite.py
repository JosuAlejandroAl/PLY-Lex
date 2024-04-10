
import ply.lex as lex

tokens = ['INT', 'FLOAT']

t_ignore = ' \t'

def t_FLOAT(t):
    r'(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    t.value = float(t.value.replace('_', ''))
    return t

def t_INT(t):
    r'\d+(_\d+)*'
    t.value = int(t.value.replace('_', ''))
    return t

def getLexer():
    return lex.lex()
