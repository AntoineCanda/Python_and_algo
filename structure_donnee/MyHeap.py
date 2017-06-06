class MyHeap:
    def __init__(self, items):
        self.n = 0;
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap)-1

    def push(self,x):
        assert x not in self.rank
        i = len(self.heap)
        # Ajout d'une feuille
        self.heap.append(x)
        self.rank[x] = i
        # Maj de l'ordre du tas
        self.up(i)

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        # retrait de la derniere feuille
        x = self.heap.pop()
        # tas non vide => on la place a la racine et on maintient l'ordre du tas
        if self:
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)
        return root

    def up(self,i):
        x = self.heap[i]
        while i > 1 and x < self.heap[1 // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        # point d'insertion 
        self.heap[i] = x
        self.rank[x] = i

    def down(self,i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            # descente dans l'arbre
            left = 2*i
            right = left + 1
            if right < n and self.heap[right] < x and self.heap[right] < self.heap[left]:
                # on remonte le fils droit
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i = right
            elif left < n and self.heap[left] < x:
                # on remonte le fils gauche
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
            else :
                # point d'insertion trouve
                self.heap[i] = x
                self.rank[x] = i
                return


    def update(self, old, new):
        # on change la valeur a l'indice i
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        # on maintient l'ordre dans le tas
        if old < new:
            self.down(i)
        else :
            self.up(i)
