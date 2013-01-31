import sys
import types
import networkx as nx

visited = set()
G = nx.DiGraph()

def tree(parent, mod, base):
    '''
    if str(parent).startswith(base) and not mod.__name__.startswith(base):
        G.add_edge(base, mod.__name__)
    elif mod.__name__.startswith(base) and not str(parent).startswith(base):
        G.add_edge(base, mod.__name__)
    elif not str(parent).startswith(base) and not mod.__name__.startswith(base):
        G.add_edge(base, mod.__name__)
    '''

    #print '"%s" -> "%s" ; '%(parent, mod.__name__)
    if mod in visited:
        return
    visited.add(mod)
    #if "." not in str(parent) and "." not in mod.__name__:
    if str(parent) != str(mod.__name__):
        G.add_edge(str(parent), str(mod.__name__))

    for i in dir(mod):
        obj = getattr(mod, i)
        if isinstance(obj, types.ModuleType):
            tree(mod.__name__, obj, base)

if __name__ == "__main__":
    class Foo: pass
    Foo.__name__ = "Top"
    base = sys.argv[1]
    mod = __import__(base)
    tree(Foo, mod, base)

    '''
    nodes = G.nodes()
    nodes.remove(base)
    for node in nodes:
        base = node
        mod = __import__(base)
        tree(Foo, mod, base)
    '''
    nx.write_graphml(G, base + ".graphml")