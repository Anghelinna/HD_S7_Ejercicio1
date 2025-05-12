from flask import Flask, jsonify
from db import obtener_productos

app = Flask(__name__)

@app.route("/api/productos")
def productos():
    datos = obtener_productos()
    return jsonify(datos)

if __name__ == "__main__":
    app.run(debug=True)
