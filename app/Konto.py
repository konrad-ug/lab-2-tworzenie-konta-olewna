class Konto:
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.kod_rabatowy=kod_rabatowy
        self.rok_urodzenia = int(self.pesel[:2])
        if int(self.pesel[2]) in [8,9]:
            self.rok_urodzenia += 1800
        elif int(self.pesel[2]) in [0,1]:
            self.rok_urodzenia += 1900
        elif int(self.pesel[2]) in [2,3]:
            self.rok_urodzenia += 2000
        elif int(self.pesel[2]) in [4,5]:
            self.rok_urodzenia += 2100
        elif int(self.pesel[2]) in [6,7]:
            self.rok_urodzenia += 2200
        if self.kod_rabatowy=="PROM_ABC":
            if self.rok_urodzenia > 1960:
                self.saldo+=50
                