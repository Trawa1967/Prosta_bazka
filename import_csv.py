import os
import connect_to_db
import csv


# IPORT DANYC Z PLIKU CVS
def ImportCSV():

    # SQL="SELECT * FROM filmydvd.dvd"
    with open('C:/Python_projects/New_projects/import_dvd.csv', 'r',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        next(csvreader) #Pominięcie wiersza tytułowego w pliku
        print(csvreader)
        add_dvd = ("INSERT INTO DVD values (%s, %s, %s, %s, %s)")
        try:
            db=connect_to_db.db_connection()
            c = db.cursor()
            for row in csvreader:
                print(row)
                if len(row) == 5:
                    Title=row[0]
                    Star=row[1]
                    Costar=row[2]
                    Year=row[3]
                    Genre=row[4]
                    data_dvd=(Title, Star, Costar, Year, Genre)
                    c.execute(add_dvd, data_dvd)
            db.commit()
            c.close()
            db.close()
            print("Dane zaimportowane poprawnie....")
            input("Naciśniej [ENETER]...")
        except:
            print("WYSTĄPIŁ PROBLEM Z DODANIEM REKORDU DO BAZY")
