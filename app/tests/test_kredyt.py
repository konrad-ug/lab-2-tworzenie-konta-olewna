import unittest
from parameterized import parameterized, parameterized_class

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    @parameterized.expand([
        ([-69,777,420,2137,123],True,2000,2000),
        ([-69,777,420,2137,-123],True,2000,2000),
        ([123,15,-420,-2137,123],False,2000,0),
        ([123,15],False,2000,0)
    ])

    def test_kredyt_wariant_(self,historia,exp,kwota,saldo):
        self.konto.historia = historia
        expectation = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(expectation,exp)
        self.assertEqual(self.konto.saldo,saldo)

    # def test_kredyt_udany_wariant_b(self):
    #     self.konto.historia = [-69,777,420,2137,-123]
    #     self.assertTrue(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo,2000)

    # def test_kredyt_nieudany_mniej_niz_kredyt(self):
    #     self.konto.historia = [123,15,-420,-2137,123]
    #     self.assertFalse(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo,0)

    # def test_kredyt_nieudany_krotko(self):
    #     self.konto.historia = [123,15]
    #     self.assertFalse(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo,0)