from utils.List.IndexedList import IndexedList

class ReversibleIndexedList(IndexedList):

    def reverse(self):
        n = self.get_length()
        for i in range((n+1)//2):
            j = n - i - 1
            self.swap(i,j)
