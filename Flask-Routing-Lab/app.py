from flask import Flask, redirect, request, render_template, url_for


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/product')
def pro():
    return render_template('product.html')

@app.route('/cookies')
def cook():
    return render_template('cookie.html')

@app.route('/cakes')
def cake():
    return render_template('cake.html')

@app.route('/cupcakes')
def cup():
    return render_template('cupcake.html')

@app.route('/pies')
def pie():
    return render_template('pie.html')

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
