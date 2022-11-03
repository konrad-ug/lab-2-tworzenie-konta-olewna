import unittest

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    nazwa_firmy = "Zabka"

    def test_udany_zapisywanie_przelewu_przychodzacego(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertListEqual(konto.historia,[100])

    def test_udane_zapisywanie_przelewu_wychodzacego(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertListEqual(konto.historia,[-100])