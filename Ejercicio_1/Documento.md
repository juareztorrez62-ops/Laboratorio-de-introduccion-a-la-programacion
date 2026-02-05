# 🐍 Guía paso a paso para crear un entorno virtual en Python (Windows + VS Code)
Esta guía explica detalladamente cómo crear, activar y utilizar un entorno virtual en Python usando el módulo venv, trabajando en Windows con PowerShell y Visual Studio Code.
## 📌 ¿Qué es un entorno virtual?
Un entorno virtual es un espacio aislado donde se instalan las librerías necesarias para un proyecto específico, sin afectar la instalación global de Python ni otros proyectos. Esto evita conflictos entre versiones de paquetes y mantiene el entorno de trabajo organizado.
## 🧱 1. Abrir el proyecto en Visual Studio Code
1. Abre Visual Studio Code.
2. Ve a File → Open Folder.
3. Selecciona la carpeta del proyecto donde trabajarás (por ejemplo: Ejercicio_1).
Abrir la carpeta del proyecto es importante para que el entorno virtual se cree dentro de ella y quede asociado correctamente.
## 🧾 2. Abrir la terminal integrada
Dentro de Visual Studio Code, abre la terminal integrada presionando:
Ctrl + ñ
(O Ctrl + ` dependiendo del teclado).
Verifica que la terminal esté usando PowerShell.
## 🟢 3. Crear el entorno virtual
En la terminal escribe el siguiente comando y presiona Enter:
py -3 -m venv env
Este comando utiliza Python 3, ejecuta el módulo venv y crea una carpeta llamada env que contendrá el entorno virtual.
## 🟡 4. Activar el entorno virtual
En PowerShell ejecuta:
.\env\Scripts\Activate.ps1
Si el entorno se activa correctamente, la terminal mostrará (env) al inicio de la línea.
## ⚠️ 5. Error común: ejecución de scripts deshabilitada
Si PowerShell bloquea la activación del entorno, ejecuta una sola vez:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Después vuelve a activar el entorno con:
.\env\Scripts\Activate.ps1
## ✅ 6. Verificar que el entorno está activo
Puedes verificarlo ejecutando:
python --version
O también:
where python
La ruta debe apuntar a env\Scripts\python.exe.
## 📦 7. Instalar librerías dentro del entorno
Con el entorno activo, instala paquetes usando pip:
pip install requests
Las librerías se instalarán únicamente dentro del entorno virtual.
## 🔄 8. Desactivar el entorno virtual
Cuando termines de trabajar, ejecuta:
deactivate
Esto desactiva el entorno virtual y regresa al Python global.
## 🐍 9. Configurar el intérprete de Python en VS Code
1. Presiona Ctrl + Shift + P.
2. Escribe Python: Select Interpreter.
3. Selecciona el intérprete que diga Python 3.x (env).
Esto asegura que VS Code use el entorno virtual al ejecutar los archivos .py.
## 📝 10. Resumen de comandos importantes
py -3 -m venv env
.\env\Scripts\Activate.ps1
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
pip install nombre_paquete
deactivate
## 📌 Recomendaciones importantes
No subir la carpeta env al repositorio.
Agregar env al archivo .gitignore.
Para compartir dependencias, generar:
pip freeze > requirements.txt
Y reinstalarlas con:
pip install -r requirements.txt
## ✅ Conclusión
El uso de entornos virtuales es una práctica fundamental en Python 
que permite mantener proyectos organizados, evitar conflictos de 
dependencias y trabajar de forma profesional.
El uso de entornos virtuales es una práctica fundamental en Python que permite mantener proyectos organizados, evitar conflictos de dependencias y trabajar de forma profesional.

