#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Graph:
    def __init__(self):
        self.graph = (list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cycle_in_graph(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                if self.is_cycle_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def has_cycle(self):
        visited = [False] * len(self.graph)
        for i in range(len(self.graph)):
            if visited[i] is False:
                if self.is_cycle_util(i, visited, -1):
                    return True
        return False

g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(2, 4)


if g.has_cycle():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")


# In[6]:


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cycle_in_graph(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                if self.cycle_in_graph(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def has_cycle(self):
        visited = [False] * len(self.graph)
        for i in range(len(self.graph)):
            if visited[i] is False:
                if self.cycle_in_graph(i, visited, -1):
                    return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.has_cycle():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")


# In[ ]:




