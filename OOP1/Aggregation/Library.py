
from Book import Book 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Aggregation: Books are associated with Library but can exist independently
        #เป็น collection แบบ list
        #self.books.append(book)  # เพิ่มข้อมูลใน list
        #self.books.remove(book)  # ลบข้อมูลออกจาก list

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f"{book.title} แต่งโดย {book.author}")
            
# Test Aggregation
library = Library("ห้องสมุดสามพร้าว")
book1 = Book("OOP by Python", "วิศวะ รักเรียน")
book2 = Book("ระบบ Iot เพื่อชุมชน", "ดร.มุ่งมัน ขยันอ่าน")

library.add_book(book1)
library.add_book(book2)

library.list_books()            