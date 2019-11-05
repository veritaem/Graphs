from operator import itemgetter

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # enqueue integer starting_node tupled with length = 0
    # dequeue, add starting_node to visited if not in
    # make a comparison - is starting_node a child of anything?
    #    if yes: add that parent to the queue along with len + 1,
    #            repeat process until not a child, add that len + node to choices
    #    if no: go to choices, return longest length,
    #           if lengths are same, return smallest node int
    q = Queue()
    v = set()
    c = []
    q.enqueue((starting_node, 0))
    while q.size() > 0:
        i = q.dequeue()
        if i[0] not in v:
            v.add(i[0])
            for x in range(len(ancestors)):
                if ancestors[x][1] == i[0]: # we have a child match
                    q.enqueue((ancestors[x][0], i[1]+1)) #parent/len tuple gets put in q
                else:
                    c.append(i) # no parents; this is the end of a branch, possible choice
    print(c)
    if max(c, key =itemgetter(1))[1] == 0:
        return -1
    print('choice is, ', max(c, key=itemgetter(1))[0])
    return max(c, key=itemgetter(1))[0]

