# Sombras Proyecto

## Manual de Instalación
1. Clonar el repositorio:
```sh
git clone https://github.com/Cristobal-Camisa-Cuadro/Sombras
```
o descargar el archivo zip desde `https://github.com/Cristobal-Camisa-Cuadro/Sombras`,
apretando el boton verde 'Code' > 'Download ZIP', y extraer la carpeta `Sombra-main`.

2. Cambiar al directorio `cd Sombras` , o abrir una terminal/powershell en el directorio (apretar el boton shift y dar click derecho en la carpeta,
luego seleccionar 'Abrir la ventana de PowerShell aquí')
`Sombra-main`.
(Opcional) Crear Entorno Virtual, esto permite contener las librerias en el directorio, y no de forma global:
```sh
python -m venv .venv
```
- Ejecutar Entorno Virtual:
Linux, MacOS (Bash):
```sh
source ./.venv/bin/activate
```
Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
3. Instalar Librerias:
```sh
python -m pip install -r requirements.txt
```

## Manual de Uso
1. Ejecutar Servidor:
```sh
python ./src/server.py
```
2. Visualizar la Pagina en `http://127.0.0.1:5000`
3. Hacer click en el mapa.
4. Listo!

Notar:
- Si sale del rango de la Universidad y quiere volver, recargue la pagina.
