# b. Usor spre Mediu (obligatoriu)
# 1.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# o variabila este ca si o cutiuta care contine niste valori, definite de catre programator

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte

# tip_mobila = str('dulap')
# pret_dulap = int(350)
# pret_usa_dulap = float(75.5)
# reduceri_incluse = bool(False)
# print(tip_mobila)
# print(pret_dulap)
# print(pret_usa_dulap)
# print(reduceri_incluse)

# 3. Utilizat functia type pentru a verifica daca au tipul de date asteptat
# print(type(reduceri_incluse))

# 4.
# Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia

# pret_usa_dulap = float(75.5)
# print(round(pret_usa_dulap))
# print(type(pret_usa_dulap))

# 5.
# folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)

# tip_mobila = 'dulap'
# pret_dulap = 350
# pret_usa_dulap = float(75.5)
# reduceri_incluse = bool(False)
# print(f"Va oferim un " + tip_mobila + " la pretul de " + str(pret_dulap))
# print(f"Pretul unei usi de " + tip_mobila + " este de " + str(pret_usa_dulap))
# print(" In cazul achizitiei a mai multor articole de tip " + tip_mobila + " se poate discuta de o reducere? " + str(reduceri_incluse))
# print("In cazul deterioarii produsului " + tip_mobila + " in decurs de 7 zile va oferim un refund de " + str(pret_dulap))
# 6.
# citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

# nume = str(input("Numele meu este: "))
# prenume = str(input("Prenumele meu este: "))
# lungime_nume_complet = len(nume+prenume)
# print(lungime_nume_complet)

# 7.
# citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

# lungime = float(input("Lungime = "))
# latime = float(input("Latime = "))
# arie = lungime*latime
# print("Aria dreptunghiului este: " + str(arie))
# #
# 8.
# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

# string = 'Coral is either the stupidest animal or the smartest rock'
# print(len(string))
# x = int(input("x = "))
# print(string[:-x])

#
# 9.
# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# string = 'Coral is either the stupidest animal or the smartest rock'
# # print(len(string))
# first_five = string[0:5]
# last_five = string[53:]
# print(first_five+ " " +last_five)
#
# 10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'

# string = 'Coral is either the stupidest animal or the smartest rock'
# the = ' the '
# count = string.count(the)
# print(count)
# #
# 11.
# acelasi string
# # inlocuieste the cu THE peste tot
# # printeaza rezultatul
#
# string = 'Coral is either the stupidest animal or the smartest rock'
# the = ' the '
# THE = the.upper()
# print(string.replace(the, THE))
#
# 12.
# acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

# string = 'Coral is either the stupidest animal or the smartest rock'
# string.find('rock')
# print(len(string))
# print(string.find('rock'))
# print(string[0:53])

#
# 13.
# citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel
# se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

# x = str.lower(input("Talk to me, HuMan: "))
# print(len(x))
# prim_caracter = x[0]
# ultim_caracter = x[-1]
# print(prim_caracter)
# print(ultim_caracter)
# assert prim_caracter == ultim_caracter
# print("Identic")

# 14.
# avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)

# x = "0123456789"
# print(x[2::2])
# print(x[1::2])

# 15.
# acelasi string de la 12 'Coral is either the stupidest animal or the smartest rock'
# folositi un assert ca sa verificati daca acest string contine doar numere
# hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare


# s = 'Coral is either the stupidest animal or the smartest rock'
# x = '1Coral 15 1either the stupidest animal or the smartest rock'
# assert s.isdigit()

#aici nu imi place assertul pentru ca daca schimb stringul si adaug un numar nu imi afiseaza corect...

# c. Optionale (may need google)
# 16.
# citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc

# x = str(input("Tell me something: "))
# def middle_char(x):
#    return x[(len(x)-1)//2]
# print(middle_char(x))

# # 17.
# # Folosind assert, verificati daca un string este palindrom

# x = 'madam'
# assert x == x[::-1]
# print('Palindrom OK')

# # 18.
# # folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# # si salveaza fiecare cuvant intr-o variabila
# # acum printeaza ambele variabile pentru verificare

# s = input("Scrie ceva: ") #create user input
# lista_input = s.split() #split input into chunks
# print(lista_input) # print chunked input as list
# cuvant1 = lista_input[0] #create variable with position 0 from the input list
# cuvant2 = lista_input[1] #create variable with position 1 from the input list
# print(cuvant1)
# print(cuvant2)

# # 19.
# # citeste un string de la tastatura (eg: alabala portocala)
# # salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# # capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# # => alAbAlA portocAla

# #create user input
# string = input("Scrie ceva: ")
# #find out the length of the variable 'string'
# print(len(string))
# #find first character from the string
# first = string[0]
# print(string[0])
# #find last character from the string
# last = string[-1]
# #string between index 0 and -1
# removed = string[1:-1]
# #capitalize first_character in the string
# print(string.replace(first, first.upper()))
# #capitalize first_character in the whole string position 1
# middle = removed.replace(first, first.upper())
# print(middle)
# #capitalize 1st character in the string apart from index 0 and -1
# final = first + middle + last
# print(final)

# s = input("Enter smth: ")
# print(s[0] + s[1:-1].replace(s[0].lower(), s[0].upper()) + s[-1])

# # 20.
# # citeste un user de la tastatura
# # citeste o parola
# # afiseaza: 'Parola pt user x este ***** si are x caractere'
# # ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# # eg: parola abc => ***
# # parola abcd => ****

username = input("Please enter your user: ")
password = input("Please enter your password: ")
#find out the length of the password
password_length = len(password)
#transform username into * characters
password_display = len(password) * '*'

print(f'Parola pt user {username} este {password_display} si are {password_length} caractere')