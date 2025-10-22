from flask import Flask, jsonify, abort
import math

app = Flask(__name__)

MAX_N = 1000  

def parity_label(value: int) -> str:
    return "par" if value % 2 == 0 else "impar"

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial_route(n):
    if n < 0:
        return jsonify({"error": "n debe ser entero no negativo"}), 400
    if n > MAX_N:
        return jsonify({"error": f"n demasiado grande (máx {MAX_N})"}), 400

    fact = math.factorial(n)
    label = parity_label(n)  
    return jsonify({
        "numero": n,
        "factorial": str(fact),   
        "paridad": label
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
