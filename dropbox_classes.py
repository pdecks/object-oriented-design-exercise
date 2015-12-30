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
        return "Error adding class %s" % class_id
  
    # add course
    new_course = Course(class_id, capacity, time)
    courses[class_id] = new_course
    
    return "Successfully added class %s" % class_id
 

def removeClass(class_id):
    # If the class is removed successfully,
    # return "Successfully removed class ID". 
    # Otherwise, return "Error removing class ID".
  
    # check if course already exists
    if courses.get(class_id, 0) == 0:
        return "Error removing class %s" % class_id

    # grab course info
    course = courses[class_id]
    student_list = course.students

    # remove course from courses
    del courses[class_id]

    # TODO: unenroll all enrolled students
    if student_list:
        for s_id in student_list:
            # update student's list of classes
            student = students[s_id]
            # find index of course in student's list of courses
            course_index = student.courses.index(class_id)
            student.courses.pop(course_index)
            # update item in students dictionary
            students[s_id] = student

    return "Successfully removed class %s" % class_id
    
  
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
        return "Class %s does not exist" % class_id

    course = courses.get(class_id)
    if not course.students:
        return "Class %s is empty" % class_id
    
    sorted_strings = [str(x) for x in sorted(course.students)]
    student_list = ",".join(sorted_strings)
    return_str = "Class %s has the following students: %s" % (class_id, student_list)

    return return_str

  
def addStudent(student_id, capacity, start, end):
    # If the student is added successfully, 
    # return "Successfully added student ID". 
    # Otherwise, return "Error adding student ID".
 
    if students.get(student_id, 0) != 0:
        return "Error adding student %s" % student_id
  
    # add student
    new_student = Student(student_id, capacity, start, end)
    students[student_id] = new_student
    
    return "Successfully added student %s" % student_id

  
def removeStudent(student_id):
    # If the student is removed successfully, 
    # return "Successfully removed student ID". 
    # Otherwise, return "Error removing student ID".
        # check if course already exists
    if students.get(student_id, 0) == 0:
        return "Error removing student %s" % student_id

    # grab student info
    student = students[student_id]
    course_list = student.courses

    # remove student from students
    del students[student_id]

    # TODO: unenroll student from all courses
    if course_list:
        for c_id in course_list:
            # update course's list of students
            course = courses[c_id]
            # find index of student in course's list of students
            student_index = course.students.index(student_id)
            course.students.pop(student_index)
            # update item in students dictionary
            course[c_id] = course

    return "Successfully removed student %s" % student_id

  
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

    # check if student already exists
    if students.get(student_id, 0) == 0:
        return "Student %s does not exist" % student_id

    student = students.get(student_id)
    if not student.courses:
        return "Student %s is not taking any classes" % student_id
    

    sorted_strings = [str(x) for x in sorted(student.courses)]
    course_list = ",".join(sorted_strings)
    return_str = "Student %s is taking the following classes: %s" % (student_id, course_list)

    return return_str

  
def enrollStudent(student_id, class_id):
    # If enrollment of the student in the class succeeded,
    # return "Number of free spots left in class CLASSID: FREESPOTS" 
    # where FREESPOTS is the number of free spots left 
    # in the class after the student enrolls. 
    # Otherwise, return "Enrollment of student STUDENTID in class CLASSID failed".

    fail_str = "Enrollment of student %s in class %s failed" % (student_id, class_id)
    # check student exists and class exists
    if students.get(student_id, 0) == 0 or courses.get(class_id, 0) == 0:
        return fail_str

    # check student not already enrolled in class
    student = students.get(student_id)
    if student.courses and class_id in student.courses:
        return fail_str

    # check student has capacity to enroll
    if student.courses and len(student.courses) == student.capacity:
        return fail_str

    # check class has capacity for student
    course = courses.get(class_id)
    if course.students and len(course.students) == course.capacity:
        return fail_str

    # check class time inside student's available time interval
    if course.time > student.end or course.time < student.start:
        return fail_str

    # check that student is not already taking a class at that time
    # get all course times for courses taken by student
    if student.courses:
        for c_id in student.courses:
            if courses[c_id].time == course.time:
                return fail_str

    # add student to course
    if course.students:
        course.students.append(student_id)
    else:
        course.students = [student_id]
    courses[class_id] = course

    # add course to student's course list
    if student.courses:
        student.courses.append(class_id)
    else:
        student.courses = [class_id]
    students[student_id] = student

    course_spots = course.capacity - len(course.students)
    return_str = "Number of free spots left in class %s: %s" % (class_id, course_spots)
    return return_str


def unenrollStudent(student_id, class_id):
    # If unenrollment of the student in the class succeeded,
    # return "Number of free spots left in class CLASSID: FREESPOTS" 
    # where FREESPOTS is the number of free spots left in the class 
    # after the student unenrolls. Otherwise, return "Unenrollment 
    # of student STUDENTID in class CLASSID failed".

    fail_str = "Unenrollment of student %s in class %s failed" % (student_id, class_id)
    # check student exists and class exists
    if students.get(student_id, 0) == 0 or courses.get(course_id, 0) == 0:
        return fail_str

    # check student already enrolled in class
    student = students.get(student_id)
    if class_id not in student.courses:
        return fail_str

    # remove student from course's students list
    course = courses.get(class_id)
    # find index of student and pop
    s_index = course.students.index(student_id)
    course.students.pop(s_index)
    courses[class_id] = course

    # remove course from student's courses list
    c_index = student.courses.index(class_id)
    student.courses.pop(c_index)
    students[student_id] = student

    course_spots = course.capacity - len(course.students)
    return_str = "Number of free spots left in class %s: %s" % (class_id, course_spots)
    return return_str


 