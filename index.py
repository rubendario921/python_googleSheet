from flask import Flask, render_template

app = Flask(__name__)

#Pagina Principal
@app.route('/')
def home():
    return render_template('/python_googleSheet/view/home.html')

#Ejecutar Aplicacion
if __name__ == '__main__':    
    app.run(debug=True)