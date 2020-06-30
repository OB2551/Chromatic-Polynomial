import copy
import sympy as sym
import itertools
GE = 0
import sys
import numpy as np
x = 100000

sys.setrecursionlimit(x)

class Graphs(object):
       
    V = 0
    
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adj = []
        
    def __copy__(self):
        return 
        
    def addEdge(self, x):
        self.edges.append(x)
    
    def setEdges(self, x):
        self.edges = x
        
    def setVertices(self, v):
        self.vertices = v
        
        
    def removeEdge(self, x):
        self.edges.remove(x)
    
    def addVertex(self, v):
        self.vertices.append(v)
        
    def removeVertex(self, v):
        self.vertices.remove(v)
        
    def getEdges(self):
        return self.edges
    
    def getVertices(self):
        return self.vertices
    
   
    

               
    
    def DFS(self, v, visited): 
   
        # Mark the current node as  
        # visited and print it  
        visited[v] = True
      
        # Recur for all the vertices  
        # adjacent to this vertex 
        i = 0
        while i < len(self.adj[v]): 
            if (not visited[self.adj[v][i]]):  
                self.DFS(self.adj[v][i], visited) 
            i += 1
      
    # Returns true if given graph is  
    # connected, else false  
    def isConnected(self): 
        V = len(self.vertices)
        self.adj = [[] for i in range(V)]
        s = 0
        Dict = {}
        for i in self.vertices:
            Dict[i] = s
            s+=1
        newEdges = []
        for x,y in self.edges:
            newEdges.append([Dict[x], Dict[y]])
        for a,b in newEdges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        visited = [False] *V
      
        # Find all reachable vertices  
        # from first vertex  
        self.DFS(0, visited)  
      
        # If set of reachable vertices  
        # includes all, return true. 
        for i in range(1, V): 
            if (visited[i] == False):  
                return False
      
        return True
    
    
    
    
    
    def isConnected2(self): 
        V = len(self.vertices)
      
        visited = [False] *V
      
        # Find all reachable vertices  
        # from first vertex  
        self.DFS(0, visited)  
      
        # If set of reachable vertices  
        # includes all, return true. 
        for i in range(1, V): 
            if (visited[i] == False):  
                return False
      
        return True
    
   
    def reLabel(self):
        V = len(self.vertices)
        self.adj = [[] for i in range(V)]
        s = 0
        Dict = {}
        for i in self.vertices:
            Dict[i] = s
            s+=1
        newEdges = []
        for x,y in self.edges:
            newEdges.append([Dict[x], Dict[y]])
        for a,b in newEdges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        return Dict
    
    
    def isBridge(self, e): 
        g = copy.deepcopy(self)
        Dict = g.reLabel()
        
        v = Dict[e[0]]
        u = Dict[e[1]]
        # Remove edge from undirected graph 
        
        indU = g.adj[v].index(u) 
        indV = g.adj[u].index(v) 
        del g.adj[u][indV]  
        del g.adj[v][indU]  
        
        res = g.isConnected2()  
      
        # Adding the edge back  
         
      
        # Return true if graph becomes  
        # disconnected after removing  
        # the edge.  
        return (res == False) 
    
    
    
    
    
    
    
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
        
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 

  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        
        V = len(self.vertices)
        visited = [] 
        cc = [] 
        for i in range(V): 
            visited.append(False) 
        for v in range(V): 
            
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        CC = []
        for x in cc:
            newlist = [a+1 for a in x]
            CC.append(newlist)
     
        return CC
    
    
    def subGraphs(self):
        g1 = copy.deepcopy(self)
        subgraphs = []
        components = g1.connectedComponents()
        for x in components:
            g = Graphs()
            g.setVertices([i for i in x])
            g.setEdges(g1.findEdges(x))
            
            subgraphs.append(g)
        return subgraphs
    
    def findEdges(self,x):
        newEdges = []
        combinations =  list(itertools.combinations(x, 2))
        
        for e in self.edges:
            if e in combinations:
                newEdges.append(e)
               
            if (e[1], e[0]) in combinations:
                newEdges.append(e)
        return newEdges
                
    
    
    
        
    def amalgamate(self, e):
        V = max(i for i in e)
        v = min(i for i in e)
        self.vertices.remove(V)
        self.edges = list(set_reduce(find_and_replace(V, v, self.edges)))
                
                
    def degree(self, v):
         i = 0 
         for e in self.edges:
             if v in e:
                 i +=1
         return i
     
    
    def findEdgetoRemove(self):
        for e in self.edges:
            if self.isBridge(e) ==False:
                return e
        

        
    def isTree(self):
        return self.isConnected() and len(self.edges)+1 == len(self.vertices)
    
    
    
    
    def chromaticTree(self):
        s = sym.symbols('k')
        expr = (s*(s-1)**(len(self.vertices)-1))
        return expr
    
    def complete(self):
        if len(self.edges) == len(list(itertools.combinations(self.vertices, 2))):
            return True
        else:
            return False
    
    def chromaticPol(self):
       
       
       if self.isConnected():
               
          if self.isTree():
            return self.chromaticTree()
          else:
          
            g1 = copy.deepcopy(self)
            g2 = copy.deepcopy(self)
            i = self.findEdgetoRemove()
            #i1 = self.isValidtoRemove()
            
            g1.removeEdge(i)
            g2.amalgamate(i)
        
            return g1.chromaticPol() - g2.chromaticPol()
       else:
          g3 = copy.deepcopy(self)
          subgraphs = g3.subGraphs()
          chroms = [x.chromaticPol() for x in subgraphs]
          return np.prod(np.array(chroms))
       
    def chromaticPoly(self):
      
       return(sym.expand(self.chromaticPol()))
       
       
    def chi(self, expr):
        for i in self.vertices:
            if expr.subs(sym.symbols('k'), i) !=0:
                return i
        

def set_reduce(pairs):
    new_pairs = set([])
    for x,y in pairs:
        if x < y:
            new_pairs.add((x,y))
        else:
            new_pairs.add((y,x))
    return new_pairs       


def find_and_replace(V, v, Edges):
    edgesToRemove = []
   
    for E in Edges:
          if V in E:
            x = list(E)
            x.remove(V)
            x.append(v)
            edgesToRemove.append(E)
            Edges.append(tuple(x))
  
        
    s = set(Edges)-set(edgesToRemove)
    Edges = list(s)
    for E in Edges:
        if E[0] == E[1]:
            Edges.remove(E)
    return Edges