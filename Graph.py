# references : https://www.techiedelight.com/graph-implementation-python/
# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            # allocate node in adjacency list from src to dest (directed graph)
            # self.adjList[src].append(dest)

            # uncomment this to change the graph to undirected graph
            # allocate node in adjacency list from src to dest if it doesn't exist
            if dest not in self.adjList[src]:
                self.adjList[src].append(dest)
            # for undirected graph, add reverse edge as well if it doesn't exist
            if src not in self.adjList[dest]:
                self.adjList[dest].append(src)


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
        print("The total number of neighbour of " + str(src) + " is " + str(countNeighbour(graph, src)))


# Question 3
def countNeighbour(graph, src):
    count = len(graph.adjList[src])
    return count

if __name__ == '__main__':
    # Input: Edges in a directed graph
    edges = [(0, 1), (1, 3), (2, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 3)]

    # No. of vertices (labelled from 0 to 5)
    n = 5

    # construct a graph from a given list of edges
    graph = Graph(edges, n)

    # print adjacency list representation of the graph
    printGraph(graph)
