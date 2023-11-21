import os
import platform
import subprocess

LIBRERIAS_NECESARIAS = ['folium', 'Flask']
OS = platform.system()


# Crear Entorno Virtual
print('[i] Verificando Entorno Virtual')
subprocess.run('python -m venv $PWD')
if OS == 'Linux' or OS == 'Darwin':
    subprocess.run('source ./bin/activate')


librerias_sistema = os.popen("python -m pip list --path ./include").read()
librerias_sistema = ''.join(librerias_sistema.splitlines()[2:])

librerias_instalar = ''
for lib in LIBRERIAS_NECESARIAS:
    if lib not in librerias_sistema:
        librerias_instalar += f' {lib}'
if len(librerias_instalar) != 0:
    os.system(f"python -m pip install {librerias_instalar} --isolated --target ./include")
