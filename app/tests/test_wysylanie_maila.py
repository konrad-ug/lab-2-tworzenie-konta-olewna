import unittest
from parameterized import parameterized
from datetime import date
from unittest.mock import patch, MagicMock

from ..SMTPConnection import SMTPConnection
from ..Konto import Konto
from ..Konto_firmowe import Konto_firmowe

class TestWysylanieMailaOsoba(unittest.TestCase):
    imie = "Jan"
    nazwisko = "Kowalski"
    pesel = "12345678901"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    @parameterized.expand([
        (100,100,100,True,"jan.kowalski@wp.pl",True),
        (100,100,100,False,"jan.kowalski@wp.pl",False)
    ])

    def test_wysylanie_maila_konto(self,kwota1,kwota2,kwota3,returnval,email,testval):
        self.konto.zaksieguj_przelew_przychodzacy(kwota1)
        self.konto.zaksieguj_przelew_przychodzacy(kwota2)
        self.konto.zaksieguj_przelew_wychodzacy(kwota3)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value = returnval)
        wyslanie = self.konto.wyslij_historie_na_maila(email,smtp)
        self.assertEqual(wyslanie,testval)
        data = date.today()
        tytul = f"Wyciąg z dnia {data}"
        tresc = "Twoja historia konta to: " + str([kwota1,kwota2,-kwota3])
        smtp.wyslij.assert_called_once_with(tytul,tresc,email)

class TestWysylanieMailaFirma(unittest.TestCase):
    firma = "Januszex"
    nip = "8461627563"

    @patch('app.Konto_firmowe.Konto_firmowe.request_api_gov', return_value=True)
    def setUp(self,mock):
        self.konto_firma = Konto_firmowe(self.firma,self.nip)

    @parameterized.expand([
        (100,100,100,True,"januszex@gmail.com",True),
        (100,100,100,False,"januszex@gmail.com",False)
    ])

    def test_wysylanie_maila_firma(self,kwota1,kwota2,kwota3,returnval,email,testval):
        self.konto_firma.zaksieguj_przelew_przychodzacy(kwota1)
        self.konto_firma.zaksieguj_przelew_przychodzacy(kwota2)
        self.konto_firma.zaksieguj_przelew_wychodzacy(kwota3)
        smtp = SMTPConnection()
        smtp.wyslij = MagicMock(return_value = returnval)
        wyslanie = self.konto_firma.wyslij_historie_na_maila(email,smtp)
        self.assertEqual(wyslanie,testval)
        data = date.today()
        tytul = f"Wyciąg z dnia {data}"
        tresc = "Historia konta Twojej firmy to: " + str([kwota1,kwota2,-kwota3])
        smtp.wyslij.assert_called_once_with(tytul,tresc,email)