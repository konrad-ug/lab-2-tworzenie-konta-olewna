from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o liczbe kont")
    liczba_kont = RejestrKont.ile_kont() 
    return jsonify(liczba_kont), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print("Request o wyszukanie konta z podanym numerem pesel")
    szukane_konto = RejestrKont.wyszukaj_konto_po_peselu(pesel)
    if szukane_konto:
        return jsonify(szukane_konto["imie"], szukane_konto["nazwisko"]), 200
    return jsonify("Account not found"), 404

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_dane_konta_z_podanym_peselem(pesel):
    dane = request.get_json()
    szukane_konto = RejestrKont.wyszukaj_konto_po_peselu(pesel)
    if szukane_konto:
        szukane_konto["imie"] = dane["imie"]
        szukane_konto["nazwisko"] = dane["nazwisko"]
        szukane_konto["saldo"] = dane["saldo"]
        return jsonify(szukane_konto), 204
    return jsonify("Account not found"), 404
    