"""
Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:
         0

 5 |     3      |  6

4 X|  2     0   | 1 5
 X | 1 X  10 X  | X X

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)
"""

import sys


class Node:

    def __init__(self, val):
        self.cost = val
        self.children = []
        self.parent = []


def sales_path(node):

    node_child_count = len(node.children)

    if not node_child_count:
        return node.cost

    min_val = sys.maxsize
    for i in range(node_child_count):
        temp_cost = sales_path(node.children[i])

        if temp_cost < min_val:
            min_val = temp_cost

    return min_val + node.cost


"""
This is the tree. 0-6-1 = 7
        0
    5        6
  4        1   5
"""

A = Node(0)

B = Node(5)

C = Node(4)

D = Node(6)

E = Node(1)

F = Node(5)

A.children = [B, D]
B.children = [C]
B.parent = A
C.parent = B
D.parent = A
D.children = [E, F]
D.parent = D
F.parent = D

ans = sales_path(A)
print(ans)

"""

Class Node:
  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
    self.best_paths = []

BruteForce: DFS + track minimal cost
Time Compexity: O(N)
Space : O( max depth of tree)

def get_cheapest_cost(rootNode, want_longest=True):
  if rootNode is None:
    return 0
  dfs(rootNode, want_longest)
  return rootNode.best_paths

def dfs(node, want_longest):
  # Basecase
  if not node.children:
    node.best_paths.append([node.cost])
    return node.cost
  
  # Aggregation
  child_costs = [dfs(child, want_longest) for child in node.children]
  best_cost = min(child_costs) if not want_longest else max(child_costs)
  
  for i, child in enumerate(node.children):
    if child_costs[i] == best_cost:
      for best_path in child.best_paths:
        best_path.insert(0, node.cost)
        node.best_paths.append(best_path)
  
  return node.cost + best_cost
"""
