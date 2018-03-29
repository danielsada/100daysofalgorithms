# 100daysofalgorithms

Hello! I'm Daniel Sada. I'm trying to do an algorithm or two a day or at least try to solve a problem a day. I'll be alternating between new algorithms and working in problems with those algorithms. I'm also fairly new with python, and I want to get aquaintanced with Python3.

# Running unit tests.

Clone the project, then run :

```
python3 -m unittest discover algorithms/test -p '*.py'
```

# Day to Day log.

Day 1:
- [x] Quick Find
- [x] Quick Union

Day 2:
- [x] Union Find
- [x] Weighted Union Find
- [x] Flattened Path Union Find

Day 3:
- [x] (partial) (undirected) Graph API

Day 4:
- [x] (finished) (undirected) Graph API
- [x] Graph API tests.
- [x] Depth-First search initialization

Day 5: 
- [x] Path between two nodes with backtracking.
- [x] Breath-first search (not finished)

Day 6:
- [x] Breath-first search
- [x] Breath-first tests

Day 7:
- [x] Connected components

Day 8:
- [x] Bipartite Graph Problem
  
Day 9:
- [x] Heap
- [x] MinHeap

Day 10:
- [x] Min Heap

Day 11:
- [x] Min Heap
- [x] Max Heap
- [x] Heap Unit tests.

Day 12: 
- [x] Bipartite grahps
- [x] Bipartite graph tests.

Day 13:
- [x] Refactoring some components to use .V instead of .num_V(), more pythonic.
- [x] Directed Graph API
- [x] Started Topological Sort

Day 14:
- [x] Finished topological sort. (tests pending)
- [x] Finished undirected graph cycle detection.
- [x] Added tests to connected components.
- [x] Started directed cycle detection.  

Day 15:
- [x] Finished directed cycle detection
- [x] Kosajaru-Sharir algoritms for strongly connected components
- [x] Added tests for topological sort
- [x] Added reversal of directed graphs
- [x] A sample stack problem, as we are in python.

Day 16:
- [x] Binary search problem for completion.

Day 17: 
- [x] Created Snippets for faster coding.
- [x] Selection Sort

Day 18: 
 - [x] insertion sort
 - [x] shellsort

Day 19:
 - [x] Weighted Graph and Edge API and 
 - [x] Minimum Spanning Trees API. 

Day 20:
- [x] Kruskal's implementation for finding the Minimum Spanning Tree of a Weighted Graph. 

Day 21:
- [x] Mergesort implemented specifically for python.

Day 22:
- [x] Sorting tests for shell sort, insertion sort, selection sort, etc. Standardize all sorts to have the same property .sorted

Day 23:
- [x] Quicksort

Day 24: 
- [x] Dijkstra's Three way quicksort 

Day 25:
- [x] Added priority queue.er (Which is only a Max Heap that implements total ording) 
- [x] Implemented tupled ordering in max heap to make max heap usable for a priority queue. 
- [x] Added tests for max heaps with tuples and priority queues.

Day 26:
- [x] Started working on Binary Search Trees and Symbol tables. 

Day 27:
- [x] Finished Binary Search Tree get and put implementations, 
- [x] Added some unit tests for bst

Day 28:
- [x] Added ceiling, floor min and max to bst.

Day 29:
- [x] Added python iterators
- [x] Started rank

Day 30:
- [x] Started working on hibbard's deletion for binary search trees
- [x] adding some unit tests, debugging some bugs.

Day 31:
- [x] Bugfixing, bst methods should take keys, not items.
- [x] Added more unit tests.

Day 32 : 
- [x] Started to learn (and code) red black trees. 

Day 33:
- [X] Implemented rotate left, rotate right, move left move right and put for Red Black Trees

Day 34:
- [x] Finished Red Black Tree Deletion, 
- [x] RBT Minimum, 
- [x] Balancing the tree.

Day 35:
- [x] Linted the entire project, fixed all of the warnings in the files. 

Day 36:
- [x] Learned about kd trees. 
- [x] Added some more tests to BSTs
- [x] level order traversal for BST.

