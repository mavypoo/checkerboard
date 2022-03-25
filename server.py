from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')     
def index():
    return render_template("index.html", row=8, col=8, color1 = 'blue' , color2='yellow')  

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color1 = 'blue' , color2='yellow')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html", row=x, col=y, color1 = 'blue' , color2='yellow')

@app.route('/<int:x>/<int:y>/<one>')
def row_col1(x,y,one):
    return render_template("index.html", row=x, col=y, color1=one , color2='yellow')

@app.route('/<int:x>/<int:y>/<one>/<two>')
def row_col_two(x,y,one,two):
    return render_template("index.html", row=x, col=y, color1=one , color2=two)

if __name__=="__main__":      
    app.run(debug=True)    