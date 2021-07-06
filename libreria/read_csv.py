# import csv
# with open("export_bookshop.csv", encoding="utf8") as file:
#     print(file.readlines()) #si usas readline, te imprime la primera...se usa en loops para imprimirte linea por linea

import csv
with open("export_bookshop.csv", "w",  encoding="utf8", newline="") as file:
    csv_writer = csv.writer(file, delimiter=",")
    csv_writer.writerow("hola") #writerow necesita un iterable....h,o,l,a
    csv_writer.writerow(["hola"]) 
    csv_writer.writerow("5")