from MyModule import*
import sys
console_picture()
availablelog=['Mihhail','Zack','Lord123']
availablepass=['qWERTY1"','4elik1!','Vasilii2002']
while 1:
    print("1. Зарегестрироваться")
    print("2. Войти в существующий аккаунт")
    print("3. Выйти из программы")
    choise=input("Выберите пункт: ")
    check(choise)
    if str(choise)=="1":
        signup(availablelog,availablepass)
    elif str(choise)=="2":
        signin(availablelog,availablepass)
    elif str(choise)=="3":
        sys.exit(0)