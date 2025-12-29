# Heap sort (Max Heap)
Properties of a heap:
- A complete binary tree, with 
	- left child of node i = i << 2 (bit shifting)
	- right child of node i = (i<<2) +1
	- parent of node i = i >> 2
- Height: The number of edges on the longest simple downward path form the node to the leaf.
### Core algorithms
##### Max Heapify
MaxHeapify(A, i)
Assumes the binary tree rooted at left child and right child of i are max heap, but A\[i\] might be violating the max heap property.

The algorithm first checks if the value at A\[i\] is the largest among its children, if yes, then nothing need to be done.
Otherwise, it finds the largest element and swap it with A\[i\], then recursively MaxHeapify the binary tree rooted at the swapped children, since its value decreased after swapping, the algorithm makes sure the update subtree also obeys max heap property.


##### Build Max Heap
BuildMaxHeap(A)
Converts an array A into a max heap by calling MaxHeapify in a bottom-up manner.
- Why bottom-up:
	- Because MaxHeapify assumes the child nodes of node i already satisfy max heap property, so we need to start from the last non-leaf node. Since the left child of node i is 2i, the first non-leaf node is where 2i>len(A), which is len(A)/2.
	
##### Heap Sort
Since the root node of a max heap is guaranteed to be the largest element in the tree, we can extract it by swapping it with the last node, then heapify the remaining elements until only two elements left in the tree.
# Priority Queue
### Operations
##### Insert
Insert the element into the queue
Insert the element to the end of the tree, then heapify the whole tree.
##### Extract
Extract the largest element in the queue
By substituting the last element with the root and the heapify the whole tree.
##### Update Priority
Increase the value of an element in the queue and update the priority, then heapify the whole tree.
##### Maximum
Return the maximum element in the queue
