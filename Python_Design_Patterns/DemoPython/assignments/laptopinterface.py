from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print('Inside HP')

class Dell(TouchScreenLaptop):

    def scroll(self):
        print('Inside Dell')

class HPNoteBook(HP):

    def scroll(self):
        print("HP Notebook Scroll")

    def click(self):
        print("HP Notebook Click")

class DELLNotebook(HP):

    def scroll(self):
        print("Dell Notebook Scroll")

    def click(self):
        print("Dell Notebook Click")

hp = HPNoteBook()
hp.click()
hp.scroll()

dell = DELLNotebook()
dell.click()
dell.scroll()
