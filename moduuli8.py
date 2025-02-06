#1
import mysql.connector

def hae_lentokentta(icao_koodi):

    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        passwd="N1k0sB3r",
        autocommit=True
    )

    mycursor = yhteys.cursor()

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    val = (icao_koodi,)

    mycursor.execute(sql, val)

    tulos = mycursor.fetchone()

    if tulos:
        nimi, kunta = tulos
        return nimi, kunta
    else:
        return None, None

if __name__ == "__main__":
    icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
    nimi, kunta = hae_lentokentta(icao_koodi)

    if nimi and kunta:
        print(f"Lentokentän nimi: {nimi}")
        print(f"Sijaintikunta: {kunta}")
    else:
        print("Lentoasemaa ei löytynyt.")
