import random, os
import connect_to_db
import print_mod

#WYWOŁANIE ZAPYTANIE SQL
def SQLLookupDVD(searchby, searchtext):
    SQL = ('Select * from filmydvd.dvd WHERE ' +searchby+ ' LIKE "%'+ searchtext+'%"' )
    print(SQL)

    try:
        db=connect_to_db.db_connection()
 
        print("Połączenie z bazą danych MySQL zostało ustanowione.")
        if db.is_connected():
            print("Połączenie jest aktywne.")
            
        else:
            print("Połączenie zostało zamknięte.")
         
        c = db.cursor()
        c.execute(SQL)
        input("Naciśniej [ENETER]...")
        output = c.fetchall()
        c.close()
        db.close()
        print_mod.Print_findings(output)
        input("Naciśniej [ENETER]...")
    except mysql.connector.Error as err:
        print("Błąd podczas łączenia z bazą danych MySQL:", err)
        input("Naciśniej [ENETER]...")


#ODCZYT DANYCH WPROWADZANYCH PRZEZ UŻYTKOWNIKA
# I WYWOŁANIE FUNKCJI WYSZUKUJĄCEJ
def LookupDV():
    print()
    print("""
        Podaj kryteria wyszukiwania:
        1. Tytuł filmu
        2. Rola główna
        3. Rola drugoplanowa
        4. Rok produkcji
        5: Gatunek
        """)
    choice = input("\nWybierz pozcyje menu i nacisniej [ENETER]...:  ")

    searchby=''
    searchtxt=''
    if choice =="1":
        searchby = "DVD_TITLE"
        searchtxt = input("Wprowadź tytuł filmu lub jego fragment:  ")
    elif choice =="2":
        searchby = "DVD_STAR_NAME"
        searchtxt = input("Wprowadź nazwisko aktora głównej roli:  ")
    elif choice =="3":
        searchby = "DVD_COSTAR_NAME"
        searchtxt = input("Wprowadź nazwisko aktora roli drugoplanowej:  ")
    elif choice =="4":
        searchby = "DVD_YEAR"
        searchtxt = input("Wprowadź rok premier filmu:  ")
    elif choice =="5":
        searchby = "DVD_GENRE"
        print("""
        Podaj gatunek filmu:
        1. Dramat
        2. Horror
        3. Komedia
        4. Romans
            """)
        entrychoice = input("\t")
        if entrychoice == "1":
            searchtxt="\"Dramat\""
        elif entrychoice == "2":
            searchtxt="\"Horror\""
        elif entrychoice == "3":
            searchtxt="\"Komedia\""
        elif entrychoice == "4":
            searchtxt="\"Romans\""
        else:
            print("BŁĘDNY WYBÓR")
            input("Naciśnij [ENTER], aby wrócić do menu:   ")
            return
        
    SQLLookupDVD(searchby, searchtxt)

def Print_findings(output):
    os.system('cls')
    print('--------------------------------------')
    print("WYNIKI WYSZUKIWANIA")
    print()
    if output==None:
        print("NIE ZNALEZIONO REKORDÓW")
        print('--------------------------------------')
    
    print("|----------------------------------------------------------------------------------------------------|")
    print("|            Tytuł             |        Rola główna      !    Rola drugoplanowa    | Rok  |  Gatunek |")
    print("|----------------------------------------------------------------------------------------------------|")
    for entry in output:
        print('|'+"{:^30}".format(entry[0])+'|'+ "{:^25}".format(entry[1])+'|'+"{:^25}".format(entry[2])+'|'+"{:^6}".format(entry[3])+'|'"{:^10}".format(entry[4])+'|')
    print("|----------------------------------------------------------------------------------------------------|")
    input("\n\nNaciśnij [ENTER]...")