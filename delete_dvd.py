import connect_to_db
import print_mod


#WYWOŁANIE ZAPYTANIE SQL USUWAJĄCEGO Z BAZY WSKAZANY REKORD(Y)
def SQLdeleteDVD(dvdToDelete):
    
 
    try:
        sql_to_delete = 'SELECT *  from filmydvd.dvd WHERE DVD_TITLE LIKE "%'+ dvdToDelete+'%"'
        SQL = 'DELETE from filmydvd.dvd WHERE DVD_TITLE LIKE "%'+ dvdToDelete+'%"'

        db=connect_to_db.db_connection()
 
        print("Połączenie z bazą danych MySQL zostało ustanowione.")
        if db.is_connected():
            print("Połączenie jest aktywne.")
            
        else:
            print("Połączenie zostało zamknięte.")
         
        c = db.cursor()
        c.execute(sql_to_delete)
        output=c.fetchall()
        print_mod.Print_findings(output)
        answer=input("Czy zatwierdzasz pliki do skasowania (T/N)?   ")
        if answer.lower()=='t':
            c.execute(SQL)
            input("Tekord(y) został(y) usunięty(e) Naciśniej [ENETER]...")
        else:
            input("Zrezygnowałeś z kasowania rekordów Naciśniej [ENETER]...")
        db.commit()
        c.close()
        db.close()
        
        
    except:
        
        print("Błąd podczas usuwania reordu(ów)")
        input("Naciśniej [ENETER]...")
        


# ODCZYT DANYCH WPROWADZANYCH PRZEZ UŻYTKOWNIKA
# I WYWOŁANIE FUNKCJI USUWAJĄCEJ REKORD(Y) Z
def DeleteDVD():
    print()
    dvdToDelete = input("Wprowadź tytuł filmu lub jego fragment:  ")
        
    SQLdeleteDVD(dvdToDelete)
