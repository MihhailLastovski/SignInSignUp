import random
from time import*
import os 
def console_picture():
    """Функция, которая выводит надпись на экран
    """
    a=80
    simvol="*"
    print(simvol*a)
    print("                **    **  ********  **        **            **      ");sleep(0.3)
    print("               **    **  ********  **        **         **     **   ");sleep(0.3)
    print("              ********  **        **        **         **      **  ");sleep(0.3)
    print("             ********  ********  **        **         **      **  ");sleep(0.3)
    print("            **    **  **        **        **         **      **  ");sleep(0.3)
    print("           **    **  ********  ********  ********    **    **   ");sleep(0.3)
    print("          **    **  ********  ********  ********       **      ");sleep(0.3)
    print(simvol*a);sleep(0.3)

def check(x:str):
    """Функция проверки, если пользователь ввел не то значение.
    Применяется только к типу str
    :param str x: текст, который нужно проверить
    """
    while x not in ["1","2","3"]:
        try:
            x=input("Вы ввели неверное значение! Попробуйте еще раз: ")
        except:
            TypeError
            
def signup(l_log:list,l_pass:list):
    """Функция регистрации, которая работает со списками с выбором создания пароля автоматический/самостоятельно
    :param list l_log: список логинов
    :param list l_pass: список паролей
    """
    while 1:
        log1=input("Введите логин: ")
        if log1 not in l_log and len(log1)>=3:
            break
        else:
            print("Данный логин уже занят или состоит меньше, чем из 3 символов")
    l_log.append(log1)
    print("1. Автоматический создать пароль")
    print("2. Самостоятельно создать пароль")
    while 1:
        try:
            valik=input("Выберите пункт: ")
            if valik in ["1","2"]:
                break
            else:
                continue
        except:
            print("Вы ввели неверное значение")
    if valik=="1":
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls=list(str4)
        random.shuffle(ls)
        psword="".join([random.choice(ls) for x in range(12)])
        print(psword)
        l_pass.append(psword)
    elif valik=="2":
        while 1:
            print("В пароле должны содержаться:")
            print("цифры")
            print("буквы в нижнем регистре")
            print("буквы в верхнем регистре")
            print("спец. символы")
            numb=0
            upp=0
            loww=0
            spec=0
            pass1=input("Введите пароль: ")
            for i in pass1:
                    if i.isupper():
                        upp+=1
                    elif i.islower():
                        loww+=1
                    elif i.isdigit():
                        numb+=1
                    else:
                        spec+=1
            if len(pass1)<=5:
                print("Пароль должен содержать не менее 6 символов")
                continue
            elif upp==0:
                continue
            elif numb==0:
                continue
            elif loww==0:
                continue
            elif spec==0:
                continue
            else:
                l_pass.append(pass1)
                break

def signin(loglist:list,passlist:list):
    """Функция применяется к спискам для входа в систему с ограничением на количество попыток ввода пароля.
    После входа в систему запускается игра "Орел/Решка"
    :param list loglist: список логинов
    :param list passlist: список паролей
    """
    trypass=0
    log2=input("Введите логин: ")
    while 1:
        pass2=input("Введите пароль: ")
        if pass2 not in passlist:
            trypass+=1
            print(f"Осталось попыток:{3-trypass}")
        if trypass==3:
            print("Вы исчерпали допустимое количество попыток ввода пароля. Подождите")
            for i in range(1,11):
                print("\r" + "осталось - " + str(10-i), end='')
                sleep(1)
            trypass=0
        if log2 in loglist and pass2 in passlist:
            if loglist.index(log2)==passlist.index(pass2):
                print("Welcome!") #Начало игры
                orel="Орел"
                reshka="Решка"
                orel_sum=0
                reshka_sum=0
                count=0
                print("Хотите подбросить монетку? Да/Нет")
                ask=input(str(""))
                while ask not in ["Да","да","ДА","Нет","нет","НЕТ"]:
                    try:
                        ask=input("Введите правильно=>")
                    except:
                        TypeError
                if ask in ["Да","да","ДА"]:
                    print("Выберите орел или решка:")
                    ask2=input(str(""))
                    while ask2 not in ["Орел","орел","Решка","решка"]:
                        try:
                            ask2=input("Введите правильно=>")
                        except:
                            TypeError
                    while count!=51:
                        count+=1
                        result=random.randint(1,2)
                        if result==1:
                            orel_sum+=1
                        else:
                            reshka_sum+=1
                    print(f"Орел: {orel_sum} Решка: {reshka_sum}")
                    if ask2 in ["Орел","орел"] and orel_sum>reshka_sum:
                        print("Вы выиграли!")
                    elif ask2 in ["Решка","решка"] and reshka_sum>orel_sum:
                        print("Вы выиграли!")
                    else:
                        print("Вы проиграли!")
                else:
                    print("Досвидания!") #Конец игры
                break
            else:
                print("Вы ввели неправильный логин или пароль")
                
        else:
            print("Вы ввели неправильный логин или пароль")  