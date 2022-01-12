#1 способ
#clear=lambda: os.system('cls')
#clear()
#for i in range(1,6):
#    print("\r" + "Done -" + str(i))
#    print("\r" + "Left -" + str(5-i))
#    time.sleep(2)
#    if i!=5:
#        clear()
#    else:
#        exit()

#2 способ
#for i in range(1,6):
#    print("\r" + "Done -" + str(i) + "pending -" + str(5-i), end='')
#    time.sleep(2)
