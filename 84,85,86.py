class sklad():
    список_валидации = []
    information = {}
    def __init__(self, number, quantity, massa, номер_отсека):
        self.number = number #номер на складе
        self.quantity = quantity #количество на складе
        self.massa = massa #масса товара
        self.номер_отсека = номер_отсека


    def валидация(self):
        for item in sklad.список_валидации:
            if type(item) == str:
                print("вы ввели не число")
                break

    def приём_оргтехники(self, номер_отсека, количество):
        self.номер_отсека = номер_отсека
        self.quantity += количество

    def get_info(self):
        print(sklad.information)

        pass

    #возвращает кол-во товара на складе
    def get_quantity():
        print(self.quantity)

    #возвращает номер товара на складе
    def get_number():
        print(self.number)

    #возвращает массу товара на складе
    def get_massa():
        print(self.massa)

    #выключает аппарат
    def switch_on():
        print("включено")

    #включает аппарат
    def switch_off():
        print("выключено")

class printer(sklad):
    def __init__(self, number, quantity, massa, ink, номер_отсека):
        self.massa = massa
        self.ink = ink # количестов чернил
        self.number = number  # номер на складе
        self.quantity = quantity  # количество на складе
        self.номер_отсека = номер_отсека
        sklad.список_валидации += [number, quantity, massa, ink, номер_отсека]
        параметры = ["number", "quantity", "massa", "ink", "номер отсека"]
        sklad.information = {параметры[item] : sklad.список_валидации[item] for item in range(4)}

    def get_ink(self):
        print(self.ink)

class skaner(sklad):
    def __init__(self, number, quantity, massa, качество):
        self.massa = massa
        self.качество = качество # количестов чернил
        self.number = number  # номер на складе
        self.quantity = quantity  # количество на складе
        self.номер_отсека = номер_отсека
        sklad.список_валидации += [number, quantity, massa, качество, номер_отсека]
        параметры = ["number", "quantity", "massa", "качество", "номер отсека"]
        sklad.information = {sklad.список_валидации[item] : параметры[item] for item in len(параметры)}

    def get_качество():
        print(self.качество)

class ксерокс(sklad):
    def __init__(self, number, quantity, massa, качество, ink):
        self.massa = massa
        self.качество = качество # количестов чернил
        self.number = number  # номер на складе
        self.quantity = quantity  # количество на складе
        self.ink = ink  # количество чернил
        self.номер_отсека = номер_отсека
        sklad.список_валидации += [number, quantity, massa, качество, ink, номер_отсека]
        параметры = ["number", "quantity", "massa", "качество", "ink", "номер отсека"]
        sklad.information = {sklad.список_валидации[item] : параметры[item] for item in len(параметры)}

    def get_качество(self):
        print(self.качество)

    def get_ink(self):
        print(self.ink)



b = printer(1234, 12, 143, 2, 3)
b.приём_оргтехники("склад", 12)
print(b.quantity)
print(b.список_валидации)
b.валидация()
b.get_info()