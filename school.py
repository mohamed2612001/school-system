
from student import *
from teacher import *

class School:
    def __init__(self,name,address,built_in):
        """
        Initializes a School object with its name, address, and year built.
        Args:
            name (str): The name of the school.
            address (str): The address of the school.
            built_in (int): The year the school was built.
        """
        self.name=name
        self.address=address
        self.built_in=built_in
        
    @staticmethod
    def to_continue():
        """
        Asks the user if they want to continue adding students or teachers.

        Returns:
            bool: True if the user wants to continue, False otherwise.
        """
        while True:
            ans=input("enter (y) if you want to add another student or enter (n)").lower().strip()
            match ans:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("invalid choice please enter (y or n)")
                    

    
    def add_students(self):
        """
        Adds students to the school by collecting their details and creating Student objects.
        """
        while True:
            answers=Student.get_answers_from_students()
            Student(*answers)
            Continue=School.to_continue()
            if not Continue:
                break                

    def delete_student(self,ID):
        """
        Deletes a student from the school using their ID.

        Args:
            ID (str): The ID of the student to be removed.
        """
        Student.remove_student(ID)
        
    def add_teachers(self):
        """
        Adds teachers to the school by collecting their details and creating Teacher objects.
        """
        while True:
            answers=School.get_answers_from_teacher()
            Teacher(*answers)
            Continue=School.to_continue()
            if not Continue:
                break     
    
    def display_students(self):
        Student.display_students()
        
    def display_teachers(self):
        Teacher.display_teachers()
               
               

                


    

            
     
grades= {"mathematics":70,
"physics":80,
"english":90,
"cs":90,
"machine_learning":95}
school=School("mohamed","2-street",12)
student=Student("mohamed","16","11111111111111","01551548192","mohamed.sobhy@gmail.com","street",grades,"cs")
teacher=Teacher("mohamed","16","11111111111111","01551548192","mohamed.sobhy@gmail.com","street",[2,5,7,8],10,100)
school.display_teachers()
school.display_students()

            
        
        

