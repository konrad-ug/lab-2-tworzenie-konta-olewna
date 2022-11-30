from app.Konto import Konto

class RejestrKont():
    lista_kont = []

    @classmethod
    def dodaj_konto(cls,konto):
        cls.lista_kont.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)

    @classmethod
    def wyszukaj_konto_po_peselu(cls,pesel):
        for k in cls.lista_kont:
            if k.pesel == pesel:
                return k
        return None