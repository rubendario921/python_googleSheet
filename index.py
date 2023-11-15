from flask import Flask, render_template


app = Flask(__name__)

#Pagina Principal
@app.route('/')
def home():
    return render_template('/register_in_google_sheets/view/home.html')

app.route('/about')
def about():
    return 'About Page'

#Ejecutar Aplicacion
if __name__ == '__main__':
    
    app.run(debug=True)