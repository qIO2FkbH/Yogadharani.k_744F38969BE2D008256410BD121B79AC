Class student:



  Def __init__(self, name, roll_number, cgpa):

     Self.name = name

     Self.roll_number = roll_number

     Self.cgpa=cgpa





Def sort_student(student_list):

  # sort the list of students in descending order of CGPA

  Sorted_students = sorted(student_list,

                        Key=lambda student: student.cgpa, 

                         Reverse=True)

  #syntax _ lambda arg:exp

  Return sorted_students





#Example usage:

Students = [

     Student(“Stephen”, “A123”, 7.8),

     Student(“Karthik”, “A124”, 8.9),

     Student(“Santhosh”, “A125”, 9.1),

     Student(“Komban”, “A126”, 9.9),

 ]



Sorted_students = sort_student(students)



 # Print the sorted list of students

For students in sorted_students:

  Print(“Name: {}, Roll Number: {}. CGPA  {}”.format(students.name,

                                           Students.roll_number 
                           Students.cgpa)￼•
