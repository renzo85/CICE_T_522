import json
import csv
with open("./Clase_20/bookshop.json", "r", encoding="utf8") as file:
    bookshop = json.load(file)["books"]

print(bookshop)

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]


def menu():
    print("Bookshop".center(50, "-"))
    print("1. ID")
    print("2. Author")
    print("3. Title")
    print("4. Genre")
    print("5. New book")
    print("6. Modify book")
    print("7. Delete book")
    print("8. Export to csv")
    print("q. Exit")


def get_by_id(id_book, libreria):
    for book in libreria:
        if book["id"] == id_book:
            return book #devolverá el libro apenas encuentre el resultado y termina la función

def print_pretty (book_to_print):
    for k, v in book_to_print.items():
        print(f"{k}: {v}")

def get_by_author(author_book, libreria):
    resultado = []
    for book in libreria:
        if book["author"].lower().find(author_book.lower()) >= 0:
            resultado.append(book)
    return resultado

def books_by_key(search_term, libreria, key):
    resultado = []
    for book in libreria:
        if book[key].lower().find(search_term.lower()) >= 0:
            resultado.append(book)
    return resultado

def create_book(user_genre, user_author, user_title):
    new_book = {}
    new_book["genre"] = user_genre
    new_book["title"] = user_title
    new_book["author"] = user_author
    user_genre = user_genre.lower()
    name_list = user_genre.split()
    if len(name_list) == 1:
        new_book["id"] = f"{name_list[0][0]}{name_list[0][-1]}_{len(bookshop)}"
    
    else:
        new_book["id"] = f"{name_list[0][0]}{name_list[1][0]}_{len(bookshop)}"
    bookshop.append(new_book)

def write_book():
    with open("./Clase_20/bookshop.json", "w", encoding="utf8") as file:
        json.dump({"books":bookshop}, file, ensure_ascii=False, indent = 4)

def export_books():
    with open("./Clase_20/export_bookshop_2.csv", "w",  encoding="utf8", newline="") as file:
        csv_writer = csv.writer(file, delimiter=",")

        csv_writer.writerow(bookshop[0].keys()) #Para las cabeceras

        # for book in bookshop: #Para los valores dentro de cada libro 
        #     book_id = book["id"]
        #     book_title = book["title"]
        #     book_author = book["author"]
        #     book_genre = book["genre"]
        #     csv_writer.writerow([book_id, book_title, book_author, book_genre])

        for book in bookshop:
            csv_writer.writerow(book.values())

       
#-----------------------------------------------

user = "0"
while user != "q":
    menu()
    user = input("Choose: ")

    if user == "1":
        user_id = input("ID: ")
        book = get_by_id(user_id, bookshop)
        print_pretty(book)


    elif user == "2":
        author_book = input("Author: ").lower()
        booklist_by_author = get_by_author(author_book, bookshop)
        for book in booklist_by_author:
            print_pretty(book)


    elif user == "3":
        title = input("Title: ").lower()
        books_by_title = books_by_key(title, bookshop, "title")
        for book in books_by_title:
            print_pretty(book)   
         

    elif user =="4":
        print("Seleccione genre")
        for i, genre in enumerate (genres):
            print(f"{i + 1}.{genre}")      
        user_index = int(input("Choose: "))
        user_genre = genres[user_index - 1]
        result = books_by_key(user_genre, bookshop, "genre")
        print(f"-------Resultados {user_genre}--------")
        for book in result:
            print_pretty(book)
            input ("Continuar: ")
            print("". center(50, "-"))
            print(f"Se han encontrado {len(result)} libros")


    elif user == "5": #CREATE BOOK
        print ("Selecione genero a asignar")
        for i, genre in enumerate (genres):
            print(f"{i + 1}.{genre}")

        user_index = int(input("Choose: "))
        user_genre = genres[user_index - 1]
        user_author = (input("Ingrese nombre autor: "))
        user_title = (input("Ingrese título: "))

        result = create_book(user_genre,user_author,user_title)
        write_book()
  


    elif user =="6": #UPDATE BOOK
        print ("Indique id del libro a actualizar")
        book_id = input("ID: ")
        book_to_update = get_by_id(book_id, bookshop)
        if book_to_update == None:
            print("Libro no encontrado")
        
        else:
            keys = list(book_to_update)
            for i, key in enumerate(keys):
                print(f"{i + 1}. {key}")
            user = int(input("Choose field to modify: ")) - 1
            key = keys[user]
            bookshop.remove(book_to_update)
            book_to_update[key] = input("Nuevo valor: ")
            bookshop.append(book_to_update) #en este punto bookshop ha sido modificado
            write_book()
          

 
    elif user == "7": #DELETE BOOK
        print ("Indique id del libro a eliminar")
        book_id = input("ID: ")
        book_to_delete = get_by_id(book_id, bookshop)
        user = input("Do you want to proceed with the elimination? (Y/N):  ")
        if user.lower() == "y":
            bookshop.remove(book_to_delete) #book es el elemento que estás iterando
            write_book()
    
    elif user == "8":
        export_books()



    elif user.lower() =="q":
        user = user.lower()
        print("Bye")
    
    
    else:
        user = "1"