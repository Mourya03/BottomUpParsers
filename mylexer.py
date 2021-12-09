import ply.lex as lex


tokens = (
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'POWER',
    'LEFTPAR',
    'RIGHTPAR'
)


def MyLexer():
    t_ignore = ' '

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_POWER = r'p'
    t_LEFTPAR = r'\('
    t_RIGHTPAR = r'\)'

    def t_FLOAT(t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(t):
        print("illegal char:", t.value[0])
        t.lexer.skip(1)
    return lex.lex()