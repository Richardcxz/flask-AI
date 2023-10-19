from flask import Flask,render_template,request,jsonify
from calculorota import Gera_Problema,pegardestino
from greedyABusca import iniciar
app = Flask(__name__)


@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
    origem = request.form['origen']
    destino = request.form['destinon']
    a = iniciar(origem,destino)
    print(a)
    return render_template("index.html",resultado=a)

    

  
   
if __name__ == "__main__":
    app.run()


