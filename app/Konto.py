from datetime import date

class Konto:
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.kod_rabatowy=kod_rabatowy
        self.historia = []
        self.wiadomosc = "Twoja historia konta to: "
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
        
    def zaksieguj_przelew_wychodzacy(self,kwota):
        if self.saldo-kwota>=0:
            self.saldo -= kwota
            self.historia.append(kwota*-1)

    def zaksieguj_przelew_przychodzacy(self,kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelew_ekspresowy(self,kwota):
        oplata_ekspres = -1
        if self.saldo>=kwota:
            self.saldo = self.saldo-kwota+oplata_ekspres
            self.historia.append(kwota*-1)
            self.historia.append(oplata_ekspres)
        else:
            self.saldo = "Saldo nie moze byc na minusie"
        # self.saldo = self.saldo-kwota+oplata_ekspres if self.saldo>=kwota else "Saldo nie moze byc na minusie"
    
    def kredyt_wariant_a(self):
        if (len(self.historia) >= 3 and self.historia[-1]>0 and self.historia[-2]>0 and self.historia[-3]>0):
            return True

    def kredyt_wariant_b(self,kwota):
        if (len(self.historia)>=5 and sum(self.historia[-5:])>kwota):
            return True

    def zaciagnij_kredyt(self,kwota):
        if self.kredyt_wariant_a() or self.kredyt_wariant_b(kwota):
            self.saldo += kwota
            return True
        else:
            return False

    def wyslij_historie_na_maila(self,adresat,smtp):
        data = date.today()
        temat = f"Wyciąg z dnia {data}"
        tresc = self.wiadomosc + str(self.historia)
        if smtp.wyslij(temat,tresc,adresat):
            return True
        return False