import random, os
import mysql.connector
import print_mod
import connect_to_db

#WYWOŁANIE ZAPYTANIE SQL
def ShowDatabase():
    show = ("Select * from filmydvd.dvd")
    print(show)
    conf=[]

    try:
        # conf=db_conf.imp_config()
        # db = mysql.connector.connect(user=conf[0],
        #                              password=conf[1],
        #                               host=conf[2],
        #                                database=conf[3])
        # db = mysql.connector.connect(user="root",
        #                              password="Trawa!1967",
        #                               host="localhost",
        #                                database="filmydvd")

        db=connect_to_db.db_connection()
   
        print("Połączenie z bazą danych MySQL zostało ustanowione.")
        if db.is_connected():
            print("Połączenie jest aktywne.")
            
        else:
            print("Połączenie zostało zamknięte.")
         
        c = db.cursor()
        c.execute(show)
        output = c.fetchall()
        
        
        c.close()
        # data=c.fetchone()
        # print ("Database version : %s " % data)
        db.close()
        
        # input("Rekord zosstał zapisany, naciśnij [ENTER]...")
        # input("Naciśniej [ENETER]...")
    except mysql.connector.Error as err:
        print("Błąd podczas łączenia z bazą danych MySQL:", err)
        # input("Naciśniej [ENETER]...")
        
    # except:
    #     print("WYSTĄPIŁ PROBLEM Z DODANIEM REKORDU DO BAZY")
    #     input("Naciśniej [ENETER]...")
    print_mod.Print_findings(output)
    # os.system('cls')
    # print('--------------------------------------')
    # print("WYNIKI WYSZUKIWANIA")
    # print()
    # if output==None:
    #     print("NIE ZNALEZIONO REKORDÓW")
    #     print('--------------------------------------')
    
    # print("|----------------------------------------------------------------------------------------------------|")
    # print("|            Tytuł             |        Rola główna      !    Rola drugoplanowa    | Rok  |  Gatunek |")
    # print("|----------------------------------------------------------------------------------------------------|")
    # for entry in output:
    #     print('|'+"{:^30}".format(entry[0])+'|'+ "{:^25}".format(entry[1])+'|'+"{:^25}".format(entry[2])+'|'+"{:^6}".format(entry[3])+'|'"{:^10}".format(entry[4])+'|')
    # print("|----------------------------------------------------------------------------------------------------|")
    # input("\n\nNaciśnij [ENTER]...")