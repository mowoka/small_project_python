class Person:

    def __init__(self, nama, umur, email):
        self.nama = nama
        self.umur = umur
        self.email = email

class Nasabah:

    def __init__(self, nasabah, profesi, id):
        self.nasabah = nasabah
        self.profesi = profesi
        self.id = id
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Penarikan tidak bisa dilakukan")
    
    
    def status(self):
        print('------Status-------')
        print(f'Nasabah ID : {self.id}')
        print(f'Nama : {self.nasabah.nama}')
        print(f'Umur : {self.nasabah.umur}')
        print(f'Profesi : {self.profesi}')
        print(f'Jumlah Deposit : {self.balance}')
        print('------endStatus-------')

class DataNasabah:

    def __init__(self, nasabah, max_nasabah):
        self.nasabah = nasabah
        self.max_nasabah = max_nasabah
        self.database = []
    
    def addNasabah(self, nasabah):
        if len(self.database) < self.max_nasabah:
            self.database.append(nasabah)
            return True
        else:
            return False

    def list_databse(self):
        print('=============list data ==============')
        for i in self.database:
            print(f'ID : {i.id}')
            print(f'Nama : {i.nasabah.nama}')
            print(f'Deposit : {i.balance}')


p1 = Person("Giofanny Mowoka",23, "giomowoka@gmail.com")
p2 = Person("Mokaz",20,"mokaz@gmail.com")
p3 = Person("Kimmy",30,"kimy@gmail.com")

nasabah1 = Nasabah(p1, "IT", 1)
nasabah2 = Nasabah(p2, "HRD", 2)
nasabah3 = Nasabah(p3, "Editor", 3)

nasabah1.deposit(200000)
nasabah2.deposit(200000)
nasabah3.deposit(200000)
nasabah1.withdraw(50000)
nasabah1.withdraw(30000)
nasabah2.withdraw(40000)

dt_bni = DataNasabah("Bank BNI", 10)
dt_bni.addNasabah(nasabah1)
dt_bni.addNasabah(nasabah2)
dt_bni.addNasabah(nasabah3)

dt_bni.list_databse()