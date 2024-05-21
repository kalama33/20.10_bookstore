import sqlite3

# connect to  'products.db' 
# conn = sqlite3.connect('products.db')
# cursor = conn.cursor()

#func to show products
def display_items(cursor): # to interact with db sqlite
    cursor.execute("SELECT * FROM products") # consultation
    products = cursor.fetchall() # results stored in products
    
    if not products:
        print("No products found in the database.") # verify if products....
    else:
        print("Product ID | Title | Category | Price | Description") # table to be shown
        print("-" * 70) 
        for product in products:
            print(f"{product[0]:<11} | {product[1]:<20} | {product[2]:<10} | ${product[3]:<7.2f} | {product[4]}")


 # for user interaction
def main():
    # connect to db 
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    while True:
        print("\nWarehouse Command-Line Interface")
        print("1. Display Items")
        print("2. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            display_items(cursor)
        elif choice == '2':
            print("Tchuss!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # close the db
    conn.close()

if __name__ == "__main__":
    main()
    







.# print(f"{product[0]:<11} | {product[1]:<20} | {product[2]:<10} | ${product[3]:<7.2f} | {product[4]}")

""" {product[0]:<16}: Aquí, {product[0]} toma el valor del primer elemento de la tupla product, 
que es el ID del producto. La parte :<16 es un formato que se aplica al valor. 

En este caso, :<16 significa que el valor se alineará a la izquierda y ocupará al menos 16 caracteres. 
Si el valor tiene menos de 16 caracteres, se añadirán espacios en blanco a la derecha para cumplir con ese ancho.

|: Esto simplemente agrega el carácter de tubería '|' como separador entre las columnas de la tabla.

{product[1]:<20}: Similar al primer elemento, aquí estamos tomando el segundo elemento de la tupla product, 
que es el título del producto, y asegurando que ocupe al menos 20 caracteres en la salida alineándolo a la izquierda.

{product[2]:<10}: De manera similar, esto toma el tercer elemento de la tupla product, que es la categoría del producto, 
y asegura que ocupe al menos 10 caracteres en la salida alineándolo a la izquierda.

${product[3]:<7.2f}: En esta parte, estamos formateando el cuarto elemento de la tupla product, que es el precio del producto. 

{product[3]} toma el valor del precio y :<7.2f significa que se formateará como un número decimal con dos decimales y 
se alineará a la izquierda ocupando al menos 7 caracteres. También se agrega el símbolo de dólar '$' antes del precio.

{product[4]}: Esta parte simplemente toma el quinto elemento de la tupla product, que es la descripción del producto, 
y lo deja sin ningún formato especial."""
    