from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scanner Pro</title>
    <script src="https://unpkg.com/@zxing/library@latest"></script>

    <style>
        body {
            background-color: #0d0d0d;
            color: #00ffcc;
            font-family: Arial;
            text-align: center;
        }

        h2 {
            margin-top: 20px;
        }

        video {
            border: 2px solid #00ffcc;
            border-radius: 10px;
            margin-top: 10px;
        }

        button {
            background-color: #00ffcc;
            color: black;
            border: none;
            padding: 10px 15px;
            margin: 10px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background-color: #00ccaa;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            background: #1a1a1a;
            margin: 5px auto;
            padding: 8px;
            width: 80%;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<h2>📷 Scanner (QR + Código de Barras)</h2>

<video id="video" width="320" height="240"></video>

<br>

<button onclick="iniciar()">▶ Iniciar</button>
<button onclick="detener()">⏹ Detener</button>
<button onclick="limpiar()">🧼 Limpiar</button>

<h3>📦 Detectados:</h3>
<ul id="lista"></ul>

<audio id="beep" src="https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg"></audio>

<script>
let codeReader;
let scanning = false;
let codigosDetectados = new Set();

function iniciar() {
    if (scanning) return;

    codeReader = new ZXing.BrowserMultiFormatReader();
    scanning = true;

    codeReader.decodeFromVideoDevice(null, 'video', (result, err) => {
        if (result) {
            let codigo = result.text;

            // Evitar repetidos
            if (codigosDetectados.has(codigo)) return;

            codigosDetectados.add(codigo);

            // Sonido
            document.getElementById("beep").play();

            // Mostrar en lista
            let li = document.createElement("li");
            li.textContent = codigo;
            document.getElementById("lista").appendChild(li);

            // Enviar a Flask
            fetch('/barcode', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({codigo: codigo})
            });
        }
    });
}

function detener() {
    if (codeReader) {
        codeReader.reset();
        scanning = false;
    }
}

function limpiar() {
    document.getElementById("lista").innerHTML = "";
    codigosDetectados.clear();
}
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/barcode', methods=['POST'])
def recibir():
    data = request.json
    print("Código recibido:", data['codigo'])
    return "OK"

app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')