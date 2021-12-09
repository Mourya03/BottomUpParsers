from mylexer import MyLexer, tokens
import ply.yacc as yacc


lexer = MyLexer()


def MyParser():
    def p_E(p):
        '''E : E PLUS T
             | E MINUS T
        '''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

    def p_E_T(p):
        'E : T'
        p[0] = p[1]

    def p_T(p):
        '''T : T MUL F
             | T DIV F
        '''
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            try:
                p[0] = p[1] / p[3]
            except ZeroDivisionError:
                print("NO ZEROOOOO!!!!")

    def p_T_F(p):
        'T : F'
        p[0] = p[1]

    def p_F(p):
        '''F : G POWER F
             | MINUS G
        '''
        if p[1] == '-':
            p[0] = -p[2]
        elif p[2] == 'p':
            p[0] = p[1] ** p[3]

    def p_F_G(p):
        'F : G'
        p[0] = p[1]

    def p_G(p):
        '''G : NUM
             | LEFTPAR E RIGHTPAR
        '''
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_NUM(p):
        '''NUM : INT
               | FLOAT
        '''
        p[0] = p[1]

    def p_error(p):
        print("syntax error!")

    return yacc.yacc()