Day 37:
- [x] Added unit tests to my Red Black tree implementation.
- [x] Bugfixing RBTs
- [x] Discovered delete min was not implemented correctly

Day 38:
- [x] Learned about 1D and 2D interval search with BSTs
- [x] Implemented in some cases python __len__ __repr__ __build_subclass__ etc, also __add__.

Day 39:
- [x]  More changes in imports.
- [x] started prim's algorithm for MSTs 
- [x] Seeing whether a contains method is useful in a MST.

Day 40:
- [x] Kept working on prim's algorithm for minimum spanning trees. 
- [x] I added some unit tests for prim.
- [x] Dunder methods for Heap, PQ, Edge, etc.

Day 41:
- [x] Finally finished Prim's algorithm. 
- [x] Added Heap unit tests, priority queue unit tests, fixed weighted graph. 
- [x] Added tests for weighted graphs.

Day 42: 
- [x] Read about Delaunay's Triangulation and Voronoi diagrams. 
- [x] Learned about how Prim & Kruskal's algorithms can be used for k-clustering and that it can be close to linear. 
- [x] Implemented Directed Weighted Graphs API.

Day 43:
- [x] Started working on Dijkstra 
- [x] MinimumIndexedPriority queues.

Day 44: 
- [x] Continued implementing Dijkstra implemented with MinimumIndixedPriority queues

Day 45: 
- [x] Did Dijkstra unit test, still debugging. 

Day 46:
- [x] Finished Dijkstra implementation with Indexed Minimum Priority Queues

Day 47:
- [x] Implemented Bellman-Ford for negative directed graphs without negative cycles.

Topics to cover:
 - [x] union-find
 - [x] binary search
 - [x] stacks
 - [x] queues   
 - [x] insertion sort
 - [x] selection sort
 - [x] shellsort
 - [x] quicksort
 - [x] 3-way quicksort
 - [x] mergesort
 - [x] heapsort
 - [x] binary heaps
 - [x] binary search trees
 - [x] red−black trees
 - [x] depth-first search
 - [x] breadth-first search
 - [x] topological sort
 - [x] Kosaraju−Sharir
 - [x] Kruskal
 - [x] Prim
 - [x] Dijkistra
 - [X] Bellman−Ford
 - [ ] Ford−Fulkerson
 - [ ] LSD radix sort
 - [ ] MSD radix sort
 - [ ] 3-way radix quicksort
 - [ ] multiway tries
 - [ ] ternary search tries
 - [ ] Knuth−Morris−Pratt
 - [ ] Boyer-Moore
 - [ ] Rabin−Karp
 - [ ] regular expression matching
 - [ ] run-length coding
 - [ ] Huffman coding
 - [ ] LZW compression and Burrows−Wheeler transform.

Things to implement when finished researching regular algorithms (due to the time they take)
 - [ ] Graham scan
 - [ ]  kd-trees

TODO after all algorithms:
- [ ] Determine complexities
- [ ] Add docstrings to tests.

# Links
## Will fill this as soon as I finish

# Graphs
## Undirected graph API [(Go to Code.)](algorithms/ugraph/ugraph.py) [(Tests)](algorithms/test/ugraphtest.py)
## Depth First Search [(Go to Code.)](algorithms/dfs/dfs.py) [(Tests)](algorithms/test/dfstest.py)
## Breath First Search [(Go to Code.)](algorithms/bfs/bfs.py) [(Tests)](algorithms/test/bfstest.py)
## Connected Components [(Go to Code.)](algorithms/dfs/connected_components.py) [(Tests)](algorithms/test/dfstest.py)


# Heaps

## Generic Heap [(Go to Code.)](algorithms/heaps/heap.py) 
## Max Heap [(Go to Code.)](algorithms/heaps/maxheap.py) 
## Min Heap [(Go to Code.)](algorithms/heaps/minheap.py) 


# Union Find
## Tests for Union-Find [(Go to Tests.)](algorithms/union-find/unionfindtests.py)
## PathFlattened and Weighted Union Find [(Go to Code.)](algorithms/union-find/pathflattenedunionfind.py)
## Weighted Union Find [(Go to Code.)](algorithms/union-find/weightedunionfind.py)

