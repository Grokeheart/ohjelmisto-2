import mysql.connector
from flask import Flask, request

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='username',
         password='password',
         autocommit=True,
         charset='utf8mb4',
         collation='utf8mb4_general_ci'
         )


app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    sql = f"SELECT name, municipality FROM airport where ident='{ICAO}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in res:
            return {"ICAO": ICAO, "Name": row[0], "Municipality": row[1]}
    return

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
