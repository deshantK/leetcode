from sortedcontainers import SortedList

class SortedListWithSum:
    def __init__(self):
        self.item = SortedList()
        self.total = 0
        self.len = 0
    def add(self, num):
        self.item.add(num)
        self.total +=num
        self.len +=1
    def remove(self, num):
        self.item.remove(num)
        self.total -=num
        self.len -=1


class MKAverage(object):

    def __init__(self, m, k):
        self.lis = []
        self.left = SortedListWithSum()
        self.mid = SortedListWithSum()
        self.right = SortedListWithSum()
        self.k = k
        self.m = m
        self.l = 0
        

    def addElement(self, num):
        self.lis.append(num)
        self.l +=1
        self.left.add(num)
        if self.left.len > self.k:
            rm = self.left.item[-1]
            self.left.remove(rm)

            self.mid.add(rm)
            if self.mid.len > self.m - 2*self.k:
                midrm = self.mid.item[-1]
                self.mid.remove(midrm)
                self.right.add(midrm)
        


        if self.l > self.m:
            del_ = self.lis.pop(0)
            self.l -=1
            #print(del_, self.lis)
            if del_ <= self.left.item[-1]:
                self.left.remove(del_)
                midl = self.mid.item[0]
                self.mid.remove(midl)
                self.left.add(midl)
                rr = self.right.item[0]
                self.right.remove(rr)
                self.mid.add(rr)
            elif self.mid.item[-1] >= del_:
                self.mid.remove(del_)
                rr = self.right.item[0]
                self.right.remove(rr)
                self.mid.add(rr)
            else:
                self.right.remove(del_)


    def calculateMKAverage(self):
        if self.l < self.m:
            return -1
        return (self.mid.total//(self.m - 2*self.k))
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()