'''
Nama : Muhammad Jafar Gundari
NIM  : 13519197
Tanggal : 1 Maret 2021
Topik : Penentuan rencana studi penerapan algorima decrease and conquer menggunakan algoritma toposort
'''

class CourseType:
    # Constructor for class CourseType
    def __init__(self,name):
        self.name = name
        self.prereq = []
        self.inDegree = 0
    
    # Remove course item that exists in prereq, update indegree
    def removePrereq(self,course):
        self.prereq.remove(course)
        self.inDegree -= 1
    
    # Insert item as prereq
    def addPrereq(self,ListCourse):
        for course in ListCourse:
            self.prereq.append(course)
            self.inDegree += 1

    # Print all prerequisites
    def printPrereq(self):
        print("Prerequisites for", self.name, "is : ", end=" ")
        print(self.prereq, end= " ")
        print("In Degree :", self.inDegree)


# Insert all item as type CourseType into ListCourse
def addtoListCourse(arrayCourse):
    global ListCourse
    C = CourseType(arrayCourse[0])
    arrayCourse.pop(0)
    C.addPrereq(arrayCourse)
    ListCourse.append(C)

# Create an array that contains CourseType with indegree = 0
def insert0Degree():
    global ListCourse
    List0Degree = []
    for course in ListCourse:
        if (course.inDegree == 0):
            List0Degree.append(course)
    return List0Degree

# Delete CourseType prereq that equals course.name (removing edge that came from selected course)
def deleteEdge(course, List0Degree):
    global ListCourse
    for matkul in ListCourse:
        if(matkul not in List0Degree):
            if course.name in matkul.prereq:
                matkul.removePrereq(course.name)

# Toposort Algorithm
def toposort():
    global ListCourse
    global semester
    # Base, until ListCourse is empty
    if(len(ListCourse) == 0):
        return
    else:
        # Semester will assigned = 1 for the first time, outside this function, so it is safe
        print("Semester", semester,": ", end=" ")
        # Remove all CourseType with indegree = 0, remove edge from that vertice and print them
        List0Degree = insert0Degree()
        for vertice in List0Degree:
            print(vertice.name, end="; ")
            deleteEdge(vertice, List0Degree)
            # Remove vertice, substract size of ListCourse
            ListCourse.remove(vertice)
        print()
        # Call toposort recursively 
        semester += 1
        toposort()

def printLogo():
    print("  _____     _              _                  ")
    print(" | ____|___| |    ___  ___| |_ _   _ _ __ ___ ")
    print(" |  _| |_  / |   / _ \/ __| __| | | | '__/ _ \\")
    print(" | |___ / /| |__|  __/ (__| |_| |_| | | |  __/")
    print(" |_____/___|_____\___|\___|\__|\__,_|_|  \___|")
    print()
    print("============= Know Your Lecture ==============")
    print("=============      By Jafar     ==============")

def readfile():
    global ListCourse
    # Read file
    try:
        filename = input("Insert filename : ") # with .txt extension
        with open(filename) as filestream:
            for line in filestream:
                course  = line.rstrip(".\n").replace(" ", "").split(',')
                addtoListCourse(course)
        print()
        print("Your result : ")
    except FileNotFoundError:
        print("No such file in this directory. Make sure to type filename correctly")

# MAIN PROGRAM
printLogo()
while(True):
    ListCourse = []
    semester = 1
    print("\n")
    readfile()
    toposort()
    print("==================================================\n")
    choose = input("Do you want to add another file ? (yes/no) ")
    if(choose == "no"):
        print("Thank you!")
        break