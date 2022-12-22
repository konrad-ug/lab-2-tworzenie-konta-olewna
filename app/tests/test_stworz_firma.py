import unittest
from unittest.mock import patch
from ..Konto_firmowe import Konto_firmowe

class TestCreateCompanyAccount(unittest.TestCase):
    nazwa_firmy = "Januszex"
    nip = "8461627563"
    fake_nip = "8461627565"

    @patch('app.Konto_firmowe.Konto_firmowe.request_api_gov', return_value=True)
    def test_udane_tworzenie_konta_firmowego(self,mock):
        konto_firmowe = Konto_firmowe(self.nazwa_firmy,self.nip)
        self.assertEqual(konto_firmowe.nazwa_firmy,self.nazwa_firmy)
        self.assertEqual(konto_firmowe.nip,self.nip)

    def test_tworzenie_konta_firmowego_dlugi_nip(self):
        nip = "01234567895426"
        konto_firmowe = Konto_firmowe(self.nazwa_firmy,nip)
        self.assertEqual(konto_firmowe.nip,"Niepoprawny NIP!")
    
    def test_tworzenie_konta_firmowego_krotki_nip(self):
        nip = "012345"
        konto_firmowe = Konto_firmowe(self.nazwa_firmy,nip)
        self.assertEqual(konto_firmowe.nip,"Niepoprawny NIP!")

    @patch('app.Konto_firmowe.Konto_firmowe.request_api_gov', return_value=False)
    def test_tworzenie_konta_firmowego_pranie(self,mock):
        konto_firmowe = Konto_firmowe(self.nazwa_firmy,self.fake_nip)
        self.assertEqual(konto_firmowe.nip, "Pranie!")