import unittest
import parameterized

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    nazwa_firmy = "Zabka"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    @parameterized([
        ([-69,777,420,2137,123],2000,2000),
    ])

    def test_kredyt_udany_wariant_a(self,historia,kwota,saldo):
        self.konto.historia = historia
        self.assertTrue(self.self.konto.zaciagnij_kredyt(kwota))
        self.assertEqual(self.self.konto.saldo,saldo)

    def test_kredyt_udany_wariant_b(self):
        self.konto.historia = [-69,777,420,2137,-123]
        self.assertTrue(self.konto.zaciagnij_kredyt(2000))
        self.assertEqual(self.konto.saldo,2000)

    def test_kredyt_nieudany_mniej_niz_kredyt(self):
        self.konto.historia = [123,15,-420,-2137,123]
        self.assertFalse(self.konto.zaciagnij_kredyt(2000))
        self.assertEqual(self.konto.saldo,0)

    def test_kredyt_nieudany_krotko(self):
        self.konto.historia = [123,15]
        self.assertFalse(self.konto.zaciagnij_kredyt(2000))
        self.assertEqual(self.konto.saldo,0)