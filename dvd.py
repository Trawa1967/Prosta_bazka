import os
import add_dvd
import lookup_dvds
import browse_dvds
import delete_dvd
import export_dvds
import import_csv


#MAIN MENU
def Menu():
    os.system('cls')
    print("""
    ===========================================
    BAZA FILMÓW
    ===========================================
    1. Dodaj film do bazy
    2. Wyświetl bazę filmów
    3. Wyszukaj film(y)
    4. Usuń film
    5. Export danych do pliku csv
    6. Import danych z pliku csv
    7. Zakończ
    ==========================================
    """)

    choice=input("Wybierz funkcję i naciśnij ENTER:  ")
    return choice

#OBŁUGA MENU
choice=''
while choice != '7':
    choice =Menu()
    if choice == '1':
        os.system('cls')
        add_dvd.AddDVD()
    if choice == '2':
        os.system('cls')
        browse_dvds.ShowDatabase()
    if choice == '3':
        os.system('cls')
        lookup_dvds.LookupDV()
    if choice == '4':
        os.system('cls')
        delete_dvd.DeleteDVD()
    if choice == '5':
        os.system('cls')
        export_dvds.ExportCSV()
    if choice == '6':
        os.system('cls')
        import_csv.ImportCSV()
        # print("FUNKCJA JESZCZE NIE DZIAŁA ..")
        # input("Naciśnij [ENTER], aby powrócić do menu...")
