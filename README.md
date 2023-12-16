# Sombras Proyecto

## Manual de Instalación
1. Clonar el repositorio:
```sh
git clone https://github.com/Cristobal-Camisa-Cuadro/Sombras
```
o descargar el archivo zip desde `https://github.com/Cristobal-Camisa-Cuadro/Sombras`,
apretando el boton 'Code' > 'Download ZIP', y extraer la carpeta `Sombra-main`.

2. Cambiar al directorio `cd Sombras` , o abrir una terminal/powershell en el directorio
`Sombra-main`.
2. Crear Entorno Virtual:
```sh
python -m venv $PWD
```
3. Ejecutar Entorno Virtual:
- Linux, MacOS (Bash):
```sh
source ./bin/activate
```
- Windows (PowerShell):
```powershell
source ./Scripts/Activate.ps1
```
3. Instalar Librerias:
```sh
python -m pip install -r requirements.txt
```
4. Ejecutar Servidor:
```sh
python ./src/server.py
```

## Manual de Uso

1. Visualizar la Pagina en `http://127.0.0.1:5000`
2. Hacer click en el mapa.
3. Listo!
