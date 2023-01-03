from .Konto import Konto
import requests
import os
from datetime import date

class Konto_firmowe(Konto):
    def __init__(self,nazwa_firmy,nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.historia = []
        self.walidacja_nip(nip)

    def przelew_ekspresowy(self,kwota):
        oplata_ekpres = -5
        if self.saldo>=kwota:
            self.saldo = self.saldo-kwota+oplata_ekpres
            self.historia.append(kwota*-1)
            self.historia.append(oplata_ekpres)
        else:
            self.saldo="Saldo nie moze byc na minusie"
        # self.saldo = self.saldo - kwota + oplata_ekpres if self.saldo>=kwota else "Saldo nie moze byc na minusie"

    def kredyt_wariant_a(self,kwota):
        if self.saldo>kwota*2:
            return True

    def kredyt_wariant_b(self):
        if -1775 in self.historia:
            return True

    def zaciagnij_kredyt(self, kwota):
        if self.kredyt_wariant_a(kwota) and self.kredyt_wariant_b():
            self.saldo+=kwota
            return True
        else:
            return False

    def walidacja_nip(self,nip):
        if len(nip) == 10:
            if self.czy_nip_istnieje(nip):
                self.nip = nip
            else:
                self.nip = "Pranie!"
        else:
            self.nip = "Niepoprawny NIP!"

    @classmethod
    def czy_nip_istnieje(cls,nip):
        gov = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        data = date.today()
        url = f"{gov}api/search/nip/{nip}?date={data}"
        return cls.request_api_gov(url)

    @classmethod
    def request_api_gov(cls, url):
        return requests.get(url).status_code == 200