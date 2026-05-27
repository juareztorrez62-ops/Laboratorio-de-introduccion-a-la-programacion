// ── Abrir escáner ────────────────────────────────────────
document.getElementById("abrirScanner").onclick = () => {
    window.open("/scanner", "_blank", "width=400,height=520");
};

// ── Agregar código manual ────────────────────────────────
document.getElementById("btnManual").onclick = agregarManual;
document.getElementById("codigoManual").addEventListener("keydown", e => {
    if (e.key === "Enter") agregarManual();
});

function agregarManual() {
    const input  = document.getElementById("codigoManual");
    const codigo = input.value.trim();
    if (!codigo) return;

    fetch("/guardar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo})
    })
    .then(r => r.json())
    .then(data => {
        if (data.ok) {
            input.value = "";
            mostrarError(null);
            cargarProductos();
        } else {
            mostrarError(data.error || "Producto no encontrado en catálogo.");
        }
    });
}

function mostrarError(msg) {
    const el = document.getElementById("mensajeError");
    if (msg) {
        el.textContent = "⚠ " + msg;
        el.style.display = "block";
    } else {
        el.style.display = "none";
    }
}

// ── Cargar y renderizar ticket ───────────────────────────
function cargarProductos() {
    fetch("/productos")
    .then(r => r.json())
    .then(data => {
        const tbody      = document.getElementById("tablaProductos");
        const vacia      = document.getElementById("tablaVacia");
        const totalArt   = document.getElementById("totalArticulos");
        const subtotalEl = document.getElementById("subtotalVal");
        const totalEl    = document.getElementById("totalVal");

        tbody.innerHTML = "";

        if (data.length === 0) {
            vacia.style.display = "block";
            totalArt.textContent   = "0";
            subtotalEl.textContent = "$0.00";
            totalEl.textContent    = "$0.00";
            return;
        }

        vacia.style.display = "none";

        let totalArticulos = 0;
        let totalPrecio    = 0;

        data.forEach((item, i) => {
            const subtotal = item.precio * item.cantidad;
            totalArticulos += item.cantidad;
            totalPrecio    += subtotal;

            tbody.innerHTML += `
                <tr>
                    <td>${i + 1}</td>
                    <td><strong>${item.nombre}</strong></td>
                    <td style="color:#6b7a8d;font-size:12px;">${item.codigo}</td>
                    <td>$${item.precio.toFixed(2)}</td>
                    <td>
                        <div style="display:flex;align-items:center;gap:6px;">
                            <button class="btn btn-sm btn-secondary" onclick="cambiarCantidad('${item.codigo}', ${item.cantidad - 1})">−</button>
                            <span style="font-weight:600;min-width:20px;text-align:center;">${item.cantidad}</span>
                            <button class="btn btn-sm btn-secondary" onclick="cambiarCantidad('${item.codigo}', ${item.cantidad + 1})">+</button>
                        </div>
                    </td>
                    <td style="font-weight:600;">$${subtotal.toFixed(2)}</td>
                    <td><button class="btn btn-sm btn-danger" onclick="eliminar('${item.codigo}')">✕</button></td>
                </tr>
            `;
        });

        totalArt.textContent   = totalArticulos;
        subtotalEl.textContent = `$${totalPrecio.toFixed(2)}`;
        totalEl.textContent    = `$${totalPrecio.toFixed(2)}`;
    });
}

// ── Cambiar cantidad ─────────────────────────────────────
function cambiarCantidad(codigo, nuevaCantidad) {
    if (nuevaCantidad <= 0) {
        eliminar(codigo);
        return;
    }
    fetch("/cantidad", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo, cantidad: nuevaCantidad})
    }).then(() => cargarProductos());
}

// ── Eliminar producto ────────────────────────────────────
function eliminar(codigo) {
    fetch("/eliminar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo})
    }).then(() => cargarProductos());
}

// ── Limpiar ticket ───────────────────────────────────────
function limpiarLista() {
    fetch("/limpiar", {method: "POST"}).then(() => cargarProductos());
}

// ── Polling cada 1.5s (para actualizar desde el escáner) ─
setInterval(cargarProductos, 1500);
cargarProductos();