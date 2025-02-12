 

class MinHeap:


    def __init__(self, array=None):
     
        self.array = array or []
        # BUILD HEAP
        if len(self.array) > 1:
            for idx in reversed(range(len(array))):
                self.heapify(idx)


    def find_min(self) -> int:
        return self.array[0]


    def extract_min(self) -> int:
        # Move last elt to root and heapify root
        ret = self.array[0]
        self.array[0] = self.array.pop()
        self.heapify(0)
        return ret


    def insert(self, x):
        # Insert at bottom right and bubble up
        self.array.append(x)
        cur_idx = len(self.array) - 1
        par_idx = MinHeap.parent(cur_idx)

        while cur_idx > 0 and self.array[cur_idx] < self.array[par_idx]:
            self.array[cur_idx], self.array[par_idx] = self.array[par_idx], self.array[cur_idx]
            cur_idx = par_idx
            par_idx = MinHeap.parent(cur_idx)


    "======== Helpers ========"

    def heapify(self, idx):
       
        left = MinHeap.left(idx)
        right = MinHeap.right(idx)
        while (left < len(self.array) and self.array[left] < self.array[idx])\
                or (right < len(self.array) and self.array[right] < self.array[idx]):

            new_par = left if right >= len(self.array) or self.array[left] < self.array[right] else right
            self.array[idx], self.array[new_par] = self.array[new_par], self.array[idx]

            idx = new_par
            left = MinHeap.left(idx)
            right = MinHeap.right(idx)


    @staticmethod
    def left(idx):
        return (idx + 1) * 2 - 1


    @staticmethod
    def right(idx):
        return (idx + 1) * 2


    @staticmethod
    def parent(idx):
        return (idx - 1) // 2



"========= Testing Heap ========="

heap = MinHeap([10, 7, 3, 6, 0, 5, 4, 2])
print(heap.array)

heap.insert(8)
print(heap.extract_min())  # pops 0
heap.insert(1)
heap.insert(9)
heap.insert(0)

print(heap.array)
#   U p d a t e d   H e a p   i m p l e m e n t a t i o n  
 #   H e a p :   I m p l e m e n t s   M i n H e a p   o r   M a x H e a p   f o r   e f f i c i e n t   p r i o r i t y   q u e u e   o p e r a t i o n s .   U s e d   i n   a l g o r i t h m s   l i k e   D i j k s t r a ' s   a n d   H u f f m a n   c o d i n g .  
 