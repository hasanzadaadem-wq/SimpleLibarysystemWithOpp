class Book:
    def __init__(self, BookID, title, author, pageCount ):
        self.book = BookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.isAvaliable = True


    def showInfo(self):
        print(f"""
ID: {self.bookID}
title: {self.title}
Author:{self.author}
PageCount:{self.pageCount}
        """)

        if self.isAvailable:
            print("Status: Available.")
        else:
            print("Status: Borrowed.")

    def borrow(self):
        if self.isAvaliable:
            self.isAvaliable = False
            print(f"{self.title}Returned")
        else:
            print("This book Is Already in the libary.")

    def returnBook(self):
        if not self.IsAvaliable:
            self.IsAvaliable = True
            print(f"{self.title} returned.")
        else:
            print(f"\nThis book is already in the libary.")


book1 = Book(1,"Clean Code","Robert Martin", 464)
book2 = Book(2,"Python Crash","Eric Mattehs", 560)
book3 = Book(3,"Atomis Habbits","James Clear", 320)



# for i in book1, book2, book3:
#     i.showInfo

