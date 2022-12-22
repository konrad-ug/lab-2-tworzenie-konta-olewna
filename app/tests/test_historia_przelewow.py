import unittest
from unittest.mock import patch

from ..Konto import Konto
from ..Konto_firmowe import Konto_firmowe

class TestHistoryOfAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"

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


class TestHistoryOfCompany(unittest.TestCase):
    nazwa_firmy = "Januszex"
    nip = "8461627563"

    @patch('app.Konto_firmowe.Konto_firmowe.request_api_gov', return_value=True)
    def setUp(self,mock):
        self.konto_firma = Konto_firmowe(self.nazwa_firmy,self.nip)


    def test_przelew_przychodzacy_firma(self):
        self.konto_firma.zaksieguj_przelew_przychodzacy(1000)
        self.assertListEqual(self.konto_firma.historia,[1000])

    def test_przelew_wychodzacy_firma(self):
        self.konto_firma.zaksieguj_przelew_przychodzacy(1000)
        self.konto_firma.zaksieguj_przelew_wychodzacy(100)
        self.konto_firma.zaksieguj_przelew_wychodzacy(600)
        self.assertListEqual(self.konto_firma.historia,[1000,-100,-600])

    def test_przelew_ekspresowy_firma(self):
        self.konto_firma.zaksieguj_przelew_przychodzacy(100)
        self.konto_firma.przelew_ekspresowy(100)
        self.assertListEqual(self.konto_firma.historia,[100,-100,-5])