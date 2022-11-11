import unittest

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    nazwa_firmy = "Zabka"
    nip = "0123456789"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    def test_udany_zapisywanie_przelewu_przychodzacego(self):
        self.konto.zaksieguj_przelew_przychodzacy(100)
        self.assertListEqual(self.konto.historia,[100])

    def test_udany_zapisywanie_przelewu_wychodzacego(self):
        self.konto.zaksieguj_przelew_przychodzacy(100)
        self.konto.zaksieguj_przelew_wychodzacy(100)
        self.assertListEqual(self.konto.historia,[100,-100])

    def test_udany_zapisywanie_przelewu_ekspresowego_osoba(self):
        self.konto.zaksieguj_przelew_przychodzacy(100)
        self.konto.przelew_ekspresowy(100)
        self.assertListEqual(self.konto.historia,[100,-100,-1])

    def test_udany_zapisywanie_przelewu_ekspresowego_firma(self):
        self.konto_firma = Konto_firmowe(self.nazwa_firmy,self.nip)
        self.konto_firma.zaksieguj_przelew_przychodzacy(100)
        self.konto_firma.przelew_ekspresowy(100)
        self.assertListEqual(self.konto_firma.historia,[100,-100,-5])

    