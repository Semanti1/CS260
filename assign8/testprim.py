import sys
#from heap import Heap
class Heap:
        '''
        Implementation of a binary minimum heap data structure
        Assumptions:
                Input elements can be tuples or lists, where
                the first element is a key (which the algorithm for enforcing the heap property is based on),
                the second element is an identifier for the related object,
                and after that, anything can follow.
        Attributes:
                heap: a list as a realization of the heap
                heapIdx: a dictionary with keys the identifiers of the objects in the heap, and
                                 with values the indices of the objects' positions in the heap.
        '''

        def __init__(self, element = None, batch = None):
                '''
                Creates the heap
                The heap can be initiated empty, with an object, or with many objects
                Args:
                        element: an object for insertion into the heap
                        batch: a list of objects for insertion into the heap
                '''
                self.heap, self.heapIdx = [], {}
                if batch: self.heapify(batch)
                if element: self.insert(element)


        def length(self):
                '''
                Returns the number of objects in the heap
                '''
                return len(self.heap)


        def insert(self, element):
                '''
                Inserts an object in the heap
                Args:
                        element: object for insertion into the heap
                '''
                self.heap[self.length():] = [element]
                self.heapIdx[element[1]] = self.length() - 1
                self.__siftUp()


        def __siftUp(self):
                '''
                Enforces the heap property (after an insertion into the heap)
                '''
                childIdx = self.length() - 1
                parentIdx = int((childIdx - 1) / 2)
                while self.heap[childIdx][0] < self.heap[parentIdx][0]:
                        parent, child = self.heap[parentIdx], self.heap[childIdx]
                        self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
                        self.heap[childIdx], self.heapIdx[parent[1]] = parent, childIdx
                        parentIdx, childIdx = int((parentIdx - 1) / 2), parentIdx
        def heapify(self, batch):
                '''
                Builds the heap in linear time
                
                Args:
                        batch: list of objects for insertion into the heap
                '''
                for idx, element in enumerate(batch):  # populates the heap
                        self.heap.append(element)
                        self.heapIdx[element[1]] = idx
                for i in range(int(self.length() / 2) - 1, -1, -1):  # enforces the heap property
                        self.__minHeapify(i)


        def __minHeapify(self, parentIdx):
                '''
                Enforces the heap property, top to bottom, along a certain path
                
                Args:
                        parentIdx: starting position for the checking
                '''
                leftChildIdx, rightChildIdx = 2 * parentIdx + 1, 2 * parentIdx + 2
                lowest = leftChildIdx if leftChildIdx < self.length() and self.heap[leftChildIdx] < self.heap[parentIdx] else parentIdx
                if rightChildIdx < self.length() and self.heap[rightChildIdx] < self.heap[lowest]: lowest = rightChildIdx
                if lowest != parentIdx:
                        parent, child = self.heap[parentIdx], self.heap[lowest]
                        self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
                        self.heap[lowest], self.heapIdx[parent[1]] = parent, lowest
                        self.__minHeapify(lowest)


        def extractMin(self):
                '''
                Extracts the top (minimum) object from the heap, and rectifies the heap
                '''
                minElm = self.heap[0]
                del self.heapIdx[minElm[1]]
                lastElm = self.heap.pop()
                if self.length():
                        self.heap[0] = lastElm
                        self.heapIdx[lastElm[1]] = 0
                        self.__siftDown(0)
                return minElm


        def __siftDown(self, parentIdx):
                '''
                Enforces the heap property (after an extraction from the heap)
                '''
                if 2 * parentIdx + 1 >= self.length(): return  # if the parent doesn't have children, you are good to go!
                if 2 * parentIdx + 2 >= self.length():  # if the parent has one child...
                        # and the child's key is less than the parent's key, it swaps the entries
                        if self.heap[parentIdx][0] > self.heap[2 * parentIdx + 1][0]:
                                parent, child = self.heap[parentIdx], self.heap[2 * parentIdx + 1]
                                self.heap[parentIdx], self.heapIdx[child[1]] = child, parentIdx
                                self.heap[2 * parentIdx + 1], self.heapIdx[parent[1]] = parent, 2 * parentIdx + 1
                        return
                parent = self.heap[parentIdx]
                leftChild, rightChild = self.heap[2 * parentIdx + 1], self.heap[2 * parentIdx + 2]
                minLeft = False
                if leftChild[0] <= rightChild[0]: minLeft = True
                if parent[0] > min(leftChild[0], rightChild[0]):
                        self.heap[parentIdx] = leftChild if minLeft else rightChild
                        self.heapIdx[leftChild[1] if minLeft else rightChild[1]] = parentIdx
                        self.heap[2 * parentIdx + 1 if minLeft else 2 * parentIdx + 2] = parent
                        self.heapIdx[parent[1]] = 2 * parentIdx + 1 if minLeft else 2 * parentIdx + 2
                        self.__siftDown(2 * parentIdx + 1 + (not minLeft))
        def get(self, id):
                '''
                Returns an object from the heap. If the object is not in the heap, it returns None
                Args:
                        id: identifier of the object to be retrieved
                '''
                return self.heap[self.heapIdx[id]] if id in self.heapIdx else None


        def delete(self, id):
                '''
                Deletes an object from the heap, and returns that object
                Args:
                        id: identifier of the object to be handled
                '''
                if id not in self.heapIdx: return None
                idx = self.heapIdx[id]
                del self.heapIdx[id]
                element = self.heap[idx]
                lastElm = self.heap.pop()
                if idx != self.length():
                        self.heap[idx] = lastElm
                        self.heapIdx[lastElm[1]] = idx
                        self.__siftDown(idx)
                return element


