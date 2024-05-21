import sqlite3

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []
        self.conn = sqlite3.connect('library.db')
        self.cur = self.conn.cursor()
        self.books_table()
        
    def books_table(self):
        query= '''
        CREATE TABLE IF NOT EXISTS (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT
        )
        '''    
        self.cur.execute(query)
        self.conn.commit() 
        
    def add_book(self, book: Book):
        books_table = "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)"
        self.cur.execute(query, (book.title, book.author))
        self.conn.commit()
        self.books.append(book)
        
    def remove_book(self, book:Book):
        query = "DELETE FROM books WHERE title = ? and author = ?"
        self.cur.execute(query, (book.title, book.author))
        self.conn.commit()
        if book in self.books:
            self.books.remove(book)
            
    def search_book(self, search_str):
        #is_included = [book for book in self.books if book.title == search_str or book.author == search_str ]
        is_included = [book for book in self.books if search_str in [book.title, book.author]]
        if is_included:
            query = '''SELECT  FROM books WHERE title = ? and author = ?'''
            result = self.cur.execute(query, (search_str,))
            return [ Book(row[0],row[1], row[2])for row in result]
        
new_book = Book("Harry Potter", "J.K.Rowling", "1234")

library = Library()

library.add_book(new_book)

print(library.search_book("Harry Potter"))