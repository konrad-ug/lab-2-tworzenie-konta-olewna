import unittest

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    nazwa_firmy = "Zabka"
    nip = "0123456789"

    def test_udany_zapisywanie_przelewu_przychodzacego(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertListEqual(konto.historia,[100])

    def test_udany_zapisywanie_przelewu_wychodzacego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertListEqual(konto.historia,[100,-100])

    def test_udany_zapisywanie_przelewu_ekspresowego_osoba(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        konto.przelew_ekspresowy(100)
        self.assertListEqual(konto.historia,[100,-100,-1])

    def test_udany_zapisywanie_przelewu_ekspresowego_firma(self):
        konto_firma = Konto_firmowe(self.nazwa_firmy,self.nip)
        konto_firma.zaksieguj_przelew_przychodzacy(100)
        konto_firma.przelew_ekspresowy(100)
        self.assertListEqual(konto_firma.historia,[100,-100,-5])

    