# Algorithms for Counting-Sort

The Counting-Sort algorithm is a non-comparative sorting technique suited for sorting integers or data that can be mapped to integer keys.

## Algorithm Steps

1. **Find the Range**:  
   Determine the maximum and minimum values in the input array to calculate the size of the count array.

2. **Initialize the Count Array**:  
   Create a count array of size `max_value - min_value + 1` and initialize all elements to zero.

3. **Count the Elements**:  
   Traverse the input array, and for each element, increment the respective index in the count array.

4. **Compute Cumulative Counts**:  
   Update the count array to reflect the position of each element in the sorted order.

5. **Sort the Array**:  
   Create a result array. Traverse the input array again, placing each element in its correct position in the result array using the count array.

---

##  Analysis of Counting-Sort

### 1. Input Format
- **Input**: An array `A` of \(n\) integers with range \([\text{min}, \text{max}]\).  
- **Output**: A sorted version of `A`.

### 2. Time Complexity
- **Finding Range**: \(O(n)\) to find minimum and maximum values.
- **Counting Elements**: \(O(n)\) to populate the count array.
- **Cumulative Count**: \(O(k)\), where \(k = \text{max} - \text{min} + 1\).
- **Sorting**: \(O(n)\) to fill the output array.

**Overall Complexity**: \(O(n + k)\).


---

# Algorithms for Prim's

## Graph Representation

- **Input**:  
  A list of edges where each edge consists of two nodes and a weight.

- **Output**:  
  An adjacency list representing the graph.

- **Efficiency**:  
  Constructing the adjacency list is \(O(E + V)\), where \(E\) is the number of edges, and \(V\) is the number of vertices.

---

## Priority Queue

This data structure is central to efficiently selecting the smallest weight edge. A binary heap is commonly used.

### Operations:
1. **Insertion**:  
   \(O(\log E)\)

2. **Extract Min**:  
   \(O(\log E)\)

---

## Prim's Algorithm

### Steps:

1. **Push the Start Node's Edges to the Queue**:  
   \(O(\log E)\).

2. **Process Each Edge Removed from the Queue**:  
   For each edge, check if the destination node is unvisited,  
   \(O(\log E)\).

3. **Include the Edge in MST and Process Neighbors**:  
   If the destination is unvisited, include the edge in the MST and push its neighbors' edges,  
   \(O(\log E)\).

### Total Complexity:
The total complexity of Prim's Algorithm is \(O(E \log V)\), because, at worst, every edge is processed once.
