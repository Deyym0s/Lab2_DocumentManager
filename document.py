from abc import ABC, abstractmethod

class Document(ABC):
    __count = 0  # приватне статичне поле

    def __init__(self, doc_type, doc_name, doc_date):
        self.__doc_type = doc_type
        self.__doc_name = doc_name
        self.__doc_date = doc_date
        Document.__count += 1

    def getDocType(self): return self.__doc_type
    def getDocName(self): return self.__doc_name
    def getDocDate(self): return self.__doc_date

    @abstractmethod
    def showDocInfo(self):
        pass

    @staticmethod
    def getDocumentCount():
        return Document.__count


class Printable:
    def print_to_console(self, text):
        print("==== Друк інформації про документ ====")
        print(text)
        print("=" * 38, end="\n\n")


class Report(Document, Printable):
    def __init__(self, doc_type, doc_name, doc_date, report_author, report_viewer):
        super().__init__(doc_type, doc_name, doc_date)
        self.__report_author = report_author
        self.__report_viewer = report_viewer

    def changeViewer(self, new_viewer):
        self.__report_viewer = new_viewer

    def showDocInfo(self):
        info = (f"Тип: {self.getDocType()}\n"
                f"Назва: {self.getDocName()}\n\n"
                f"Автор: {self.__report_author}\n"
                f"Адресат: {self.__report_viewer}\n\n"
                f"Дата створення: {self.getDocDate()}")

        self.print_to_console(info)


class Contract(Document, Printable):
    def __init__(self, doc_type, doc_name, doc_date, first_party, second_party, expiration_date):
        super().__init__(doc_type, doc_name, doc_date)
        self.__contract_first_party = first_party
        self.__contract_second_party = second_party
        self.__contract_expiration_date = expiration_date

    def extendContractExpirationDate(self, new_expiration_date):
        self.__contract_expiration_date = new_expiration_date

    def showDocInfo(self):
        info = (f"Тип: {self.getDocType()}\n"
                f"Назва: {self.getDocName()}\n\n"
                f"Перша сторона: {self.__contract_first_party}\n"
                f"Друга сторона: {self.__contract_second_party}\n\n"
                f"Дата укладення контракту: {self.getDocDate()}\n"
                f"Дата закінчення контракту: {self.__contract_expiration_date}")

        self.print_to_console(info)
