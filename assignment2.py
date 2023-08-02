
#1. LIST
#Write a PYTHON script with List comprehension for the following
#a) Is the given list divisible by 3 or NOT?
#b) Square of even numbers in a list
#c) Sum of digits of all EVEN numbers in a list
#d) Remove duplicate numbers in a list
#a
numbers=[22,34,22,54,10,9,33,12]
divisble=[num for num in numbers if num%3==0]
print(divisble)

#b
numbers=[22,34,23,9,8,10,33]
square=[num**2 for num in numbers if num%2==0]
print(square)


#c
numbers=[220,23,66,55,77,88]
sum_even=sum([num**2 for num in numbers if num%2==0])
print(sum_even)

#d
numbers=[22,33,44,55,22,19,20,20]
print("original:",numbers)
unique=[]
[unique.append(num) for num in numbers if num not in unique]
print("after removing duplicates",unique)

#Create a dictionary to store the details of your company employees (name as key and birthdate as value).
#Write a function birthDate() that takes the full name of your employees(as a string) and
#displays
employee_details = {
    'Virat Kohli': '5 November 1988',
    'Umesh Yadav': '25 October 1987',
    'Manish Pandey': '10 September 1989',
    'Rohit Sharma': '30 April 1987',
    'Ravindra Jadeja': '6 December 1988',
    'Hardik Pandya': '11 October 1993'
}

def getting_name(name):
    return employee_details.get(name)
    
print(getting_name('Umesh Yadav'))

