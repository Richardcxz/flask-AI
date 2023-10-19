import numpy as np
import random as rd

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        # controle da árvore de busca
        self.pai       = pai
        # indica o nó do grafo
        self.estado    = estado
        # função de avaliação f(n) do método
        self.valor1    = valor1        
        # custo do caminho da origem até o nó atual
        self.valor2    = valor2     
        # controle da lista encadeada
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


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

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):
    
    def custo_uniforme(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                print("---- Custo uniforme ------")
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                print("Cópia da árvore:\n",l2.exibeLista())
                print("\nÁrvore de busca Custo uniforme:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    def greedy(self, inicio, fim):
        
        ind_f = nos.index(fim) 
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                print("--------------Greeedy--------------")
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = h[ind_f][ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      


    def a_estrela(self, inicio, fim):
        
        ind_f = nos.index(fim)
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                print("------A*--------")
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 + h[ind_f][ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

    def aia_estrela(self, inicio, fim, limite):
        
        ind_f = nos.index(fim)
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            #print("Limite: ",limite)
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
    
                    return caminho, atual.valor2
            
                ind = nos.index(atual.estado)
                for novo in grafo[ind]:
                    
                    ind1 = nos.index(novo[0])
                    
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[1]  # custo do caminho
                    v1 = v2 + h[ind_f][ind1] # f2(n)
    
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo[0]:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(novo[0], v1 , v2, atual)
                            l2.inserePos_X(novo[0], v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(novo[0])
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
            limite = sum(lim_exc)/len(lim_exc)
                    
        return "Caminho não encontrado"
    
def gera_H(n):
    aux = busca()
    h = np.zeros((n,n),int)
    i = 0
    for no_origem in nos:
        j = 0
        for no_destino in nos:
            if no_origem != no_destino:
                print(no_origem)
                print(no_destino)
                cm = []
                v  = aux.custo_uniforme(no_origem, no_destino)
                if "Caminho não encontrado" not in v:
                    print(v[1])
                    h[i][j] = v[1]*rd.uniform(0,1)
            j += 1
        i += 1
    return h

nos = ['rua1', 'rua2', 'rua3', 'rua4', 'rua5', 'rua6', 'rua7', 'rua8', 'rua9', 'rua10', 'rua11', 'rua12', 
      'rua13', 'rua14', 'rua15', 'rua16', 'rua17', 'rua18', 'rua19', 'rua20', 'rua21', 'rua22', 'rua23', 
       'rua24', 'rua25', 'rua26', 'rua27', 'rua28', 'rua29', 'rua30', 'rua31', 'rua32', 'rua33', 'rua34', 
       'rua35', 'rua36', 'rua37', 'rua38', 'rua39', 'rua40', 'rua41', 'rua42', 'rua43','avenidaA','avenidaB',
       'avenidaC','avenidaD','avenidaE','avenidaF','cruzamentoA','cruzamentoB','viaA','viaB','rotatoriaA']

grafo = [[['rua2',2],['rua3',2],['rua4',3],['rua5',3],['rua6',3],['rua7',3],['rua10',4],['rua9',5]],
        [['avenidaF',1],['rua1',1]],
        [['rua1',1],['avenidaB',1]],
        [['avenidaF',1],['rua1',1]],
        [['rua1',1],['avenidaB',1]],
        [['avenidaF',1],['rua1',1]],
        [['rua1',1],['avenidaB',1],['rua8',2]],
         [['rua7',1],['rua9',2]],
         [['avenidaF',1],['cruzamentoB',2],['rua8',3]],
         [['avenidaF',1],['rua1',1]],
         [['rua13',3],['avenidaF',1]],
         [['rua13',1],['avenidaF',1]],
         [['rua12',4],['rua11',5],['viaA',3],['avenidaA',1]],
         [['viaA',1],['viaB',1]],
         [['rua22',1],['rua19',6],['rua20',7],['viaB',8]],
         [['rua22',1],['rua17',3],['rua18',4],['rua19',5]],
         [['rua23',3],['rua16',1]],
         [['rua16',1],['rua21',3],['rotatoriaA',4]],
         [['rua21',3],['rua26',4],['rua16',2],['rua15',1]],
         [['rua15',1],['rua21',4],['rua26',6]],
         [['rua18',1],['rua19',2],['rua20',3]],
         [['rua23',1],['rua16',5],['rua15',6],['rua24',8]],
         [['rua22',1],['rua17',2],['rotatoriaA',1]],
         [['rua22',1],['avenidaA',5]],
         [['rotatoriaA',1],['avenidaC',3]],
         [['rotatoriaA',1],['rua19',1],['rua20',2],['avenidaC',4]],
         [['rotatoriaA',1],['avenidaC',2],['avenidaD',3],['avenidaE',5]],
         [['avenidaD',1],['avenidaE',1]],
         [['avenidaE',1],['rua30',2]],
         [['rua29',1],['rua32',1]],
         [['avenidaC',1],['avenidaD',1]],
         [['avenidaD',1],['avenidaE',1],['rua30',2]],
         [['rua32',1],['rua35',1],['avenidaF',7]],
         [['avenidaC',1],['avenidaD',1]],
         [['avenidaD',1],['avenidaE',1],['rua33',3]],
         [['avenidaF',1],['rua41',3]],
         [['avenidaF',1],['rua40',2]],
         [['avenidaF',1],['cruzamentoB',1],['rua43',6]],
         [['rua36',1],['rua42',1]],
         [['rua38',1],['rua37',1]],
         [['rua36',1],['rua37',1]],
         [['avenidaF',1],['rua41',2],['rua43',3]],
         [['avenidaB',1],['rua37',1],['rua36',3],['rua42',3]],
         [['rua24',1],['cruzamentoA',2],['rua13',2],['rua1',5],['avenidaB',8]],
         [['avenidaA',1],['rua3',1],['rua5',2],['rua7',3],['rua43',10]],
         [['rua27',1],['rua25',2],['rua26',3],['viaB',3],['viaA',7],['rua31',7],['rua34',8]],
         [['rua27',1],['rua28',4],['rua32',5],['rua35',6],['avenidaF',10]],
         [['rua27',1],['rua28',2],['rua29',2],['rua32',3],['rua34',5],['avenidaF',12]],
         [['rua2',1],['rua4',2],['rua6',3],['rua10',4],['rua12',4],['rua11',5],['rua9',5],['rua38',7],['rua37',8],['rua36',9],['rua37',10]],
         [['rua14',1],['rua24',3]],
         [['rua8',2],['rua38',1]],
         [['avenidaC',1],['rua14',6],['rua13',9]],
         [['rua26',1],['avenidaC',1],['rua14',6]],
         [['rua23',1],['rua18',2],['rua26',3],['rua25',2],['rua27',3]]
] 
h = gera_H(len(nos))
def iniciar(inicio,final):
    sol = busca()
        
    caminho = []
    
    cu,valorcu = sol.custo_uniforme(inicio,final)
    ce,valorce = sol.a_estrela(inicio,final)
    gre,valorgre = sol.greedy(inicio,final)
    a = ""+' '.join(map(str,cu))+","+str(valorcu)
    p = ""+' '.join(map(str,ce))+","+str(valorce)
    pl = ""+' '.join(map(str,gre))+","+str(valorgre)
    
    return a+"/"+p+"/"+pl


