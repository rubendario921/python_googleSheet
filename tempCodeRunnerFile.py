from flask import Flask

app = Flask(__name__)

#Pagina Principal
@app.route('/')
def home():
    return 'Hola Mundo'

app.route('/about')
def about():
    return 'About Page'

#Ejecutar Aplicacion
if __name__ == '__main__':
    
    app.run(debug=True)