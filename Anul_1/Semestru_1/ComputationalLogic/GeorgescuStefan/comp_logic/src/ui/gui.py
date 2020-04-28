import traceback

from tkinter import *
from tkinter import messagebox

from domain.conversions import substitution_method, rapid_conversions, successive_divisions, intermediate_base
from domain.operations import addition, subtraction, multiply, division, get_decimal_value
from domain.util import strip_insignificant_zeros

"""
This part of the code only represents the graphical user interface and is completely independent from 
the code required to solve the tasks. As a consequence, I will only comment the methods that are relevant
to the problem statement. 
"""


class GUI:
    def __init__(self):
        self.master = Tk()
        self.master.title("Operations and Conversions with Arbitrary Bases")

        self.operation_title = Label(self.master, text="Operations")
        self.operation_title.grid(row=0, column=0)
        self.number1_label = Label(self.master, text="Number 1: ")
        self.number1_label.grid(row=1, column=0, pady=5)
        self.number1_field = Entry(self.master, width=10)
        self.number1_field.grid(row=1, column=1)
        self.number2_label = Label(self.master, text="Number 2: ")
        self.number2_label.grid(row=2, column=0, pady=5)
        self.number2_field = Entry(self.master, width=10)
        self.number2_field.grid(row=2, column=1)
        self.base_label = Label(self.master, text="Base")
        self.base_label.grid(row=3, column=0, pady=5)
        self.base_selector = Entry(self.master, width=2)
        self.base_selector.grid(row=3, column=1)
        self.addition_button = Button(self.master, text="Add", command=self.addition_button_pressed)
        self.addition_button.grid(row=4, column=0, pady=5)
        self.subtraction_button = Button(self.master, text="Subtract", command=self.subtraction_button_pressed)
        self.subtraction_button.grid(row=5, column=0, pady=5)
        self.multiply_button = Button(self.master, text="Multiply", command=self.multiply_button_pressed)
        self.multiply_button.grid(row=4, column=1)
        self.divide_button = Button(self.master, text="Divide", command=self.divide_button_pressed)
        self.divide_button.grid(row=5, column=1)
        self.result_operations_label = Label(self.master, text="Result:")
        self.result_operations_label.grid(row=6, column=0, pady=5)
        self.result_operations_field = Entry(self.master, width=20)
        self.result_operations_field.grid(row=6, column=1)

        self.clear_operations_button = Button(self.master, text="Clear", command=self.clear_operations_button_pressed)
        self.clear_operations_button.grid(row=7, column=0, pady=5)

        self.conversions_title = Label(self.master, text="Conversions")
        self.conversions_title.grid(row=0, column=2, pady=(20, 30))
        self.number_label = Label(self.master, text="Number: ")
        self.number_label.grid(row=1, column=2)
        self.number_field = Entry(self.master, width=10)
        self.number_field.grid(row=1, column=3)
        self.source_base_label = Label(self.master, text="Source Base:")
        self.source_base_label.grid(row=2, column=2)
        self.source_base_selector = Entry(self.master, width=2)
        self.source_base_selector.grid(row=2, column=3)
        self.destination_base_label = Label(self.master, text="Destination Base:")
        self.destination_base_label.grid(row=3, column=2, padx=80)
        self.destination_base_selector = Entry(self.master, width=2)
        self.destination_base_selector.grid(row=3, column=3)
        self.convert_button = Button(self.master, text="Convert", command=self.convert_button_pressed)
        self.convert_button.grid(row=4, column=3)
        self.convert_with_intermediate_button = Button(self.master, text="Convert with intermediate", command=self.convert_with_intermediate_button_pressed)
        self.convert_with_intermediate_button.grid(row=5, column=3)
        self.result_conversions_label = Label(self.master, text="Result:")
        self.result_conversions_label.grid(row=6, column=2)
        self.result_conversions_field = Entry(self.master, width=10)
        self.result_conversions_field.grid(row=6, column=3)
        self.result_conversions_field.configure(state=DISABLED)

        self.clear_conversions_button = Button(self.master, text="Clear", command=self.clear_conversions_button_pressed)
        self.clear_conversions_button.grid(row=7, column=2)
    
        self.author_label = Label(self.master, text="Developed by Stefan Georgescu")
        self.author_label.grid(row=8, column=4)
        self.exit_button = Button(self.master, text="EXIT", foreground='red', command=self.exit_button_pressed)
        self.exit_button.grid(row=0, column=4)

    def __get_operations_data(self):
        return self.number1_field.get(), self.number2_field.get(), self.base_selector.get()

    def __perform_conversion(self, method, number, source_base, destination_base):
        self.result_conversions_field.configure(state='normal')
        self.result_conversions_field.delete(0, len(self.result_conversions_field.get()))
        self.result_conversions_field.insert(END, strip_insignificant_zeros(method(number, source_base, destination_base)))
        self.result_conversions_field.configure(state='readonly')

    def __perform_operation(self, operation, number1, number2, base):
        self.result_operations_field.configure(state='normal')
        self.result_operations_field.delete(0, len(self.result_operations_field.get()))
        self.result_operations_field.insert(END, strip_insignificant_zeros(operation(number1, number2, base)))
        self.result_operations_field.configure(state='readonly')
        
    def addition_button_pressed(self):
        number1, number2, base = self.__get_operations_data()
        try:
            base = int(base)
            if not self.__base_validator(base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number1, base) or not self.__fits_base(number2, base):
                    messagebox.showinfo("Error", "One of the numbers does not fit the base.")
                else:
                    self.__perform_operation(addition, number1, number2, base)
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")

    def subtraction_button_pressed(self):
        number1, number2, base = self.__get_operations_data()
        try:
            base = int(base)
            if not self.__base_validator(base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number1, base) or not self.__fits_base(number2, base):
                    messagebox.showinfo("Error", "One of the numbers does not fit the base.")
                else:
                    self.__perform_operation(subtraction, number1, number2, base)
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")
    
    def multiply_button_pressed(self):
        number1, number2, base = self.__get_operations_data()
        try:
            base = int(base)
            if not self.__base_validator(base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number1, base) or not self.__fits_base(number2, base):
                    messagebox.showinfo("Error", "One of the numbers does not fit the base.")
                else:
                    if len(number2) != 1:
                        messagebox.showinfo("Error", "This program can only multiply by one digit.")
                    else:
                        self.__perform_operation(multiply, number1, number2, base)
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")
            traceback.print_exc()

    def divide_button_pressed(self):
        number1, number2, base = self.__get_operations_data()
        try:
            base = int(base)
            if not self.__base_validator(base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number1, base) or not self.__fits_base(number2, base):
                    messagebox.showinfo("Error", "One of the numbers does not fit the base.")
                else:
                    if len(number2) != 1:
                        messagebox.showinfo("Error", "This program can only multiply by one digit.")
                    else:
                        self.result_operations_field.configure(state='normal')
                        self.result_operations_field.delete(0, len(self.result_operations_field.get()))
                        result, remainder = division(number1, number2, base)
                        self.result_operations_field.insert(END, result + ' remainder ' + remainder)
                        self.result_operations_field.configure(state='readonly')
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")
    
    def clear_operations_button_pressed(self):
        self.number1_field.delete(0, len(self.number1_field.get()))
        self.number2_field.delete(0, len(self.number2_field.get()))
        self.base_selector.delete(0, len(self.base_selector.get()))
        self.result_operations_field.configure(state='normal')
        self.result_operations_field.delete(0, len(self.result_operations_field.get()))
        self.result_operations_field.configure(state='readonly')

    def convert_button_pressed(self):
        number = self.number_field.get()
        source_base = self.source_base_selector.get()
        destination_base = self.destination_base_selector.get()
        try:
            source_base = int(source_base)
            destination_base = int(destination_base)
            if not self.__base_validator(source_base) or not self.__base_validator(destination_base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number, source_base):
                    messagebox.showinfo("Error", "The number does not fit the source base.")
                else:
                    if self.__is_rapid(source_base, destination_base):
                        self.__perform_conversion(rapid_conversions, number, source_base, destination_base)
                        messagebox.showinfo("Success", "The result has been computed using rapid conversions.")
                    elif source_base < destination_base:
                        self.__perform_conversion(substitution_method, number, source_base, destination_base)
                        messagebox.showinfo("Success", "The result has been computed using the substitution method.")
                    else:
                        self.__perform_conversion(successive_divisions, number, source_base, destination_base)
                        messagebox.showinfo("Success", "The result has been computed using successive divisions.")
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")
    
    def convert_with_intermediate_button_pressed(self):
        number = self.number_field.get()
        source_base = self.source_base_selector.get()
        destination_base = self.destination_base_selector.get()
        try:
            source_base = int(source_base)
            destination_base = int(destination_base)
            if not self.__base_validator(source_base) or not self.__base_validator(destination_base):
                messagebox.showinfo("Error", "This program can only work with bases 2 to 10 and 16.")
            else:
                if not self.__fits_base(number, source_base):
                    messagebox.showinfo("Error", "The number does not fit the source base.")
                else:
                    mid_result, final_result = intermediate_base(number, source_base, destination_base)
                    messagebox.showinfo("Success", "The result has been computed using 10 as an intermediate base and "
                                                   "the corresponding value is {0}".format(mid_result))
                    self.result_conversions_field.configure(state='normal')
                    self.result_conversions_field.delete(0, len(self.result_conversions_field.get()))
                    self.result_conversions_field.insert(END, final_result)
                    self.result_conversions_field.configure(state='readonly')
        except ValueError:
            messagebox.showinfo("Error", "Base must be an int.")
    
    def clear_conversions_button_pressed(self):
        self.number_field.delete(0, len(self.number_field.get()))
        self.source_base_selector.delete(0, len(self.source_base_selector.get()))
        self.destination_base_selector.delete(0, len(self.destination_base_selector.get()))
        self.result_conversions_field.configure(state='normal')
        self.result_conversions_field.delete(0, len(self.result_conversions_field.get()))
        self.result_conversions_field.configure(state='readonly')
        
    def exit_button_pressed(self):
        messagebox.showinfo("Credits", "Application developed by Stefan Georgescu, student at the Faculty of "
                                       "Mathematics and Informatics, group number 913. \n \nAny unauthorised use of "
                                       "this code will upset the developer. \n \nThank you!")
        self.master.quit()

    @staticmethod
    def run_app():
        mainloop()

    @staticmethod
    def __fits_base(number, base):
        """
        Checks if a number can be a representation in a given base
        :param number: a string
        :param base: an int
        :return: True if all the digits are smaller than the base, false otherwise
        """
        for digit in number:
            if get_decimal_value(digit) >= base:
                return False
        return True
    
    @staticmethod
    def __base_validator(base):
        """
        Checks if a given base is valid for the problem statement
        :param base: an int
        :return: True or False
        """
        if base < 2:
            return False
        if base in range(11, 16):
            return False
        if base > 16:
            return False
        return True

    @staticmethod
    def __is_rapid(base1, base2):
        """
        Checks if two bases are powers of two
        :param base1: an int
        :param base2: an int
        :return: True or False
        """
        powers_of_2 = [2, 4, 8, 16]
        if base1 not in powers_of_2:
            return False
        if base2 not in powers_of_2:
            return False
        return True
