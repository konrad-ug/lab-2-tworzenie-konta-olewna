from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    if RejestrKont.dodaj_konto(konto) != None:
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Konto już istnieje"), 400

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
    return jsonify("Nie znaleziono konta"), 404

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_dane_konta_z_podanym_peselem(pesel):
    print("Request o update w koncie z podanym numerem pesel")
    dane = request.get_json()
    szukane_konto = RejestrKont.zaaktualizuj_konto_po_peselu(pesel,dane)
    if szukane_konto != None:
        return jsonify(szukane_konto), 200
    return jsonify("Nie znaleziono konta"), 404
    
@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto_z_podanym_peselem(pesel):
    print("Request o usuniecie konta z podanym peselem")
    RejestrKont.usun_konto_po_peselu(pesel)
    return jsonify("Usunięto konto z podanym peselem"), 200

