"""
YBS401 Odev 5 Dosyadan metin okuyup json dosyasi olusturma odevi.
* dateutil paketini pip ile kurmaniz gerekmektedir.
* dosya okuma methodunu yazmaniz gerekmektedir.
* dosya yazma methodunu yazmaniz gerekmektedir.
* yas hesaplama methodunu yazmaniz gerekmektedir.
* yas hesaplarken dateutil.relativedelta fonksiyonunu kullanmaniz gerekmektedir. 
* ornek girdiler ve ornek ciktilar verilmistir.
* degisiklik yapmaniz gereken yerler isaretlenmistir, diger kisimlari degistirmeyiniz.

Ad Soyad:
Ogrenci No:
Bolum:
Sinif:

"""


from datetime import date, datetime
import sys
from dateutil.relativedelta import *  # https://pypi.org/project/python-dateutil/
import json


class Person:
    name_surname = ""
    father_name = ""
    mother_name = ""
    age = 0  # not birthday!
    city = ""

    def set_age(self, str_date):
        birthday = datetime.fromisoformat(str_date.strip())
        today = date.today()
        """bu satirlari silip yerine 
        dateutil.relativedelta() fonksiyonunu kullanarak
        kisinin yasini hesaplayan kodu yaziniz"""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def read_file(file_name):
    """bu satirlari silip yerine 
    readlines() fonksiyonunu kullanarak
    file_name ile adi verilen 
    dosyayi okuyan ve okudugu satirlari lines icerisine atan kodu yaziniz"""
    return lines


def write_file(file_name, content):
    """bu satirlari silip yerine 
    write() fonksiyonunu kullanarak
    file_name ile adi verilen 
    content ile icerigi verilen 
    dosyayi yazan kodu yaziniz"""


def fill_person(lines):
    p1 = Person()
    p1.name_surname = lines[0].strip()
    p1.father_name = lines[1].strip()
    p1.mother_name = lines[2].strip()
    p1.set_age(lines[3])
    p1.city = lines[4].strip()
    return p1


def main():
    try:
        file_name = sys.argv[1]
        lines = read_file(f"{file_name}.txt")
        person1 = fill_person(lines)
        my_json = person1.toJSON()
        write_file(f"{file_name}.json", my_json)
        print("Ok!")
    except:
        print("""
        Hata!
        Dosya bulunamadi!
        programi cagirirken dosya adini parametre olarak eklemelisiniz!
        ornek: "python odev5.py kisi2" """)


main()
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)
def age(self):
    if hasattr(self, "_age"):
        return self._age

    today = datetime.date.today()

    age = today.year - self.birthdate.year

    if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
        age -= 1

    self._age = age
    return age
filename = input('input the filename: ')
#read the file
def read_from_file(filename):
    content = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "-" not in line:
                content.append(float(line))
    return content

print(read_from_file(filename))
filename = input('input the filename: ')
#read the file
def write_from_file(filename):
    content = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "-" not in line:
                content.append(float(line))
    return content

print(write_from_file(filename))

