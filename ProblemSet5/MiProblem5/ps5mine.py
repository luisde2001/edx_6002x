# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."

    f = open(mapFilename, 'r')
    g = WeightedDigraph()

    dataLineList = []

    line = None

    while True:
        line = f.readline()
        if line == '':
            break
        line_split = string.split(line)
        dataLineList.append(line_split)
    f.close()

    for l in dataLineList:
        if not g.hasNode(Node(l[0])):
            g.addNode(Node(l[0]))
        if not g.hasNode(Node(l[1])):
            g.addNode(Node(l[1]))

    for l in dataLineList:
        g.addEdge(WeihtedEdge(Node(l[0]),Node(l[1]),float(l[2]),float(l[3]))

    return g


########################################################################
########################################################################

mitMap = load_map("mit_map.txt")
print isinstance(mitMap, Digraph)
print isinstance(mitMap, WeightedDigraph)

print mitMap.nodes

print mitMap.edges
