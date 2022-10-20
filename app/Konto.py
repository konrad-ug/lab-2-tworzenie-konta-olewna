class Konto:
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.kod_rabatowy=kod_rabatowy
        if self.kod_rabatowy=="PROM_ABC":
            self.saldo+=50