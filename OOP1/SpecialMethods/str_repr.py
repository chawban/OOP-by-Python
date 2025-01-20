class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# สร้างอ็อบเจ็กต์ของ Book
book = Book("The Great Gatsby", "F. Scott Fitzgerald")

# เรียกใช้ __str__ โดยตรงจาก print()
print(book)  # Output: Book: The Great Gatsby by F. Scott Fitzgerald

# เรียกใช้ __repr__ โดยตรง
print(repr(book))  # Output: Book('The Great Gatsby', 'F. Scott Fitzgerald')
