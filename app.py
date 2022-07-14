from flask import Flask, request, g, redirect, url_for, render_template, flash, session #Importa las librerías que usaré

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/reserva_success', methods = ['GET', 'POST'])
def reserva_success():
    correo = request.form['correo']
    codSeguridad = request.form['codSeguridad']
    numTarjeta = request.form['numTarjeta']
    fecha = request.form['fecha']
    numPersonas = request.form['numPersonas']

    return redirect(url_for('index'))


app.run(debug=True, use_debugger=False, use_reloader=False)