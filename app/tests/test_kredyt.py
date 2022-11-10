import unittest

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    nazwa_firmy = "Zabka"

    def test_kredyt_udany_wariant_a(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [-69,777,420,2137,123]
        self.assertTrue(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo,2000)

    def test_kredyt_udany_wariant_b(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [-69,777,420,2137,-123]
        self.assertTrue(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo,2000)

    def test_kredyt_nieudany_mniej_niz_kredyt(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [123,15,-420,-2137,123]
        self.assertFalse(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo,0)

    def test_kredyt_nieudany_krotko(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.historia = [123,15]
        self.assertFalse(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo,0)