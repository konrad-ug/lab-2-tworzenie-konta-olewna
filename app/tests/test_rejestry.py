import unittest

from ..RejestrKont import RejestrKont
from ..Konto import Konto

class TestRejestry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    pesel2 = "11111111111"
    dane = {
        "imie": "Bartek",
        "saldo":17
    }

    @classmethod
    def setUpClass(cls):
        cls.konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(cls.konto)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista_kont = []

    def test_dodanie_drugiego_konta(self):
        RejestrKont.dodaj_konto(self.konto)
        self.assertEqual(RejestrKont.ile_kont(),2)

    def test_dodanie_trzeciego_konta(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel2)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(),3)

    def test_znajdz_konto_po_peselu(self):
        znalezione_konto = RejestrKont.wyszukaj_konto_po_peselu("01234567890")
        self.assertEqual(znalezione_konto, self.konto )

    def test_nieznajdz_konto_po_peselu(self):
        znalezione_konto = RejestrKont.wyszukaj_konto_po_peselu("12111111111")
        self.assertEqual(znalezione_konto, None)

    def test_aktualizuj_konto_po_peselu(self):
        konto = Konto(self.imie,self.nazwisko,"09876543211")
        dodaj_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodaj_konto, konto)
        konto_do_aktualizacji = RejestrKont.zaaktualizuj_konto_po_peselu("09876543211",self.dane)
        self.assertEqual(konto_do_aktualizacji.imie, self.dane['imie'])
        self.assertEqual(konto_do_aktualizacji.nazwisko, self.nazwisko)
        self.assertEqual(konto_do_aktualizacji.saldo, self.dane['saldo'])
        # self.assertEqual(konto_do_aktualizacji,{"imie":"Bartek","nazwisko":"Januszewski","pesel":"09876543211","saldo":17})

    def test_nieudane_dodanie_konta(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        dodaj_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodaj_konto, None)

    def test_usuwanie_konta_po_peselu(self):
        konto = Konto(self.imie,self.nazwisko,"09876543211")
        RejestrKont.dodaj_konto(konto)
        ile_kont = RejestrKont.ile_kont()
        usunięte_konto = RejestrKont.usun_konto_po_peselu('09876543211')
        self.assertEqual(usunięte_konto, konto)
        bez_usuniętego = RejestrKont.ile_kont()
        self.assertEqual(ile_kont-1,bez_usuniętego)

    def test_nieudane_usuwanie_konta_po_peselu(self):
        ile_kont = RejestrKont.ile_kont()
        usunięte_konto = RejestrKont.usun_konto_po_peselu('98989898989')
        self.assertEqual(usunięte_konto,None)
        bez_usuniętego = RejestrKont.ile_kont()
        self.assertEqual(ile_kont,bez_usuniętego)