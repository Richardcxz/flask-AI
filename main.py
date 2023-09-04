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

class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, anterior=None, 
                       proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, ni, p):
        novo_no = No(p, st, ni, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, ni, p):

        novo_no = No(p, st, ni, None, None)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
            self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head
    
    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.nivel)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
            
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

class busca(object):

    # BUSCA EM AMPLITUDE
    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            
            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in grafo[ind][::1]:

                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    # BUSCA EM PROFUNDIDADE
    def profundidade(self, inicio, fim):

        # manipular a PILHA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            
            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            #for novo in grafo[ind][::-1]:
            for novo in grafo[ind][::]:

                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"
    
    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self, inicio, fim, limite):

        # manipular a PILHA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            
            if atual.nivel<limite:
                ind = nos.index(atual.estado)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in grafo[ind][::-1]:
    
                    # pressuponho que não foi visitado
                    flag = True
    
                    # controle de nós repetidos
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("\nFila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"
    
    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self, inicio, fim, lim_max):
        
        for limite in range(1,lim_max):
            # manipular a PILHA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio() == False:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                
                if atual.nivel<limite:
                    ind = nos.index(atual.estado)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in grafo[ind][::-1]:
        
                        # pressuponho que não foi visitado
                        flag = True
        
                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.nivel+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.nivel+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.nivel + 1, atual)
                            l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("\nFila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho

        return "caminho não encontrado"

        
    # BUSCA BIDIRECIONAL
    def bidirecional(self, inicio, fim):
    
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        
        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l4 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
    
    
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.primeiro().nivel:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in grafo[ind]:
        
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            if visitado1[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado1[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==novo:
                                flag = True
                                break
                        
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.primeiro().nivel:
                    break
                
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in grafo[ind]:
        
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            if visitado2[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado2[j][1]=atual.nivel+1
                            break
                        
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==novo:
                                flag = True
                                break
                            
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"

def Gera_Problema(JSON):
    #f = open(arquivojsoncomosvaloresdolaibriiton.JSON)
    print('2')
nos, grafo = Gera_Problema("algumbagulhoemjsoncomosvaloresdolabirinto.json")    
