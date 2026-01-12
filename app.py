
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulador')
def simulador():
    return render_template('simulador.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/simular', methods=['POST'])
def simular():
    with open("data/dados.csv", 'r', encoding='utf-8') as arq:
        dados = arq.read().splitlines()
        option = request.form['material']
        valor = request.form['quantidade']

        valor_float= float(valor) if valor else 0
        for i in range(1, len(dados)):
            r = dados[i].split(';')
            if option == r[0]:
                energia_eco = valor_float * (float(r[4])/100)
                agua_eco = valor_float * (float(r[5])/100)
                co2_eco = valor_float * (float(r[6])/100)
                return render_template('simulador.html', quantidade=valor_float, material=option, energia_eco=energia_eco, agua_eco=agua_eco, co2_eco=co2_eco, energia_v=r[1], agua_v=r[2], co2_v=r[3])
    return render_template('simulador.html')

if __name__ == '__main__':
    app.run(debug=True)