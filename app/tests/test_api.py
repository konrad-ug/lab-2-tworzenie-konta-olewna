import unittest
import requests

class TestApi(unittest.TestCase):
    body = {
        "imie": "Darek",
        "nazwisko": "Kowalski",
        "pesel": "12345678901"
    }
    body2 = {
        "imie": "Janek",
        "nazwisko":"Brzoza",
        "saldo": 123
    }

    nieistniejący_pesel = "64385729431"
    url = "http://localhost:5000"

    def test_tworzenie_konta(self):
        stworz_res = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(stworz_res.status_code, 201)

    def test_pobierz_konto_po_peselu_udany(self):
        get_res = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_res.status_code, 200)
        body_res = get_res.json()
        self.assertEqual(body_res["imie"],self.body["imie"])
        self.assertEqual(body_res["nazwisko"],self.body["nazwisko"])
        self.assertEqual(body_res["saldo"], 0)

    def test_pobierz_konto_po_peselu_nieudany(self):
        get_res = requests.get(self.url + "/konta/konto/" + self.nieistniejący_pesel)
        self.assertEqual(get_res.status_code, 404)
    
    def test_zmien_dane_konta_z_podanym_peselem(self):
        put_res = requests.put(self.url + "/konta/konto/zmien_dane", self.body2)
        self.assertEqual(put_res.status_code, 204)
        get_res = requests.get(self.url + f"/konta/konto/{self.body['pesel']}").json()
        self.assertEqual(get_res["imie"],self.body2["imie"])
        self.assertEqual(get_res["nazwisko"], self.body2["nazwisko"])
        self.assertEqual(get_res["saldo"], self.body2["saldo"])
        
