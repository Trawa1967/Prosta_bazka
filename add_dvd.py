import random, os
import connect_to_db


#WYWOŁANIE ZAPYTANIE SQL DODAJĄCEGO REKORD DO BAZY
def SQLAddDVD(Title, Star, Costar, Year, Genre):
    add_dvd = ("INSERT INTO DVD values (%s, %s, %s, %s, %s)")
    data_dvd=(Title, Star, Costar, Year, Genre)
    print(add_dvd)
    print(data_dvd)

    try:
        db=connect_to_db.db_connection()
        
        c = db.cursor()
        c.execute(add_dvd, data_dvd)
        db.commit()
        c.close()
        db.close()
        
        input("Rekord zosstał zapisany, naciśnij [ENTER]...")
    except:
        print("WYSTĄPIŁ PROBLEM Z DODANIEM REKORDU DO BAZY")
        input("Naciśniej [ENETER]...")
#ODCZYT DANYCH WPROWADZANYCH PRZEZ UŻYTKOWNIKA
#I WYWOŁANIE FUNKCJI DODAJĄCEJ REKORD DO BAZY
def AddDVD():
    print("----------------------------------")
    print('DODAJ REORD DO BAZY')
    print('----------------------------------')
    Title = input("Podaj tytuł filmu:  ")
    Star = input("Podaj imię i nazwisko aktora głównej roli:  ")
    Costar = input("Podaj imię i naziwkso aktora  drugoplanowego:  ")
    Year = input("Podaj rok premiery filmu:  ")
    Genre = input("Wprowadź gatunek firmu \n 1. Dramat, \n 2. Horror, \n 3. Komedia, \n 4. Romans:   \n")
    if Genre == '1':
        Genre ="Dramat"
    elif Genre == '2':
        Genre ="Horror"
    elif Genre == '3':
        Genre ="Komedia"
    elif Genre == '4':
        Genre ="Romans"
    else:
        print("BŁĄD PRZY OKREŚLENIU GATUNKU")
        input("Naciśnij [ENETER], abyt wrócic do menu:  ")
    SQLAddDVD(Title, Star, Costar, Year, Genre)