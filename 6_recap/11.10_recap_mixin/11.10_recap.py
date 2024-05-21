
class Book:
    def __init__(self, title, sales):
        self.title = title
        self.sales = sales
        
class StringRepresentationMixin:
    def __str__(self):
        return f'title:{self.title}'

class BestSellerMixin:
    def is_bestseller(self):
        return self.sales >= 5000

         
class EnhancedBook(StringRepresentationMixin,BestSellerMixin,Book):
    pass

book1 = EnhancedBook("Orlando", 100000)
print(book1)

print(book1.is_bestseller())
 
 
  