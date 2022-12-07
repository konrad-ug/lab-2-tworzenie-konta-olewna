from app.Konto import Konto

class RejestrKont():
    lista_kont = []

    @classmethod
    def dodaj_konto(cls,konto):
        for konta in cls.lista_kont:
            if konta.pesel == konto.pesel:
                return None
        cls.lista_kont.append(konto)
        return konto

    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)

    @classmethod
    def wyszukaj_konto_po_peselu(cls,pesel):
        for konto in cls.lista_kont:
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def zaaktualizuj_konto_po_peselu(cls,pesel,nowe_dane):
        konto = cls.wyszukaj_konto_po_peselu(pesel)
        if konto != None:
            konto.imie = dane['imie'] if 'imie' in dane else konto.imie
            konto.nazwisko = dane['nazwisko'] if 'nazwisko' in dane else konto.nazwisko
            konto.saldo = dane['saldo'] if 'saldo' in dane else konto.saldo
        return konto
    
    @classmethod
    def usun_konto_po_peselu(cls,pesel):
        konto = cls.wyszukaj_konto_po_peselu(pesel)
        if konto != None:
            cls.lista_kont.remove(konto)
        return konto