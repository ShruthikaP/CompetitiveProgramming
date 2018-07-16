import unittest
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None
def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception ('legal coloring impossible for node with loop : %s' %node.label)
        used_col = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
        for color in colors:
            if color not in used_col:
                node.color = color
                break