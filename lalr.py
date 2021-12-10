from myparser import MyParser

if __name__ == "__main__":
    parser = MyParser()
    while True:
        try:
            s = input('Input Exp >>>> ')
        except EOFError:
            break
        if s == 'exit':
            break
        result = parser.parse(s)
        print(f"Result Is -> { {result} }\n")