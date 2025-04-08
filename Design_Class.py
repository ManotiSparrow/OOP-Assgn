class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' has {self.pages} pages.")

class FictionBook(Book):
    def special_feature(self):
        print(f"'{self.title}' is a fictional story full of imagination.")

class NonFictionBook(Book):
    def special_feature(self):
        print(f"'{self.title}' is based on real facts and information.")

# Fiction Book
book1 = FictionBook("The Adventures of Tom Sawyer", 250)
book1.describe()
book1.special_feature()

print()

# Non-Fiction Book
book2 = NonFictionBook("Understanding Climate Change", 180)
book2.describe()
book2.special_feature()
