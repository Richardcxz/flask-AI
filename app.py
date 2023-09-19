from flask import Flask,render_template,request,jsonify
from calculorota import Gera_Problema,pegardestino
app = Flask(__name__)


@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
    origem = request.form['origen']
    destino = request.form['destinon']
    Gera_Problema("rotas.txt")
    pegardestino(origem,destino)
    print(origem,destino)
    a = pegardestino(origem,destino)
    print(a)
    return render_template("index.html",resultado=a)

    

  
   
if __name__ == "__main__":
    app.run()


