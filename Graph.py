#  File: Graph.py

#  Description: Implementing various functions for graph

#  Student Name: Rakshana Govindarajan

#  Student UT EID: rg38236

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 7 May 2016

#  Date Last Modified: 9 May 2016

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited 

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)


class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return(self.weight < other.weight)

  def __le__ (self, other):
    return(self.weight <= other.weight)

  def __gt__ (self, other):
    return(self.weight > other.weight)

  def __ge__ (self, other):
    return(self.weight >= other.weight)

  def __eq__ (self, other):
    return(self.weight == other.weight)

  def __ne__ (self, other):
    return(self.weight != other.weight)

  


from collections import deque

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
    
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)


  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight


  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight


  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # does a depth first search in a graph
  # do depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)


  # does a breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # get index from vertex label
  def getIndex (self, label):
    # Traverses through vertices list and finds index of vertex that has a matching label to the one inputted
    for item in self.Vertices:
      if(item.label == label):
        index = self.Vertices.index(item)
    return index


  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    edges = []
    num_rows = len(self.adjMat)
    num_cols = len(self.adjMat[0])
    for i in range(num_rows):
      for j in range(num_cols):
        # Creating an edge using the from, to, and weights in the adjacency matrix where the weight is not 0
        edge = Edge(j, i, self.adjMat[i][j])
        edges.append(edge)

    for item in edges:
      if((item.u == fromVertexLabel) and (item.v == toVertexLabel)):
        if(item.weight != 0):
          return weight

        else:
          return -1

    return -1



  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    unvisited_neighbors = []
    neighbors = []
    nVert = len (self.Vertices)
    index = self.getIndex(vertexLabel)
    for i in range (nVert):
      if (self.adjMat[index][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        unvisited_neighbors.append(i)

    #return unvisited_neighbors

    for item in unvisited_neighbors:
      neighbors.append(item.getLabel())

    return neighbors


  # get a copy of the list of vertices
  def getVertices (self):
    vertices_copy = []
    for item in self.Vertices:
      vertices_copy.append(item)

    for item in vertices_copy:
      print(item.label)

  # determine if a directed graph has a cycle
  #def hasCycle (self):
       
  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    # Changing the adjMatrix value to 0 for that specific edge
    # If is undirected edge, resetting the value for both edges in matrix
    indexFrom = self.getIndex(fromVertexLabel)
    indexTo = self.getIndex(toVertexLabel)
    
    
    if(self.adjMat[indexFrom][indexTo] == self.adjMat[indexTo][indexFrom]):
      self.adjMat[indexFrom][indexTo] = 0
      self.adjMat[indexTo][indexFrom] = 0

    # If directed edge, then reset value for that particular directed edge
    else:
      self.adjMat[indexFrom][indexTo] = 0

   

    return("Removed edge from " + str(fromVertexLabel) + " to " + str(toVertexLabel))
    
    

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    for item in self.Vertices:
      if(item.label == vertexLabel):
        #self.Vertices.remove(item)
        index = self.getIndex(vertexLabel)
       
    # Removing row and column with that index
    for i in range(len(self.adjMat)):
      if(i == index):
        #print(self.adjMat[i])
        self.adjMat.remove(self.adjMat[i])

    for i in range(len(self.adjMat)):
      for j in range(len(self.adjMat[i])):
        if(j == index):
          
          self.adjMat[i].pop(j)


    for item in self.Vertices:
      if(item.label == vertexLabel):
        self.Vertices.remove(item)

    return("Removed vertex " + str(vertexLabel))          
      

  # return a list of vertices after a topological sort 
  
  #def toposort (self):


  # prints a list of edges in ascending order of their weights
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def edgeList (self):
    edges = []
    edge_names = []
    name = []
    num_rows = len(self.adjMat)
    num_cols = len(self.adjMat[0])

    for i in range(num_rows):
      for j in range(num_cols):
        # Creating an edge using the from, to, and weights in the adjacency matrix where the weight is not 0
        
        if(self.adjMat[i][j] != 0):
          
          edge = Edge(i, j, self.adjMat[i][j])
          edges.append(edge)

    edges = sorted(edges, key = lambda edge: edge.weight)
  
    # Finding labels for the edge vertices 
    for item in edges:
      for item2 in self.Vertices:
        if(self.Vertices.index(item2) == item.u):
          u_name = item2.label

        if(self.Vertices.index(item2) == item.v):
          v_name = item2.label
       

      name = str(u_name) + " - " + str(v_name)     
      edge_names.append(name)

    print(', '.join(edge_names))      
       


def main():

  print("Undirected Graph")
  print()

  # Create Graph object
  cities = Graph()
  cities_copy = Graph()

  # Open file for reading
  inFile = open ("./graph.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)
    cities.addVertex (city)
    cities_copy.addVertex(city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  #print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    cities.addDirectedEdge (start, finish, weight)
    cities_copy.addDirectedEdge(start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  #print (startVertex)

  
  print("Adjacency Matrix")
  # print the adjacency matrix
  nVert = len (cities.Vertices)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()

  
  print ("Depth First Search from Houston")
  cities.dfs (11)
  print()

 
  # test breadth first search
  print ("Breadth First Search from Houston")
  cities_copy.bfs (11)
  print()

  ###################
  print("Directed Graph")
  print()


  # Create Graph object
  cities2 = Graph()
  cities2_copy = Graph()

  # Read the vertices
  numVertices2 = int ((inFile.readline()).strip())
  #print (numVertices2)

  
  for i in range (numVertices2):
    city = (inFile.readline()).strip()
    #print (city)
    cities2.addVertex (city)
    cities2_copy.addVertex(city)

  # Read the edges
  numEdges2 = int ((inFile.readline()).strip())
  #print (numEdges2)

  for i in range (numEdges2):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    cities2.addDirectedEdge (start, finish, weight)
    cities2_copy.addDirectedEdge(start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  #print (startVertex)

  print("Adjacency Matrix")
  # print the adjacency matrix
  nVert2 = len (cities2.Vertices)
  for i in range (nVert2):
    for j in range (nVert2):
      print (cities2.adjMat[i][j], end = " ")
    print()
  print ()


  print("Depth First Search From B")
  cities2.dfs (1)
  print()

 
  # test breadth first search
  print ("Breadth First Search from B")
  cities2_copy.bfs (1)
  print()


  ###########
  #print("has Cycle(): " + )
  #cities2.hasCycle()



  # test deletion of an edge
  from_value = "B"
  to = "F"
  result = cities2.deleteEdge(from_value, to)
  print(result)
  print()

  # print the adjacency matrix
  print("Adjacency Matrix")
  nVert2 = len (cities2.Vertices)
  for i in range (nVert2):
    for j in range (nVert2):
      print (cities2.adjMat[i][j], end = " ")
    print()
  print ()


  # test deletion of a vertex
  delete_vert = cities2.deleteVertex("A")
  print(delete_vert)
  print()

  # print the adjacency matrix
  print("Adjacency Matrix")
  nVert2 = len (cities2.Vertices)
  
  for i in range (nVert2):
    for j in range (nVert2):
      print (cities2.adjMat[i][j], end = " ")
    print()
  print ()

  
  #print("hasCycle():" + )
  # print("Topological Sort")

  print("Edge List")
  cities2.edgeList()
  
 
  # Close file
  inFile.close()

  

 
  
main()