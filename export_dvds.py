import os
import connect_to_db
import csv


# ZAPIS BAZY DO PLIKU CSV)
def ExportCSV():

    SQL="SELECT * FROM filmydvd.dvd"
  
    try:
     
        db=connect_to_db.db_connection()

        print("Połączenie z bazą danych MySQL zostało ustanowione.")
        if db.is_connected():
            print("Połączenie jest aktywne.")
            
        else:
            print("Połączenie zostało zamknięte.")
         
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()
        
    except:
        
        print("Błąd dostępu do bazy")
        input("Naciśniej [ENETER]...")
        return
        
    os.system('cls')
    print("-----------------------------------------------------")
    print("EXPORT BAZY DO PLIKU CSV")
    print("-----------------------------------------------------")
    filename  = input("Podaj nazwę pliku bez rozszerzenia:  ")
    filename ="c:/Python_projects/"+filename+".csv"
    print(filename)
    header=["TITLE", "STAR NAME", "COSTAR NAME", "YEAR", "GENRE"]
    with open(filename, 'w+', encoding='utf-8') as file:
        print(file)
        csvwriter = csv.writer(file)
        print(csvwriter)
        print(header)
        csvwriter.writerow(header)
        for item in output:
            csvwriter.writerow(item)
        print(" Zapis prawidłowy")
        input("Naciśnij [ENTER], aby powrócić do menu...")
