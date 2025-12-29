import queue
from typing import List


from structures.node import node

def BFS(start: node, end:node)-> List[node]|None:
    q = queue.Queue() 
    pathToNode = {}

    pathToNode[start.id] = [start]

    while len(q)>0:
        nodeToExpand = q.get()
        
