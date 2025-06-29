from person import *

class Teacher(Person):
    """
    Represents a teacher, inheriting from the Person class.
    """
    teachers=[]
    def __init__(self,name,age,ID,phone,email,address,classes,hour_rate,hours_work):
        """
        Initializes a Teacher object with personal and professional details.

        Args:
            name (str): The name of the teacher.
            age (int): The age of the teacher.
            ID (str): The unique ID of the teacher.
            phone (str): The phone number of the teacher.
            email (str): The email address of the teacher.
            address (str): The address of the teacher.
            classes (list): The classes the teacher teaches.
            hour_rate (int): The hourly rate of the teacher.
            hours_work (int): The number of hours the teacher works.
        """
        super().__init__(name,age,ID,phone,email,address)
        self.classes=classes
        self.hour_rate=hour_rate
        self.hours_work=hours_work
        Teacher.teachers.append(self)
        
    def add_teacher_to_list(self):
        """
        Adds the teacher's details to the list of teachers.
        """
        self.person["classes"]=self.classes
        self.person["hour_rate"]=self.hour_rate
        self.person["hours_work"]=self.hours_work
        Teacher.teachers.append(self.person)
        
    @staticmethod
    def get_teacher_by_id(ID):
        """
        Retrieves a teacher's details by their ID.

        Args:
            ID (str): The unique ID of the teacher.

        Returns:
            dict: The teacher's details if found, otherwise None.
        """
        for teacher  in Teacher.teachers:
            if teacher["ID"]==ID:
                return teacher
            return None
        
    @classmethod
    def remove_teacher(cls,ID):
        """
        Removes a teacher from the list by his/her ID.

        Args:
            ID (str): The unique ID of the teacher to be removed.

        Returns:
            None
        """
        teacher=cls.get_teacher_by_id(ID)
        if teacher:
            cls.teachers.remove(teacher)
        else:
            print("we cannot found this teacher")
            
    def calculate_salary(self):
        """
        Calculates the teacher's salary based on their hourly rate and hours worked.

        Returns:
            int: The calculated salary.
        """
        return self.hour_rate*self.hours_work
    
    @classmethod
    def get_answers_from_teacher(cls):
        """
        Collects personal and professional information for a teacher.

        Returns:
            tuple: A tuple containing personal details, classes taught, hourly rate, and hours worked.
        """
        person=cls.get_answer_from_person()
        
        classes=cls.get_classes_from_teacher()

        hour_rate,hours_work=cls.get_hourly_rate_hours_work()      
        return (*person,classes,hour_rate,hours_work)
    
    @classmethod
    def get_classes_from_teacher(cls):
        number_of_classes=cls.get_number_of_classes()
        classes=[]
        for i in range(number_of_classes):
            class_name=input(f"enter class {i+1}: ")
            classes.append(class_name)
            
    @staticmethod
    def get_number_of_classes():
        while True:
            try:
                number_of_classes=int(input("enter the number of classes that teacher will teach").strip())
                return number_of_classes
            except ValueError:
                print("please enter valid number")
                
    @staticmethod
    def get_hourly_rate_hours_work():
        """
        Collects the hourly rate and hours worked for a teacher.

        Returns:
            tuple: A tuple containing the hourly rate and hours worked.
        """
        while True:
            try:
                hour_rate=int(input("hour rate :"))
                hours_work=int(input("hours_work: "))
                return (hour_rate,hours_work)
            except ValueError:
                print("please enter hour_rate and hours_rate in digits")
                
    @classmethod
    def display_teachers(cls):
        print("Teachers: ")
        all_teachers=cls.teachers
        if all_teachers:
            for teacher in all_teachers:
                print(f"name is {teacher.name}\nslalay is {teacher.calculate_salary()}")
                teacher.display_classes()
    
    def display_classes(self):
        print("the classes he teaches are :")
        for index ,class_number in enumerate(self.classes,1):
            print(f"{index}: {class_number} ")
            
                