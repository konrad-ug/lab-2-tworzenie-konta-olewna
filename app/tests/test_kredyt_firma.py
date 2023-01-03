import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..Konto_firmowe import Konto_firmowe

class TestCreateBankAccount(unittest.TestCase):
    nazwa_firmy = "Zabka"
    nip = "8461627563"

    @patch('app.Konto_firmowe.Konto_firmowe.request_api_gov', return_value=True)
    def setUp(self,mock):
        self.konto_firma = Konto_firmowe(self.nazwa_firmy,self.nip)

    @parameterized.expand([
        (3000,1000,[306,-1775,-5],True,4000),
        (2000,1000,[-1775],False,2000),
        (6666,1000,[100,302,-120,69],False,6666)
    ])

    def test_kredyt_firma(self,saldo,kwota,historia,expect,saldo_po_kredycie):
        self.konto_firma.saldo = saldo
        self.konto_firma.historia = historia
        expectation = self.konto_firma.zaciagnij_kredyt(kwota)
        self.assertEqual(expectation,expect)
        self.assertEqual(self.konto_firma.saldo,saldo_po_kredycie)