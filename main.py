from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
#codigo do post
@app.route("/", methods=['POST'])
def post():
 #valordopost = request.form['name do campo(tem que ser o name)']
  print("B")
if __name__ == '__main__':
  app.run(port=5000)

#implementar os algoritmos aqui
