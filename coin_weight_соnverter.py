def num():
    x = input("Введите номинал монеты (1,2,5,10):")
    y = input ("Введите сколько рублей всего  в монетах ")
    a = 0
    kg = 0
    try:
      if (x == "1"):
        a = 3.24
        gr = (int(y)/1)
      if (x == "2"):
        a = 5.13
        gr = (int(y)/2)
      if (x == "5" ):
        a = 6.5
        gr = (int(y)/5)
      if (x == "10"):
        gr = (int(y)/10)
        a = 5.65
      kg = gr*a/1000
      z = gr*a
      z = float('{:.2f}'.format(z))
      gr = float('{:.3f}'.format(gr))
      kg = float('{:.3f}'.format(kg))
      print("У вас " + str(z) + " грамм монет номиналом " + str(x) + " руб.")
  
      print("Или " + str(kg) + " килограмм")
      print ("Количесво монет: " + str(gr))
    except ZeroDivisionError:
      print("Нельзя делить на ноль")
    except (ValueError, TypeError,NameError):
      print("Похоже вы ввели неверное значение")
      print ("Повторите ввод")
      return num()



def ves():
    x = input("Введите номинал монеты (1,2,5,10): ")
    y = int(input("Введите вес  монет в граммах "))
    a = 0
    kg = 0
    b = 0
    try:
      if (x == "1"):
        b = 3.24
        gr = (float(y)/b)
      if (x == "2"):
        a = 5.13
        gr = (y/a)
      if (x == "5" ):
        a = 6.5
        gr = (int(y)/a)
      if (x == "10"):
        a = 5.65
        gr = (y/a)
      rub = gr*int(x)
      
     
      gr = float('{:.1f}'.format(gr))
      rub = float('{:.2f}'.format(rub))
      print("У вас " + str(rub) + " руб номиналом " + str(x) + " руб.")
  
      
      print ("Количесво монет: " + str(gr))
    except ZeroDivisionError:
      print("Нельзя делить на ноль")
      return ves()
    except (ValueError, TypeError,NameError):
      print("Похоже вы ввели неверное значение")
      print ("Повторите ввод")
      return ves()
   
def err():
    print ("Неверный выбор")
    return var()

def var():

    print ("1 - Из суммы монет в вес")
    print ("2 - Из веса монет в сумму руб.")
    print ("3 - Выход")
    v = input("Пожалуйста выберите тип  конвертирования: ")
    if (v != "1") and (v != "2") and (v != "3"):
        err()
    if (v == "1"):
        num()
    if (v == "2"):
        ves()
    if (v == "3"):
        print ("Выход из программы...")
        exit()

    
       
          
    
print ("Выберите действие: ")
var()





