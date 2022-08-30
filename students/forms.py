from dataclasses import fields
from tkinter import Widget
from   django import forms
from .models import Student
import attrs
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {'student_number', 'first_name', 'last_name', 'email', 'fieid_of_study', 'gpa'}
        labels = {
            'student_number': 'Student_Number',
            'first_name': 'First_Name',
            'last_name': 'Last_Name',
            'email': 'Email',
            'fieid_of_study': 'Field_of_Study',
            'gpa': 'GPA'
        }

          
                