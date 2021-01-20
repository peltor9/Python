## 1. Traversal

def traversal() :
    num = [3,4,89,12,10,1]
    for i in range (6) :
        print("Data ["+str(i)+"] = "+str(num[i]))
traversal()


## 2. Searching

def searching():
    num = [3,4,89,12,10,1]
    ck = 0
    for i in range (6) :
        if num[i] ==12:
            print("found at position : "+str(i))
            ck = 1
        if ck ==0:
            print("not found")
searching()


## 3. Insertion

def insert_array():
        data = [5,4,3,2,7]
        newdata = 999
        pos=2
        print(data)
        for i in range(len(data)-1,pos-2,-1):
                data[i] = data[i-1]
        data[i] = newdata
        print(data)

                                   ## //// Insert in to empty array
def insert_to_array():               
        data = []
        for i in range(2):
                name = input("enter name: ")
                data.append(name)
        print(data)


## 4. Deletion

def replace():
        name = []
        for i in range(3):
                fname = input("enter first name: ")
                name.append(fname)          
        print(name)
        no=input("which position to replace: ")
        newname=input("what is the new name: ")
        name[int(no)] = newname
        print(name)


## 5. Reversing

def reverse():
    num = [3,4,89,12,10,1]
    for i in range(6):
        print("Data ["+str(len(num)-i-1)+"] = "+str(num[len(num) -i-1]))
reverse()


## 6. Sorting           // Prints by column order

d = [["a","b","xx"],
     ["c","d","yy"],
     ["c2","d2","yy2"],
     ["e","f", "zz"]]
for i in range(4):         
     for j in range(3):
          print(d[i] [j])

                        ## /// Prints by row order
b = [["a","b","xx"],
     ["c","d","yy"],
     ["c2","d2","yy2"],
     ["e","f", "zz"]]
for i in range(3):     
     for j in range(4):
          print(b[j] [i])


## Calculate and print

d = [["Vlad", 20,80],   
  ["Donny",100, 90]]
for i in range(2):
          print(d[i][0]+" : " +str(d[i][1]+d[i][2])) 
