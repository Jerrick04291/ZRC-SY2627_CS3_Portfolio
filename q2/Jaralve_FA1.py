class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and not isinstance(number_of_pages, bool) and number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)

publication1 = Publication("Encyclopedia", "John Smith")
publication2 = Publication("Dictionary", "Mary Jones")

book1 = Book("Noli Me Tangere", "Jose Rizal", 400)
book2 = Book("El Filibusterismo", "Jose Rizal", 350)

magazine1 = Magazine("Science Today", "Alex Cruz", 12)
magazine2 = Magazine("Tech World", "Sam Lee", 8)

print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()