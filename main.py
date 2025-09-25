from document import Document, Report, Contract


r1 = Report("Звіт", "Фінансовий", "2025-09-25", "Іван", "Директор")
r2 = Report("Звіт", "Технічний", "2025-09-26", "Олена", "Керівник")
c1 = Contract("Контракт", "Оренда", "2025-09-20", "Компанія А", "Компанія Б", "2026-09-20")
c2 = Contract("Контракт", "Поставка", "2025-09-15", "Фірма Х", "Фірма Y", "2025-12-31")

print("\n--- Інформація про документи ---\n")
r1.showDocInfo()
c2.showDocInfo()

print("\n--- Зміна адресата звіту ---\n")
r1.changeViewer("Генеральний директор")
r1.showDocInfo()

print("\n--- Продовження контракту ---\n")
c2.extendContractExpirationDate("2027-09-20")
c2.showDocInfo()

print("\n--- Статистика ---")
print("Кількість створених документів:", Document.getDocumentCount())
