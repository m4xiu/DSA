from typing import List, Optional


class Node:
    """Represents a node in the segment tree storing range information."""
    __slots__ = "l", "r", "lmx", "rmx", "mx"
  
    def __init__(self, l: int, r: int):
        self.l = l        # Left boundary of the range
        self.r = r        # Right boundary of the range
        self.lmx = 1      # Maximum consecutive repeating chars from left
        self.rmx = 1      # Maximum consecutive repeating chars from right
        self.mx = 1       # Maximum consecutive repeating chars in range


class SegmentTree:
    """Segment tree for efficiently querying and updating longest repeating substring."""
    __slots__ = "chars", "tree"
  
    def __init__(self, s: str):
        self.chars = list(s)  # Convert string to list for easy modification
        n = len(s)
        self.tree: List[Optional[Node]] = [None] * (n * 4)
        self.build(1, 1, n)
  
    def build(self, node_idx: int, left: int, right: int) -> None:
        """Build the segment tree recursively."""
        self.tree[node_idx] = Node(left, right)
      
        if left == right:
            # Leaf node - single character
            return
      
        mid = (left + right) // 2
        # Build left subtree
        self.build(node_idx << 1, left, mid)
        # Build right subtree
        self.build(node_idx << 1 | 1, mid + 1, right)
        # Update current node based on children
        self.pushup(node_idx)
  
    def query(self, node_idx: int, query_left: int, query_right: int) -> int:
        """Query the maximum consecutive repeating characters in range [query_left, query_right]."""
        current_node = self.tree[node_idx]
      
        # If current range is completely within query range
        if current_node.l >= query_left and current_node.r <= query_right:
            return current_node.mx
      
        mid = (current_node.l + current_node.r) // 2
        result = 0
      
        # Query left child if needed
        if query_left <= mid:
            result = self.query(node_idx << 1, query_left, query_right)
      
        # Query right child if needed
        if query_right > mid:
            result = max(result, self.query(node_idx << 1 | 1, query_left, query_right))
      
        return result
  
    def modify(self, node_idx: int, position: int, new_char: str) -> None:
        """Modify character at position to new_char (1-indexed position)."""
        current_node = self.tree[node_idx]
      
        if current_node.l == current_node.r:
            # Leaf node - update the character
            self.chars[position - 1] = new_char
            return
      
        mid = (current_node.l + current_node.r) // 2
      
        if position <= mid:
            # Update left child
            self.modify(node_idx << 1, position, new_char)
        else:
            # Update right child
            self.modify(node_idx << 1 | 1, position, new_char)
      
        # Update current node based on children
        self.pushup(node_idx)
  
    def pushup(self, node_idx: int) -> None:
        """Update parent node information based on its children."""
        root = self.tree[node_idx]
        left_child = self.tree[node_idx << 1]
        right_child = self.tree[node_idx << 1 | 1]
      
        # Initially inherit values from children
        root.lmx = left_child.lmx
        root.rmx = right_child.rmx
        root.mx = max(left_child.mx, right_child.mx)
      
        # Calculate range lengths
        left_range_size = left_child.r - left_child.l + 1
        right_range_size = right_child.r - right_child.l + 1
      
        # Check if characters at the boundary are the same
        if self.chars[left_child.r - 1] == self.chars[right_child.l - 1]:
            # If left child is completely uniform, extend lmx
            if left_child.lmx == left_range_size:
                root.lmx += right_child.lmx
          
            # If right child is completely uniform, extend rmx
            if right_child.rmx == right_range_size:
                root.rmx += left_child.rmx
          
            # Update maximum by considering the merge at boundary
            root.mx = max(root.mx, left_child.rmx + right_child.lmx)


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        """
        Process queries to modify string and return longest repeating substring after each query.
      
        Args:
            s: Initial string
            queryCharacters: Characters to update at each query
            queryIndices: 0-indexed positions to update at each query
          
        Returns:
            List of integers representing longest repeating substring after each query
        """
        # Initialize segment tree with the string
        segment_tree = SegmentTree(s)
        results = []
      
        # Process each query
        for index, char in zip(queryIndices, queryCharacters):
            # Convert 0-indexed to 1-indexed and modify
            segment_tree.modify(1, index + 1, char)
            # Query entire range for maximum consecutive repeating characters
            max_repeating = segment_tree.query(1, 1, len(s))
            results.append(max_repeating)
      
        return results

