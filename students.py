from book import *
class student:
    def __init__(self,studentID,name):
        self.name = name
        self.borrowedBooks =[]

    def showInfo(self):
                print(f"""
ID: {self.studentID}
title: {self.name}
AuPthor:{len(self.borrovedBooks)}
        """)

    def borrowBook(self, book):
         if book.IsAvailable:
               book.borrow()
               self.borrowedBooks.append(book)
         else:
               print("Book is not Available...")


    def returnBook(self, book):
          if book in self.borrowedBooks:
                book.returnBook()
                self.borrowedBooks.remove(book)
          else:
                print("Book is not available...")

student1 = student(1, "Taleh")
student2 = student(2, "Ramiz")
student3 = student(3, "Ramal")

book1 = Book(1,"clean Code", "Robert Martin",464)
student1.borrowBook(book1)
print("Reading...")
student1.returnBook(book1)



                
                
          
             
        