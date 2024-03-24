from flask import Blueprint, render_template, url_for


routes = Blueprint('route', __name__)

@routes.route('/')
def home():
    
    return render_template('index.html')

@routes.route('/cardapio')
def cardapio():
    
    return render_template('cardapio.html')

@routes.route('/suceso')
def sucesso():

    return render_template('sucesso.html')
