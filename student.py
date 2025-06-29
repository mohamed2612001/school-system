from person import *
import string
class Student(Person):
    
    grade_points={
    "A+":4.0,
    "A":3.7,
    "B+":3.3,
    "B":3.0,
    "C+":2.5,
    "C":2.0,
    "F":0.0
    }
 
    APPROVED_HOURS=14

    HOURS_OF_EACH_SUBJECT= {"mathematics":3,
    "physics":3,
    "english":4,
    "cs":2,
    "machine_learning":2}

    students=[]

    def __init__(self,name,age,ID,phone,email,address,grades_dict,department):
        """
        Initializes a Student object with personal and academic details.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            ID (str): The unique ID of the student.
            phone (str): The phone number of the student.
            email (str): The email address of the student.
            address (str): The address of the student.
            mathematics (int): The grade in mathematics.
            physics (int): The grade in physics.
            english (int): The grade in english.
            cs (int): The grade in cs.
            machine_learning (int): The grade in learning machine.
            department (str): The department of the student.
        """
        super().__init__(name,age,ID,phone,email,address)
        self.grades=grades_dict 
        self.department=department
        self.GBA=self.calculate_gpa()
        Student.students.append(self)
        
    @classmethod
    def get_grade_point_to_subject(cls,mark):
        if 90 <= mark <= 100:
            return cls.grade_points["A+"]
        elif 85 <= mark < 90:
            return cls.grade_points["A"]
        elif 80<= mark <85:
            return cls.grade_points["B+"]
        elif 70<= mark <80:
            return cls.grade_points["B"]
        elif 60<= mark <70:
            return cls.grade_points["C+"]
        elif 50<= mark <60:
            return cls.grade_points["C"]
        else:
            return cls.grade_points["F"]
        
    def calculate_gpa(self):
        """
        Calculates the GPA (Grade Point Average) of the student.

        Returns:
            float: The calculated GPA.
        """
        grade_points_of_all_subjects=map(lambda mark :Student.get_grade_point_to_subject(mark),self.grades.values())
        points=sum(map(lambda a,b: a*b,Student.HOURS_OF_EACH_SUBJECT.values(), grade_points_of_all_subjects))
        return points/Student.APPROVED_HOURS
        
    @classmethod
    def get_sutdent_by_id(cls,ID):
        """
        Retrieves a student's details by their ID.

        Args:
            ID (str): The unique ID of the student.

        Returns:
            dict: The student's details if found, otherwise None.
        """
        for stud in cls.students:
            if stud["ID"]==ID:
                return stud
        return None
    
    @classmethod
    def remove_student(cls,ID):
        """
        Removes a student from the list by their ID.

        Args:
            ID (str): The unique ID of the student to be removed.

        Returns:
            None
        """
        stud=cls.get_sutdent_by_id(ID)
        if stud:
            cls.students.remove(stud)
        else:
            print("this student not found")
            
    @staticmethod
    def get_department():
        while True:
            department=input("enter the department: ").strip()
            if not department or department in string.punctuation:
                print("please enter the department and doesnot use symbols")
            else:
                break
        return department
    
    @classmethod
    def get_grades(cls):
        """
        Collects grades from the user.
        
        Returns:
            dict: A dict containing grades for various subjects .
        """
        grades={}
        while True:
            try:
                print("enter the grades")
                for subject in cls.HOURS_OF_EACH_SUBJECT:
                    grade=int(input(f"enter the grade of {subject}").strip())
                    grades[subject]=grade
                
                return grades
            except ValueError:
                print("please enter grades in digit")
                
    @classmethod
    def get_answers_from_students(cls):
        """
        Collects personal and academic information for a student.

        Returns:
            tuple: A tuple containing personal and academic details of the student.
        """
        person=cls.get_answer_from_person()
        department=cls.get_department()
        grades=cls.get_grades()
        return (*person,grades,department)
    
    @classmethod
    def display_students(cls):
        print("Students: ")
        all_students=cls.students
        if all_students:
            for student in all_students:
                print(f"""name is {student.name}\nage  is {student.age}\nGBA is {student.GBA:.2f}""")
                student.display_grades()
        else:
            print("we aren't find any student")
            
    def display_grades(self):
        print("the grades are: ")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
            
