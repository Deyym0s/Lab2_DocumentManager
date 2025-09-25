from abc import ABC, abstractmethod

class Document(ABC):
    _count = 0

    def __init__(self, doc_type, doc_name, doc_date):
        self._doc_type = doc_type
        self._doc_name = doc_name
        self._doc_date = doc_date
        Document._count += 1

    def getDocType(self): return self._doc_type
    def getDocName(self): return self._doc_name
    def getDocDate(self): return self._doc_date

    @abstractmethod
    def showDocInfo(self):
        pass

    @staticmethod
    def getDocumentCount():
        return Document._count

class Printable:
    def print_to_console(self, text):
        print("==== Друк інформації про документ ====")
        print(text)
        print("=" * 38, end="\n\n")


class Report(Document, Printable):
    def __init__(self, doc_type, doc_name, doc_date, report_author, report_viewer):
        super().__init__(doc_type, doc_name, doc_date)
        self._report_author = report_author
        self._report_viewer = report_viewer

    def changeViewer(self, new_viewer): self._report_viewer = new_viewer

    def showDocInfo(self):
        info = (f"Тип: {self._doc_type}\n"
                f"Назва: {self._doc_name}\n\n"
                f"Автор: {self._report_author}\n"
                f"Адресат: {self._report_viewer}\n\n"
                f"Дата створення: {self._doc_date}")

        self.print_to_console(info)


class Contract(Document, Printable):
    def __init__(self, doc_type, doc_name, doc_date, first_party, second_party, expiration_date):
        super().__init__(doc_type, doc_name, doc_date)
        self._contract_first_party = first_party
        self._contract_second_party = second_party
        self._contract_expiration_date = expiration_date

    def extendContractExpirationDate(self, new_expiration_date):
        self._contract_expiration_date = new_expiration_date

    def showDocInfo(self):
        info = (f"Тип: {self._doc_type}\n"
                f"Назва: {self._doc_name}\n\n"
                f"Перша сторона: {self._contract_first_party}\n"
                f"Друга сторона: {self._contract_second_party}\n\n"
                f"Дата укладення контракту: {self._doc_date}\n"
                f"Дата закінчення контракту: {self._contract_expiration_date}")

        self.print_to_console(info)

