print("Hello World")
name = "Maria Solis"
name1 = "Jalen Solis"
print(name,"and" ,name1)

#dictionaries {}
person =  {
    "key" : "value",
    "name" : "Jay",
    "From" : "Hawaii"
    }
print(person["From"])

#tuple can not alter ()
kids = ("Maria", "Jalen")

#set {} unique values and does not remember order
foods = {"Pizza", "Tacos", "Ice Cream", "Pizza", "Pizza", "Tacos"}
print(foods)

#booleans
is_adult = True

#integer
age = 30

#float
pi = 3.14

#indexing

#from string start at 0
print(len(name))
print(name[0:5]) #Substring start at M and stop at space

#list start at 0 : end 
groceries = ["Milk", "Eggs", "Ice Cream", "Coke", "Coffee"]
print(groceries[0:2]) #stop at 2

#function
def thing():
    """
    Hello this is a docstring comment
    """
    pass


#string formatting
new_name = "Python"
course = "{} for everybody".format(new_name)
print(course)
print(f"the course is {new_name}")#newer
print("This %s" % "also works") #older

#files
with open("try.py", "w") as file_handler:
    file_handler.write("print('Ayo it works')") #writes a command
    file_handler.close()

with open("try.py", "r") as file_reader:
    content = file_reader.read()
    file_reader.close()

print(content)

#comparison op
maria = "in love with Jalen"
if maria == "Hates Jalen":
    print("Yes you do")
elif maria == "Does not like Jalen":
    print("of course")
else:
    print(f"Ya sureeee, you are {maria}")

#for loop
for item in groceries:
    print(f"The item is {item}")
for letter in name:
    print(f"{letter}")
for letter in name:
    l = letter.lower()
    if l in 'aeiouy':
        print(f"Vowel is: {l}")
        continue
    if l == "s":
        print("Found the S")
        break

#while loop
num = 0

while num < 10:
    print(num)
    num= num+1

#list comprehension
nums = [1,2,3,4,5,6,7,8,9,10] #list
times_ten = [num*10 for num in nums]
print(times_ten)
times_ten_condition = [num*10 for num in nums if num%2 == 0]
print(times_ten_condition)

#functions with return
def maria(who):
    return "Maria Hates " + who
print(maria("Jalen"))

#functions without return
def maria_hates(hates, loves):
    print(f"Maria absolutely hates {hates}, and loves {loves}")
maria_hates("Jalen", "some other hoe")

#class 
class Person:
    loves = "Maria"
jalen = Person()
print(jalen.loves)

class Lover:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
    def loves_who(self):
        print(f"Who do you love {self.name}?")
    def get_food(self):
        print(f"i want to eat {self.food}")
    def __str__(self):
        return self.name + " is the best"

Maria  = Lover("Maria", 21, "Tacos")
Maria.get_food()
print(Maria)

#try and except
try:
    1/0
except Exception as e:
    print(e)
    print(type(e))
