from Exception import *
import re
class Person:
    """
    Represents a person with basic personal details such as name, age, ID, phone, email, and address.
    """
    def __init__(self,name,age,ID,phone,email,address):
        """
        Initializes a Person object with personal details.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            ID (str): The unique ID of the person.
            phone (str): The phone number of the person.
            email (str): The email address of the person.
            address (str): The address of the person.
        """
        self.name=name
        self.age=age
        self.__ID=ID
        self.__phone=phone
        self.__email=email
        self.address=address

                
    def __str__(self):
        return f" {self.name} his age{self.age} lived in {self.address} his number {self.__phone}"
    
    def __repr__(self):
        """
        Returns a detailed string representation of the person's details for debugging.

        Returns:
            str: A formatted string with all the person's attributes.
        """
        return f"{self.__class__.__name__} name:{self.name}\
            age:{self.age}\
            ID:{self.__ID}\
            phone:{self.__phone}\
            email:{self.__email}\
            address:{self.address}"
            
    @staticmethod
    def is_valid_phone(new_phone):
        """
        Validates a phone number.

        Args:
            new_phone (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid, otherwise raises a PhoneError.

        Raises:
            PhoneError: If the phone number is not 11 digits or does not start with "01".
        """
        if isinstance(new_phone,str) and len(new_phone)==11 and new_phone.startswith("01"):
            return True
        
        raise PhoneError(f"this phone should be 11 digits and starts with 01")
        
    @staticmethod
    def is_valid_email(new_email):
        """
        Validates an email address.

        Args:
            new_email (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, otherwise raises an EmailError.

        Raises:
            EmailError: If the email address does not match the required pattern.
        """
        pattern_email=r"[\w\.\d]+@.+\.[\w]+"
        new_email=re.findall(pattern_email,new_email)
        if new_email:
            return True
        raise EmailError(f"invalid email")
    
    @staticmethod
    def is_valid_id(id):
        """
        Validates an ID.

        Args:
            id (str): The ID to validate.

        Returns:
            bool: True if the ID is valid, otherwise raises an IdError.

        Raises:
            IdError: If the ID is not 14 digits.
        """
        if len(id)==14:
            return True
        raise IdError(f"id should be 14 digits")
    
    @property
    def phone(self):
        """
        Gets the phone number of the person.

        Returns:
            str: The phone number.
        """
        return self.__phone
    
    @phone.setter
    def phone(self,new_phone):
        """
        Sets a new phone number for the person after validation.

        Args:
            new_phone (str): The new phone number to set.
        """
        if Person.is_valid_phone(new_phone):
           self.__phone=new_phone
       
    @property
    def email(self):
        """
        Gets the email address of the person.

        Returns:
            str: The email address.
        """
        return self.__email
    
    @email.setter
    def email(self,new_email):
        """
        Sets a new email address for the person after validation.

        Args:
            new_email (str): The new email address to set.
        """
        if Person.is_valid_email(new_email):
            self.__email=new_email
            
    @property
    def ID(self):
        """
        Gets the ID of the person.

        Returns:
            str: The ID.
        """
        return self.__ID
    
    @ID.setter
    def ID(self,new_ID):
        """
        Sets a new ID for the person after validation.

        Args:
            new_ID (str): The new ID to set.
        """
        if Person.is_valid_id(new_ID):
            self.__ID=new_ID
    @staticmethod
    def get_answer_from_person():
        """
        Collects general personal information for a person (student or teacher).

        Returns:
            tuple: A tuple containing name, age, ID, phone, email, and address.
        """
        while True:
            try:        
                name=input("enter the name")
                address=input("enter the  address")
                age=input("age: ")
                phone=input("phone: ")
                email=input("email:")
                ID=input("ID: ")
                Person.is_valid_email(email)
                Person.is_valid_phone(phone)
                Person.is_valid_id(ID)
                return (name,age,ID,phone,email,address)
            except (ValueError, PhoneError, EmailError, IdError) as e:
                print(f"wrong {e}")
                print("try again")