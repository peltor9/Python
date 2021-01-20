## Example array
namelist = [['111','tod','B+'],
            ['444','tapu','A']]
            
            
## 1. Traversal
def traversal():
    for i in range(4):
            print(namelist[i][0]+"\t"+namelist[i][1]+"\t"+namelist[i][2])        
traversal()

## 2. Insertion
def insertion():
        new_id = input("Add new id: ")
        new_name = input("Add new name: ")
        new_grade = input("Add new grade: ") 
        new_student = [new_id, new_name, new_grade]
        count = (len(namelist)+1)
        namelist.insert(count, new_student)
        x = len(namelist)
        for i in range(x):
            print(namelist[i][0]+"\t"+namelist[i][1]+"\t"+namelist[i][2])
insertion()

## 3. Deletion
def deletion():
    for i in range(4):
        print(str(i)+") "+namelist[i][0]+"\t"+namelist[i][1]+"\t"+namelist[i][2])
    seek = input("What position do you want to delete? ")
    namelist.pop(int(seek))
    new_range = len(namelist)
    for i in range(new_range):
        print(namelist[i][0]+"\t"+namelist[i][1]+"\t"+namelist[i][2])
    deletion()

## 4. Update
def update2():
    seek = input("What name do you want to update? ")
    for j in range(4):
        if seek == namelist[j][1]:
            replace_pos = j            
    new_id = input("What is the new id? : ")
    new_name = input("What is new name? : ")
    new_grade = input("What is new grade? : ")    
    namelist[replace_pos][0] = new_id
    namelist[replace_pos][1] = new_name
    namelist[replace_pos][2] = new_grade
    for i in range(4):
                    print(namelist[i][0]+"\t"+namelist[i][1]+"\t"+namelist[i][2])
update2()

## 5. Searching
def searching():
    seek = input("What name do you want to find? ")
    for j in range(4):
        if seek == namelist[j][1]:
            replace_pos = j
            print(namelist[replace_pos][0]+"\t"+namelist[replace_pos][1]+"\t"+namelist[replace_pos][2])
searching()

## 6. Replace
def replace() :
    data = [ ]
    for i in range(2):
        name = input("Tell me the name : ")
        data.append(name)
    print(data)
    no = input("which position you want to replace : ")
    newname = input("Tell me new name : ")
    data[int(no)] = newname
    print(data)
replace()
