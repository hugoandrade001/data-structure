 
class Deque:
    """
    A Deque: a double-ended queue (combined stack and queue data structure)
    """

    def __init__(self):
        self.array = [None for _ in range(4)]   # underlying array
        self.capacity = 4   # the capacity of the underlying array
        self.size = 0       # the number of elements stored
        self.head = 0       # the head index (guaranteed to be valid index)
        self.tail = 0       # the tail index at which to insert (guaranteed to be valid index)


    def push(self, x):
        # Double capacity if needed
        if self.capacity == self.size:
            self.copy_into([None for _ in range(self.capacity * 2)])

        # Put element at tail of array
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1


    def pop(self):
        return self.remove(head=False)


    def enqueue(self, x):
        self.push(x)


    def dequeue(self):
        return self.remove(head=True)


    def remove(self, head):
        """
        Removes and returns element from head/tail. Downsizes array if small enough
        :param head: If true, removes from head, else from tail
        """
        if self.size == 0:
            raise Exception('Deque is empty')
        self.size -= 1

        # Wipe and store the removed element
        if head:
            ret = self.array[self.head]
            self.array[self.head] = None
            self.head = (self.head + 1) % self.capacity
        else:
            ret_idx = (self.tail - 1) % self.capacity
            ret = self.array[ret_idx]
            self.array[ret_idx] = None
            self.tail = ret_idx

        # Downsize array if needed (minimum capacity 4)
        if self.capacity > 4 and self.size <= self.capacity / 4:
            self.copy_into([None for _ in range(self.capacity // 2)])

        return ret


    def copy_into(self, new_array):
        """
        Copies elements from self.array into new_array and updates internal state
        """
        for i in range(self.size):
            new_array[i] = self.array[(i + self.head) % self.capacity]
        self.capacity = len(new_array)
        self.array = new_array
        self.head, self.tail = 0, self.size



"========= Testing Deque ========="

def test_deque():
    d = Deque()
    print(d.array)

    d.push(1)
    d.push(2)

    print(d.array)

    print(d.dequeue())
    print(d.array)

    d.enqueue(3)
    d.enqueue(4)
    print(d.array)
    d.enqueue(5)
    print(d.array)
    d.enqueue(6)
    print(d.array)

    print(d.pop())
    print(d.dequeue())
    print(d.array)


    for i in range(6, 20):
        d.push(i)
    print(d.array)