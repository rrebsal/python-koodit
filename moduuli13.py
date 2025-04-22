from flask import Flask, jsonify

moduuli13 = Flask(__name__)

airport_data = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EFET": {"Name": "Enontekio Airport", "Municipality": "Enontekio"},
    "EFJY": {"Name": "Jyvaskyla Airport", "Municipality": "Jyvaskyla"},
    "EFRO": {"Name": "Rovaniemi Airport", "Municipality": "Rovaniemi"}
}

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#1
@moduuli13.route("/alkuluku/<int:number>")
def prime_check(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

#2
@moduuli13.route("/kenttä/<icao>")
def airport_info(icao):
    icao = icao.upper()
    if icao in airport_data:
        data = airport_data[icao]
        return jsonify({
            "ICAO": icao,
            "Name": data["Name"],
            "Municipality": data["Municipality"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    moduuli13.run(port=3000)