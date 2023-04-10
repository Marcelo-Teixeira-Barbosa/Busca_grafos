import queue

class Node:
    
        
    id = -1
    pai = None
    custo = 0

    def __init__(self,id):
        self.id = id
 
    def __lt__(self, other):
        return self.custo < other.custo

class Grafo:
    h_value = []
    matriz = []
    n = 0
    direcionado = False
    heuristico = False
    ponderado = False
    
    def __init__(self,n,direcionado, heuristico, ponderado): 
        self.n = n
        self.direcionado = direcionado
        self.heuristico = heuristico
        self.ponderado= ponderado
        for i in range(n):
            self.matriz.append([0]*n)            
    
    def addAresta(self,s,t, pathValue):
        aux = pathValue
        if(not self.ponderado): aux = 1
        if(not self.direcionado):
            self.matriz[t][s]=aux
        self.matriz[s][t]=aux

    def add_H_Value(self, value):
        self.h_value = [0,0,0,0,0,0,0,0,0,0]
        if(self.heuristico):
            self.h_value= value


    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    
    def bl(self,s,t):
        q = queue.Queue()
        
        node = Node(s)
        node.pai = Node(-1)       
        
        q.put(node)
        
        while(not q.empty()):
            aux = q.get()
            print("aux: ", aux.id)
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos
        print("aux: ", aux.id)
        return aux
    
    def bp(self,s,t):
        q = queue.LifoQueue()
        
        node = Node(s)
        node.pai = Node(-1)       
        
        q.put(node)
        
        while(not q.empty()):
            aux = q.get()
            print("aux: ", aux.id)
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos
        print("aux: ", aux.id)
        return aux
    
    def bcu(self,s,t):
        pq = queue.PriorityQueue()
        
        node = Node(s)
        node.pai = Node(-1)
        node.custo = 0

        pq.put((node.custo, node))

        while not pq.empty():
            # Tirando o nó com menor custo da fila de prioridade
            # pattern matching
            # print(pq.queue)
            _, nodeAux = pq.get()
            print("node: %s custo %s" %(letras[nodeAux.id], nodeAux.custo))
            
            # Teste de Objetivo
            if nodeAux.id == t:
                return nodeAux
            # Teste de Objetivo
            
            # Expansão de vizinhos
            for i in range(self.n):
                # Verifica se o nó i é vizinho do nó atual e não sendo o pai
                if (self.matriz[nodeAux.id][i] != 0 and i != nodeAux.pai.id):
                    # Criando um nó vizinho e jogando na fila com seu peso
                    node = Node(i)
                    node.pai = nodeAux
                    node.custo = nodeAux.custo + self.matriz[nodeAux.id][i]
                    
                    pq.put((node.custo, node))
            # Expansão de vizinhos           
        return nodeAux
        
    def bme(self,s,t):

        q = queue.Queue()
        
        node = Node(s)
        node.pai = Node(-1)       
        
        value_list = []
        open_list=[]
        
        q.put(node)

        while(not q.empty()):
            aux = q.get()
            print("aux: %s valor: %s" % (aux.id, self.h_value[aux.id]) )
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
           
            # teste menor valor heuristico      
            for i in range(self.n):    
                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    print("%s : %s " %(letras[i],self.h_value[i]),end=' ')
                    value_list.append(self.h_value[i])
                    open_list.append(i)

            # Expansão de vizinhos
            menor_F = min(value_list)
            expand_node = open_list[value_list.index(menor_F)]
            print("menor valor:", letras[expand_node], end=" ")
            print()
            node = Node(expand_node)
            node.pai = aux
            q.put(node)
            value_list = []
            open_list = []
           
        #print("aux: ", aux.id)
        return aux
    
    def bas(self,s,t):

        q = queue.Queue()
        
        node = Node(s)
        node.pai = Node(-1)       
        
        value_list = []
        open_list=[]
        
        q.put(node)
        path_value = 0

        while(not q.empty()):
            aux = q.get()
            print("aux: %s value: %s" % (aux.id, self.h_value[aux.id]) )
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
           
            # teste menor valor heuristico      
            for i in range(self.n):    
                
                if(self.matriz[aux.id][i] >= 1 and i != aux.pai.id):
                    print("%s : %s " %(letras[i],self.matriz[aux.id][i] + self.h_value[i]),end=' ')
                    value_list.append(self.matriz[aux.id][i] + self.h_value[i])
                    open_list.append(i)

            # Expansão de vizinhos
            menor_F = min(value_list)
            expand_node = open_list[value_list.index(menor_F)]
            print("menor valor:", letras[expand_node], end=" ")
            path_value += self.matriz[aux.id][expand_node]
            print("path value: ", path_value)
            node = Node(expand_node)
            node.pai = aux
            q.put(node)
            value_list = []
            open_list = []
           
        #print("aux: ", aux.id)
        return aux
    
# configuração do grafo (direcionado, heuristico, ponderado)
g = Grafo(10,False, True, True)

##g.printMatriz()

#add aresta (origem, destino, custo)
g.addAresta(0, 1, 6)
g.addAresta(0, 5, 3)
g.addAresta(1, 3, 2)
g.addAresta(1, 2, 3)
g.addAresta(2, 3, 1)
g.addAresta(2, 4, 5)
g.addAresta(3, 4, 8)
g.addAresta(4, 8, 5)
g.addAresta(4, 9, 5)
g.addAresta(5, 6, 1)
g.addAresta(5, 7, 7)
g.addAresta(6, 8, 3)
g.addAresta(7, 8, 2)
g.addAresta(8, 9, 3)

#heuri_pos:   [0,1,2,3,4,5,6,7,8,9]
g.add_H_Value([10,8,5,7,3,6,5,3,1,0])
g.printMatriz()

m = queue.Queue()

letras = ['A','B','C','D','E','F','G','H','I','J']
objetivo = g.bas(0, 9)
   
while(objetivo.id != -1):
    print(letras[objetivo.id],end = ' ')
    objetivo = objetivo.pai



"""

busca em largura (BFS) > ok

busca em profundidade (DFS) > ok

busca de custo uniforme (DIJKSTRA) > 

busca de melhor escolha (INFORMED SEARCH) > ok

busca estrela (A* SEARCH) > ok

"""