def prim(G,start_node):
	'''
	Prim's Minimum Spanning Tree (MST) Algorithm 
	It finds a MST of an undirected graph
	Args:
		adjList: a dictionary, as a realization of an adjacency list, in the form
				 adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
				 Note: Every vertex should have an entry in the adjList
	Returns:
		mst: a set of all the edges (ids) that constitute the minimum spanning tree
	'''
	# if len(sys.argv) < 2: sys.exit("Error: No filename")
       # filename = sys.argv[1]
	#num=sys.argv[2]
	print("Running Prim's algorithm")
	print("Starting node:",start_node)
	adjList, edgeList = graph(G)

	def updateHeap(v):
		'''
		Updates the heap with entries of all the vertices incident to vertex v that was recently explored
		Args:
			v: a vertex that was recently explored
		'''
		for vertex,weight,edgeID in adjList[v]:
			if vertex not in explored:
				# Updates (!) the weight and reinserts the element into the heap
				element = unexplored.delete(vertex)
				if element and element[0] < weight: unexplored.insert(element)
				else: unexplored.insert((weight,vertex,edgeID))

	source = list(adjList.keys())[int(start_node)]  # Chooses an arbitrary vertex as the starting point of the algorithm
	# unexplored: a heap with elements of the following format (minWeight, destinationVertex, edgeID)
	unexplored, explored, mst = Heap(), set([source]), set()
	updateHeap(source)

	while unexplored.length():
		[weight, vertex, edgeID] = unexplored.extractMin()
		explored.add(vertex)
		mst.add(edgeID)
		print("Added",vertex)
		if edgeList[edgeID][0]>edgeList[edgeID][1]:
			#temp=edgeList[edgeID][0]
			#edgeList[edgeID][0]=edgeList[edgeID][1]
			#edgeList[edgeID][1]=temp
			edgeList[edgeID]=[edgeList[edgeID][1],edgeList[edgeID][0],edgeList[edgeID][2]]
		print(list(edgeList[edgeID]))
		updateHeap(vertex)
	
	return mst
parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1
def kruskal(G):
	with open(G, 'r') as f:
                numbers = f.readline().split()
                numVertices = int(numbers[0])
	i=0
	while i<numVertices:
		make_set(i)
		i=i+1
	mst=set()
	adjList, edgeList = graph(G)
	#mst=prim(G,0)
	newlist=[]
	print('Running Kruskal\'s algorithm')
	for edgeId in edgeList:
		newlist.append(edgeList[edgeId])
	
	newlist1=sorted(newlist, key=lambda tup: tup[2])
	for edge in newlist1:
		#print("selected Edge:",edge)
		v1,v2,wt=edge
		if find(v1)!=find(v2):
			union(v1,v2)
			mst.add(edge)
	#print(newlist1)	
	for edgek in sorted(mst,key=lambda tup: tup[2]):
		if edgek[0]>edgek[1]:
                        #temp=edgeList[edgeID][0]
                        #edgeList[edgeID][0]=edgeList[edgeID][1]
                        #edgeList[edgeID][1]=temp
                        edgek=(edgek[1],edgek[0],edgek[2])

		print("Selected Edge:",list(edgek))

def graph(filename):
	'''
	Builds an adjacency list and an incidence list
	Args:
		filename: the name of the file with a representation of the graph. The first line of the file specifies
				  the number of the vertices and the number of the edges. The file is assumed to specify
				  the edges of the graph in the following format: v w e, where v is one vertex of the
				  associated edge, w is the other vertex, and e is the edge's weight
	
	Returns:
		adjList: a dictionary, as a realization of an adjacency list, in the form
				 adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
		edgeList: a dictionary, as a realization of an incidence list, in the form
				  edgeList[edgeId] = (vertex1,vertex2,weight)
	'''
	adjList, edgeList = {}, {}

	with open(filename, 'r') as f:
		numbers = f.readline().split()
		numVertices = int(numbers[0])
		edgeID = 1

		for line in f:
			edge = line.split()
			vertex1, vertex2, weight = int(edge[0]), int(edge[1]), float(edge[2])
			
			if vertex1 in adjList: adjList[vertex1].append((vertex2,weight,edgeID))
			else: adjList[vertex1] = [(vertex2,weight,edgeID)]
			if vertex2 in adjList: adjList[vertex2].append((vertex1,weight,edgeID))
			else: adjList[vertex2] = [(vertex1,weight,edgeID)]
			
			edgeList[edgeID] = (vertex1,vertex2,weight)
			
			edgeID += 1

	return adjList, edgeList



#if __name__ == "__main__":
#	if len(sys.argv) < 2: sys.exit("Error: No filename")
#	filename = sys.argv[1]

#	adjList, edgeList = graph(filename)
def main():
	print("welcome to Minimum Spanning Tree Finder")
	filename=input("Give the file name graph is in:")
	print("Commands:")
	print("exit or ctrl-d - quits the program")
	print("help - prints this menu")
	print("prim integer_value - run's Prim's algorithm starting at node given")
	print("kruskal - runs Kruskal's algorithm")
	command=input("Enter Command:")
	c=command.split(' ',1)
	while c[0]!='exit':
		if c[0]=='help':
			print("Commands:")
			print("exit or ctrl-d - quits the program")
			print("help - prints this menu")
			print("prim integer_value - run's Prim's algorithm starting at node given")
			print("kruskal - runs Kruskal's algorithm")
		elif c[0]=='prim':
			prim(filename,c[1])
		else:
			kruskal(filename)			
		command=input('Enter Command:')
		c=command.split(' ',1)
	print('Bye')
if __name__=="__main__":
	main()

#	mst = primsMSTAlgorithm(adjList)
#	newlist=[]
#	cost = 0
	# Computes the sum of the weights of all edges in the MST
#	for edgeID in mst:
#		cost += edgeList[edgeID][2]
		#print(edgeList[edgeID])
#		newlist.append(edgeList[edgeID])
#	print(cost)
#	newlist1=sorted(newlist, key=lambda tup: tup[2])
#	print(newlist1)
