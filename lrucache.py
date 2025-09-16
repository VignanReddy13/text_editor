class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail to simplify add/remove
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head (most recent)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """Move given node to the head (most recent)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Remove and return the least recent node."""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        """Return value if key exists, else -1."""
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Add/Update key-value pair in the cache."""
        if key in self.cache:
            # Update the value and move node to head
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                # Pop least recently used node
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]

# ---------- Example Usage ----------
lru = LRUCache(2)
lru.put(1, 'A')
lru.put(2, 'B')       
print(lru.get(1))     
lru.put(5, 'C')       
print(lru.get(2))     
print(lru.get(5))     