import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 12345678901
        pierwsze_konto = Konto(imie,nazwisko,pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,pesel, "PESEL nie został zapisany!") #feature3
        self.assertEqual(len(str(pierwsze_konto.pesel)),11,"Niepoprawny PESEL") #feature4

    def test_tworzenie_konta_kod(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 12345678901
        pierwsze_konto = Konto(imie,nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel,pesel, "PESEL nie został zapisany!") #feature3
        self.assertEqual(pierwsze_konto.kod_rabatowy[:5],"PROM_","Niepoprawny kod promocyjny")
        self.assertEqual(len(pierwsze_konto.kod_rabatowy),8,"Niepoprawny kod promocyjny")
        self.assertEqual(pierwsze_konto.saldo,50,"Kod promocyjny nie działa!")
    #tutaj proszę dodawać nowe testy