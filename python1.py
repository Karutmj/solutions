import math 

list= [30, 4, 6, 3, 9, 42]
tbigest=max(list)
Length=len(list)#przypisanie do zmiennej length dlugosci listy
list.sort()#metoda sort która sortuje liste
print("The lowewst number is "+str(list[0])) #konwertowanie zmiennej z int do str wyswietlenie pierwszego znaku listy
print(list)#drukowanie listy
print("The biggest number of "+str(Length)+" numbers in list is "+str(tbigest))

form= "t"
while form == "t":
    print("Wzór funkcji kwadratowej: ax^2+bx+c")
    a=float(input("Podaj wspolczynniki a= "))
    b=float(input("Podaj wspolczynniki b= "))
    c=float(input("Podaj wspolczynniki c= "))
    
    Obliczenia=(b*b-(4*a*c))
    Pierwiastek_z_delty=math.sqrt(Obliczenia);
    print("Delta równa:" +str(Obliczenia))
    print("Pierwiastek z Delty :" +str(Pierwiastek_z_delty))
    if Obliczenia>0 :
       pierwiastek_nr_one=(((-1*b)-Pierwiastek_z_delty)/(2*a))
       pierwiastek_nr_two=(((-1*b)+Pierwiastek_z_delty)/(2*a))
       print("x1= "+str(pierwiastek_nr_one))
       print("x2= "+str(pierwiastek_nr_two))
       form=input('Jeszczed raz??t/n: ')
    
    elif Obliczenia==0 :
       pierwiastek_nr_one=(-b/2*a)
       print("x0="+str(pierwiastek_nr_one))
       form=input('Jeszczed raz??t/n: ')
     
    else :
       print("brak pierwiastków")
       form=input('Jeszczed raz??t/n: ')
