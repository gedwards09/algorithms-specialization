from utils.Factory.IFactory import IFactory
from utils.Graph.DirectedEdgeImp import DirectedEdgeImp
from utils.Graph.UndirectedEdgeImp import UndirectedEdgeImp

class EdgeImpFactory(IFactory):
    DirectedEdgeType = 0
    UndirectedEdgeType = 1

    def create(self, type):
        return EdgeImpFactory.create(type)
    
    def create(type):
        if type == EdgeImpFactory.DirectedEdgeType:
            return DirectedEdgeImp()
        elif type == EdgeImpFactory.UndirectedEdgeType:
            return UndirectedEdgeImp()
        else:
            raise Exception("EdgeImpFactory.py:create:creation type not implemented")