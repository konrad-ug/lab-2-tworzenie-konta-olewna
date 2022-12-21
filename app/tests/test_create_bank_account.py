import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    kod = "PROM_ABC"
    imie = "Dariusz"
    nazwisko = "Januszewski"
    nazwa_firmy = "Zabka"

    def test_tworzenie_konta(self):
        pesel = "12345678901"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,pesel, "PESEL nie został zapisany!") #feature3
        self.assertEqual(len(pierwsze_konto.pesel),11,"Niepoprawny PESEL") #feature4

    def test_tworzenie_konta_kod_rok2000(self):
        pesel = "02290206852"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel,pesel, "PESEL nie został zapisany!") #feature3
        self.assertEqual(len(pierwsze_konto.pesel),11,"Niepoprawny PESEL") #feature4
        self.assertEqual(pierwsze_konto.kod_rabatowy[:5],"PROM_","Niepoprawny kod promocyjny")
        self.assertEqual(len(pierwsze_konto.kod_rabatowy),8,"Niepoprawny kod promocyjny")
        self.assertEqual(pierwsze_konto.rok_urodzenia>1960,True,"Osoba urodzona po 1960r.")
        self.assertEqual(pierwsze_konto.saldo,50,"Kod promocyjny nie działa!")

    def test_tworzenie_konta_kod_rok1800(self):
        pesel = "59823856471"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.rok_urodzenia<=1960,True,"Osoba urodzona po 1960r.")

    def test_tworzenie_konta_kod_rok1990(self):
        pesel = "02090206852"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.rok_urodzenia>1960,False)

    def test_tworzenie_konta_kod_rok2100(self):
        pesel = "02590206852"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.rok_urodzenia>1960,True,"Osoba urodzona po 1960r.")

    def test_tworzenie_konta_kod_rok2200(self):
        pesel = "02790206852"
        pierwsze_konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        self.assertEqual(pierwsze_konto.rok_urodzenia>1960,True,"Osoba urodzona po 1960r.")

    def test_udany_przelew_wychodzacy(self):
        pesel = "01234567890"
        konto = Konto(self.imie,self.nazwisko,pesel,self.kod)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(800)
        self.assertEqual(konto.saldo,1000-800)

    def test_nieudany_przelew_wychodzacy(self):
        pesel = "01234567890"
        konto = Konto(self.imie,self.nazwisko,pesel)
        konto.saldo = 100
        konto.zaksieguj_przelew_wychodzacy(800)
        self.assertEqual(konto.saldo>=0,True,"Błąd z przelewem")

    def test_przelew_przychodzacy(self):
        pesel = "01234567890"
        konto = Konto(self.imie,self.nazwisko,pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_przychodzacy(800)
        self.assertEqual(konto.saldo,1000+800)

    def test_udany_przelew_ekspresowy_konto(self):
        pesel = "01234567890"
        konto = Konto(self.imie,self.nazwisko,pesel)
        konto.saldo = 200
        konto.przelew_ekspresowy(200)
        self.assertEqual(konto.saldo,200-200-1)

    def test_nieudany_przelew_ekspresowy_konto(self):
        pesel = "01234567890"
        konto = Konto(self.imie,self.nazwisko,pesel)
        konto.saldo = 200
        konto.przelew_ekspresowy(210)
        self.assertEqual(konto.saldo,"Saldo nie moze byc na minusie")
