import unittest

from ..RejestrKont import RejestrKont
from ..Konto import Konto

class TestRejestry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "01234567890"
    pesel2 = "11111111111"

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