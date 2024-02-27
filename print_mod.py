import os
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