"""
Tree data structure is a hierarchical structure that is used to represent and organize data in the form of parent child relationship. The following are some real world situations which are naturally a tree.
    Folder structure in an operating system.
    Tag structure in an HTML (root tag the as html tag) or XML document.
The topmost node of the tree is called the root, and the nodes below it are called the child nodes. Each node can have multiple child nodes, and these child nodes can also have their own child nodes, forming a recursive structure.

Basic Terminologies In Tree Data Structure:
    Parent Node: The node which is an immediate predecessor of a node is called the parent node of that node. {B} is the parent node of {D, E}.
    Child Node: The node which is the immediate successor of a node is called the child node of that node. Examples: {D, E} are the child nodes of {B}.
    Root Node: The topmost node of a tree or the node which does not have any parent node is called the root node. {A} is the root node of the tree. A non-empty tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree.
    Leaf Node or External Node: The nodes which do not have any child nodes are called leaf nodes. {I, J, K, F, G, H} are the leaf nodes of the tree.
    Ancestor of a Node: Any predecessor nodes on the path of the root to that node are called Ancestors of that node. {A,B} are the ancestor nodes of the node {E}
    Descendant: A node x is a descendant of another node y if and only if y is an ancestor of x.
    Sibling: Children of the same parent node are called siblings. {D,E} are called siblings.
    Level of a node: The count of edges on the path from the root node to that node. The root node has level 0.
    Internal node: A node with at least one child is called Internal Node.
    Neighbour of a Node: Parent or child nodes of that node are called neighbors of that node.
    Subtree: Any node of the tree along with its descendant.

Basic Operations Of Tree Data Structure:
    Create – create a tree in the data structure.
    Insert − Inserts data in a tree.
    Search − Searches specific data in a tree to check whether it is present or not.
Traversal:
    Depth-First-Search Traversal
    Breadth-First-Search Traversal
"""