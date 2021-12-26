"""
YBS401 Odev 5 Dosyadan metin okuyup json dosyasi olusturma odevi.
* dateutil paketini pip ile kurmaniz gerekmektedir.
* dosya okuma methodunu yazmaniz gerekmektedir.
* dosya yazma methodunu yazmaniz gerekmektedir.
* yas hesaplama methodunu yazmaniz gerekmektedir.
* yas hesaplarken dateutil.relativedelta fonksiyonunu kullanmaniz gerekmektedir. 
* ornek girdiler ve ornek ciktilar verilmistir.
* degisiklik yapmaniz gereken yerler isaretlenmistir, diger kisimlari degistirmeyiniz.

Ad Soyad:Hasan Can
Ogrenci No:2018507033
Bolum:ybs       
Sinif:4

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
       from dateutil.relativedelta
       import relativedelta

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def read_file(file_name):
    with open (dosya_1) as j:
        lines=j.file_name()
    return lines


def write_file(file_name, content):
    with open(dosya_1) as j:
        j=open(file_name,"w")
        j.write(content)
        j.close


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
