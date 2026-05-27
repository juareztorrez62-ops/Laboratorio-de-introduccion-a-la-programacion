from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "productos.db"

# ─── Inicializar base de datos ───────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS catalogo (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo   TEXT    UNIQUE NOT NULL,
            nombre   TEXT    NOT NULL,
            precio   REAL    NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ─── Helpers ─────────────────────────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # permite acceder por nombre de columna
    return conn

# ─── Páginas ─────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scanner")
def scanner():
    return render_template("scanner.html")

@app.route("/catalogo")
def catalogo_page():
    return render_template("catalogo.html")

# ─── Ticket (sesión en memoria) ───────────────────────────────────────────────
ticket = []          # lista de dicts {codigo, nombre, precio, cantidad}
ultimo_codigo = None

def buscar_en_ticket(codigo):
    for item in ticket:
        if item["codigo"] == codigo:
            return item
    return None

@app.route("/guardar", methods=["POST"])
def guardar():
    global ultimo_codigo
    data    = request.get_json()
    codigo  = data.get("codigo", "").strip()

    if not codigo:
        return jsonify({"ok": False, "error": "Código vacío"}), 400

    # Buscar en catálogo
    conn = get_db()
    row  = conn.execute("SELECT * FROM catalogo WHERE codigo = ?", (codigo,)).fetchone()
    conn.close()

    if row is None:
        return jsonify({"ok": False, "error": "Producto no encontrado en catálogo"}), 404

    # Evitar duplicado inmediato del escáner
    if codigo == ultimo_codigo:
        return jsonify({"ok": True, "duplicado": True})
    ultimo_codigo = codigo

    # Agregar o incrementar cantidad en el ticket
    existente = buscar_en_ticket(codigo)
    if existente:
        existente["cantidad"] += 1
    else:
        ticket.append({
            "codigo":   row["codigo"],
            "nombre":   row["nombre"],
            "precio":   row["precio"],
            "cantidad": 1
        })

    return jsonify({"ok": True})

@app.route("/productos")
def productos_lista():
    return jsonify(ticket)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    global ticket
    data   = request.get_json()
    codigo = data.get("codigo", "")
    ticket = [i for i in ticket if i["codigo"] != codigo]
    return jsonify({"ok": True})

@app.route("/cantidad", methods=["POST"])
def cantidad():
    data     = request.get_json()
    codigo   = data.get("codigo", "")
    nueva    = int(data.get("cantidad", 1))
    for item in ticket:
        if item["codigo"] == codigo:
            item["cantidad"] = max(1, nueva)
            break
    return jsonify({"ok": True})

@app.route("/limpiar", methods=["POST"])
def limpiar():
    global ticket, ultimo_codigo
    ticket        = []
    ultimo_codigo = None
    return jsonify({"ok": True})

# ─── Catálogo CRUD ────────────────────────────────────────────────────────────
@app.route("/catalogo/lista")
def catalogo_lista():
    conn     = get_db()
    rows     = conn.execute("SELECT * FROM catalogo ORDER BY nombre").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route("/catalogo/agregar", methods=["POST"])
def catalogo_agregar():
    data   = request.get_json()
    codigo = data.get("codigo", "").strip()
    nombre = data.get("nombre", "").strip()
    precio = data.get("precio")

    if not codigo or not nombre or precio is None:
        return jsonify({"ok": False, "error": "Faltan campos"}), 400

    try:
        conn = get_db()
        conn.execute(
            "INSERT INTO catalogo (codigo, nombre, precio) VALUES (?, ?, ?)",
            (codigo, nombre, float(precio))
        )
        conn.commit()
        conn.close()
        return jsonify({"ok": True})
    except sqlite3.IntegrityError:
        return jsonify({"ok": False, "error": "El código ya existe"}), 409

@app.route("/catalogo/editar", methods=["POST"])
def catalogo_editar():
    data   = request.get_json()
    codigo = data.get("codigo", "").strip()
    nombre = data.get("nombre", "").strip()
    precio = data.get("precio")

    if not codigo or not nombre or precio is None:
        return jsonify({"ok": False, "error": "Faltan campos"}), 400

    conn = get_db()
    conn.execute(
        "UPDATE catalogo SET nombre = ?, precio = ? WHERE codigo = ?",
        (nombre, float(precio), codigo)
    )
    conn.commit()
    conn.close()
    return jsonify({"ok": True})

@app.route("/catalogo/eliminar", methods=["POST"])
def catalogo_eliminar():
    data   = request.get_json()
    codigo = data.get("codigo", "").strip()

    conn = get_db()
    conn.execute("DELETE FROM catalogo WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})

# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)