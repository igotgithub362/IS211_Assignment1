"A class book with attributes author and title"


class Book:
    author = ""
    title = ""

    """A constructor to create book with attributes author and title"""
    def __init__(self, titleName, authorName):
        self.title = titleName
        self.author = authorName

    "A function to print string representing the book object"


    def display(self):
        print(f"\'{self.title}\', written by {self.author}")



#create two objects of books
obj_1 = Book("Of Mice and Men", "John Steinbeck")
obj_2 = Book("To kill a Mockingbird", "Harper Lee")

#calls the display function to display the objects

obj_1.display()
obj_2.display()

