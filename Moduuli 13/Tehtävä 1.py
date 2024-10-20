from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    if luku <= 1:
        return {"Number": luku, "isPrime": False}
    if luku == 2:
        return {"Number": luku, "isPrime": True}
    if luku % 2 == 0:
        return {"Number": luku, "isPrime": False}

    for i in range(3, int(luku ** 0.5) + 1, 2):
        if luku % i == 0:
            return {"Number": luku, "isPrime": False}
    return {"Number": luku, "isPrime": True}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


