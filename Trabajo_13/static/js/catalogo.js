let modoEdicion  = false;
let codigoEditando = null;
let todosCatalogo  = [];

// ── Cargar tabla ─────────────────────────────────────────
function cargarCatalogo() {
    fetch("/catalogo/lista")
    .then(r => r.json())
    .then(data => {
        todosCatalogo = data;
        renderTabla(data);
    });
}

function renderTabla(data) {
    const tbody = document.getElementById("tablaCatalogo");
    const vacio = document.getElementById("catalogoVacio");
    tbody.innerHTML = "";

    if (data.length === 0) {
        vacio.style.display = "block";
        return;
    }

    vacio.style.display = "none";

    data.forEach(p => {
        tbody.innerHTML += `
            <tr>
                <td style="font-size:12px;color:#6b7a8d;">${p.codigo}</td>
                <td><strong>${p.nombre}</strong></td>
                <td style="font-weight:600;">$${parseFloat(p.precio).toFixed(2)}</td>
                <td>
                    <div style="display:flex;gap:6px;">
                        <button class="btn btn-sm btn-warning" onclick="editarProducto('${p.codigo}', '${p.nombre.replace(/'/g,"\\'")}', ${p.precio})">✏ Editar</button>
                        <button class="btn btn-sm btn-danger"  onclick="eliminarProducto('${p.codigo}')">✕ Eliminar</button>
                    </div>
                </td>
            </tr>
        `;
    });
}

// ── Filtro de búsqueda ───────────────────────────────────
function filtrarTabla() {
    const q = document.getElementById("buscador").value.toLowerCase();
    const filtrados = todosCatalogo.filter(p =>
        p.nombre.toLowerCase().includes(q) || p.codigo.toLowerCase().includes(q)
    );
    renderTabla(filtrados);
}

// ── Guardar (agregar o editar) ───────────────────────────
function guardarProducto() {
    const codigo = document.getElementById("fCodigo").value.trim();
    const nombre = document.getElementById("fNombre").value.trim();
    const precio = document.getElementById("fPrecio").value.trim();

    if (!codigo || !nombre || !precio) {
        mostrarMsg("Completa todos los campos.", "error");
        return;
    }

    const endpoint = modoEdicion ? "/catalogo/editar" : "/catalogo/agregar";

    fetch(endpoint, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo, nombre, precio: parseFloat(precio)})
    })
    .then(r => r.json())
    .then(data => {
        if (data.ok) {
            mostrarMsg(modoEdicion ? "Producto actualizado." : "Producto agregado.", "ok");
            limpiarForm();
            cargarCatalogo();
        } else {
            mostrarMsg(data.error || "Error al guardar.", "error");
        }
    });
}

// ── Editar: prellenar form ───────────────────────────────
function editarProducto(codigo, nombre, precio) {
    modoEdicion    = true;
    codigoEditando = codigo;

    document.getElementById("fCodigo").value  = codigo;
    document.getElementById("fCodigo").readOnly = true;   // no cambiar el código
    document.getElementById("fNombre").value  = nombre;
    document.getElementById("fPrecio").value  = precio;

    document.getElementById("formTitulo").textContent = "✏ Editar producto";
    document.getElementById("btnCancelar").style.display = "inline-block";

    document.getElementById("fNombre").focus();
    window.scrollTo({top: 0, behavior: "smooth"});
}

// ── Cancelar edición ─────────────────────────────────────
function cancelarEdicion() {
    limpiarForm();
}

function limpiarForm() {
    modoEdicion    = false;
    codigoEditando = null;

    document.getElementById("fCodigo").value  = "";
    document.getElementById("fCodigo").readOnly = false;
    document.getElementById("fNombre").value  = "";
    document.getElementById("fPrecio").value  = "";

    document.getElementById("formTitulo").textContent = "Agregar producto";
    document.getElementById("btnCancelar").style.display = "none";
    ocultarMsg();
}

// ── Eliminar producto ────────────────────────────────────
function eliminarProducto(codigo) {
    if (!confirm(`¿Eliminar el producto con código ${codigo}?`)) return;

    fetch("/catalogo/eliminar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo})
    })
    .then(r => r.json())
    .then(() => cargarCatalogo());
}

// ── Mensajes ─────────────────────────────────────────────
function mostrarMsg(texto, tipo) {
    const el = document.getElementById("formMsg");
    el.textContent     = texto;
    el.className       = "form-msg " + tipo;
    el.style.display   = "block";
    setTimeout(ocultarMsg, 3000);
}

function ocultarMsg() {
    const el = document.getElementById("formMsg");
    el.style.display = "none";
}

// ── Enter en formulario ──────────────────────────────────
["fCodigo","fNombre","fPrecio"].forEach(id => {
    document.getElementById(id).addEventListener("keydown", e => {
        if (e.key === "Enter") guardarProducto();
    });
});

// ── Iniciar ──────────────────────────────────────────────
cargarCatalogo();