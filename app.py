from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
    origem = request.form['origen']
    destino = request.form['destinon']
    print(origem,destino)
    return render_template("index.html")

    

  
   
if __name__ == "__main__":
    app.run()

def gerarTudo(inicio,fim):
    print(inicio,fim)
    #codigos aqui