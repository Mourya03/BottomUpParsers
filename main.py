import os
os.system("cls")

# Menu Drive Program

while True:
    print('*'*100)
    print('*'*((100-34)//2) + ' B O T T O M - U P - P A R S E R S '+'*'*((100-34)//2))
    print('*'*100)
    print("\n\n1) SLR PARSER\n2) CLR PARSER\n3) LALR PARSER\n\n0) Exit\n\nYour Choice : ")
    choice = int(input())
    if choice==1:
        os.system("cls")
        print("* * * * * S L R - P A R S E R * * * * *\n\n")
        os.system("python slr.py")
    elif choice==2:
        os.system("cls")
        print("* * * * * C L R - P A R S E R * * * * *\n\n")
        os.system("python clr.py")
    elif choice==3:
        os.system("cls")
        print("* * * * * L A L R - P A R S E R * * * * *\n\n")
        os.system("python lalr.py")
    elif choice==0:
        break
    print("\n\n\n")
