class Course(object):
    """class for course objects"""
    def __init__(self, class_id, capacity, time, students=None):
        self.class_id = class_id
        self.capacity = capacity
        self.time = time
        self.students = students

    def __repr__(self):
        return "<Course ID=%s>" % self.class_id


class Student(object):
    """class for student objects"""

    def __init__(self, student_id, capacity, start, end, courses=None):
        self.student_id = student_id
        self.capacity = capacity
        self.start = start
        self.end = end
        self.courses = courses

    def __repr__(self):
        return "<Student ID=%s>" % self.student_id


courses = {}
students = {}

def addClass(class_id, capacity, time):
    # If the class is added successfully, 
    # return "Successfully added class ID". 
    # Otherwise, return "Error adding class ID".

    # check if course already exists
    if courses.get(class_id, 0) != 0:
        return "Error adding class ID"
  
    # add course
    new_course = Course(class_id, capacity, time)
    courses[class_id] = new_course
    
    return "Successfully added class ID"
 

def removeClass(class_id):
    # If the class is removed successfully,
    # return "Successfully removed class ID". 
    # Otherwise, return "Error removing class ID".
  
    # check if course already exists
    if courses.get(class_id, 0) == 0:
        return "Error removing class ID"

    # grab course info
    course = courses[class_id]
    student_list = course.students

    # remove course from courses
    del courses[class_id]

    # TODO: unenroll all enrolled students
    for s_id in student_list:
        # update student's list of classes
        student = students[s_id]
        # find index of course in student's list of courses
        course_index = student.courses.index(class_id)
        student.courses.pop(course_index)
        # update item in students dictionary
        students[s_id] = student

    return "Successfully removed class ID"
    
  
def infoClass(class_id):
    # If the class does not exist, 
    # return "Class ID does not exist". 
    # If the class is empty, 
    # return "Class ID is empty". 
    # Otherwise, return the string 
    # "Class ID has the following students: LIST" 
    # where LIST is a sorted, comma-separated list 
    # of student IDs corresponding to students currently 
    # in the class.

    # check if course already exists
    if courses.get(class_id, 0) == 0:
        return "Class ID does not exist"

    course = courses.get(class_id)
    if not course.students:
        return "Class ID is empty"
    
    student_list = ",".join(sorted(course.students))
    return_str = "Class ID has the following students: %s" % student_list

    return return_str

  
def addStudent(student_id, capacity, start, end):
  # If the student is added successfully, 
  # return "Successfully added student ID". 
  # Otherwise, return "Error adding student ID".
    return
  
def removeStudent(student_id):
  # If the student is removed successfully, 
  # return "Successfully removed student ID". 
  # Otherwise, return "Error removing student ID".
    return
  
def infoStudent(student_id):
  # If the student does not exist, 
  # return "Student ID does not exist". 
  # If the student is not taking any classes, 
  # return "Student ID is not taking any classes". 
  # Otherwise, return the string 
  # "Student ID is taking the following classes: LIST" 
  # where LIST is a sorted, comma-separated list of class IDs 
  # corresponding to classes that the student is 
  # currently taking.
    return
  
def enrollStudent(studentId, classId):
  # If enrollment of the student in the class succeeded,
  # return "Number of free spots left in class CLASSID: FREESPOTS" 
  # where FREESPOTS is the number of free spots left 
  # in the class after the student enrolls. 
  # Otherwise, return "Enrollment of student STUDENTID in class CLASSID failed".
    return

def unenrollStudent(studentId, classId):
  # If unenrollment of the student in the class succeeded,
  # return "Number of free spots left in class CLASSID: FREESPOTS" 
  # where FREESPOTS is the number of free spots left in the class 
  # after the student unenrolls. Otherwise, return "Unenrollment 
  # of student STUDENTID in class CLASSID failed".

    return
 