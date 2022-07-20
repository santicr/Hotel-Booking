from audioop import add
from flask import Flask, request, g, redirect, url_for, render_template, flash, session #Importa las librerías que usaré
import uuid

app = Flask(__name__)
nombres_hoteles = ['Intercontinental', 'Ibis', 'Airto', 'Sant']

def confirm_data(datosUsuario):
    file = open("datos.txt", "r")
    lineas = file.readlines()
    flag = True

    for linea in lineas:
        datos = linea.split()
        flag = True
        for i in range(len(datos)):
            if datos[i] != datosUsuario[i]:
                flag = False
        if flag:
            return True

    file.close()
    return False

def add_reserva(datosUsuario):
    f = open("reservas.txt", "a")
    datos_tam = len(datosUsuario)

    if datos_tam == 1 and datosUsuario[0] != 'tried':
        f.write(datosUsuario[0] + ' ')
    elif datos_tam == 1 and datosUsuario[0] == 'tried':
        f.write('tried\n')
    else:
        for i in range(datos_tam):
            f.write(datosUsuario[i] + ' ')
        f.write('\n')
    f.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserva<int:reserva_id>', methods = ['GET'])
def reserva(reserva_id):
    num = reserva_id - 1
    return render_template('reserva.html', num = num)

@app.route('/reserva_success/<var>', methods = ['GET', 'POST'])
def reserva_success(var):
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    codSeguridad = request.form['codSeguridad']
    numTarjeta = request.form['numTarjeta']
    fecha = request.form['fecha']
    numPersonas = request.form['numPersonas']
    path = request.path
    apellidos = apellidos.split()
    apellido1, apellido2 = apellidos[0], apellidos[1]
    datosUsuario = [nombre, apellido1, apellido2, numTarjeta, codSeguridad]
    datosReserva = [nombres_hoteles[int(var)], nombre, apellido1, apellido2, fecha, numPersonas, str(uuid.uuid1())]

    if not confirm_data(datosUsuario):
        return redirect(url_for('reserva_error'))

    add_reserva(datosReserva)

    return redirect(url_for('index'))

@app.route('/request_reserva', methods = ['GET', 'POST'])
def request_reserva():
    uuid = request.form['uuid']
    f = open("reservas.txt", 'r')
    lineas = f.readlines()
    for linea in lineas:
        datos = linea.split()
        if datos[6] == uuid:
            f.close()
            return render_template('reserva_gestion.html', datos = datos)
    f.close()
    return redirect(url_for('reserva_error'))

@app.route('/reserva_error')
def reserva_error():
    return render_template('error.html')

app.run(debug = True)