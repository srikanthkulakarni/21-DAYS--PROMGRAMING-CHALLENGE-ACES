size=int(input("enter the size:"))
print("enter the elements in array:")
data=[int(input())for i in range(size)]
print("input data:",data)
class insert_sort:
    def __init__(self,data,len):
        self.data=data
        self.len=len

    def insertion_sort(self):
        for i in range(1,self.len):
            temp=self.data[i]
            j=i-1
            while(j>=0 and temp<self.data[j]):
                self.data[j+1]=self.data[j] 
                j-=1
            self.data[j+1]=temp
        print(self.data)

print("sorted data:")
s=insert_sort(data,size)
s.insertion_sort()
