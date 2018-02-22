# 100daysofalgorithms

Hello! I'm Daniel Sada. I'm trying to do an algorithm or two a day or at least try to solve a problem a day. I'll be alternating between new algorithms and working in problems with those algorithms. I'm also fairly new with python, and I want to get aquaintanced with Python3.

## Day to Day log.

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
- [ ] Breath-first search

Day 6:
- [x] Breath-first search
- [x] Breath-first tests

Day 7:
- [x] Connected components

Day 8:
- [ ] Bipartite Graph Problem
  
Day 9:
- [x] Heap
- [x] MinHeap

Day 10:
- [x] Min Heap

Day 11:
- [x] Min Heap
- [x] Max Heap
- [x] Heap Unit tests.

NextTODOs:
- Add tests to connected components
- Finish Bipartite Graphs

Backlog:
- [ ] Cycle in graphs problem
- [ ] 7 Bridges of Konnisburg
- [ ] Hamiltonian Cycle
- [ ] Directed Graphs API
- [ ] Directed Graphs DFS
- [ ] Mark-sweep algorithm
- [ ] Directed Graphs BFS

Topics to cover:
 - [x] union-find
 - [ ] binary search
 - [ ] stacks
 - [ ] queues
 - [ ] bags
 - [ ] insertion sort
 - [ ] selection sort
 - [ ] shellsort
 - [ ] quicksort
 - [ ] 3-way quicksort
 - [ ] mergesort
 - [ ] heapsort
 - [ ] binary heaps
 - [ ] binary search trees
 - [ ] red−black trees
 - [ ] separate chaining and linear probing hash tables
 - [ ] Graham scan
 - [ ] and kd-trees
 - [x] depth-first search
 - [x] breadth-first search
 - [ ] topological sort
 - [ ] Kosaraju−Sharir
 - [ ] Kruskal
 - [ ] Prim
 - [ ] Dijkistra
 - [ ] Bellman−Ford
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


# Graphs
## Undirected graph API [(Go to Code.)](algorithms/ugraph/ugraph.py) [(Tests)](algorithms/ugraph/ugraphtest.py)
## Depth First Search [(Go to Code.)](algorithms/dfs/dfs.py) [(Tests)](algorithms/dfs/dfstest.py)
## Breath First Search [(Go to Code.)](algorithms/bfs/bfs.py) [(Tests)](algorithms/bfs/bfstest.py)
## Connected Components [(Go to Code.)](algorithms/connected_components/connected_components.py) (Tests) [Pending]


# Heaps

## Generic Heap [(Go to Code.)](algorithms/heaps/heap.py) 
## Max Heap [(Go to Code.)](algorithms/heaps/maxheap.py) 
## Min Heap [(Go to Code.)](algorithms/heaps/minheap.py) 


# Union Find
## Tests for Union-Find [(Go to Tests.)](algorithms/union-find/unionfindtests.py)

## Comparison: 
```
Worst Case Scenario
quick-find =>  M N
quick-union => M N
weighted QU => N + M log N
QU + path compression => N + M log N
weighted QU + path compression => N + M lg* N

For M union-find operations in a set of N objects.
```


## Quick Find [(Go to Code.)](algorithms/union-find/quickfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(n)
Connected  => O(1)
```

## Quick Union [(Go to Code.)](algorithms/union-find/quickunion.py)

```
Complexity:
Initialize => O(N)
Union      => O(N)
Connected  => O(N)
```

## Weighted Union Find [(Go to Code.)](algorithms/union-find/weightedunionfind.py)

```
Complexity:
Initialize => O(n)
Union      => O(lg N)
Connected  => O(lg N)
```

## PathFlattened and Weighted Union Find [(Go to Code.)](algorithms/union-find/pathflattenedunionfind.py)

```
Complexity:
Complexity:
Initialize => O(n)
Union      
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
Connected  
    => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
```

