print("Age Counter")
for i in range(3):
    print("")

#create the variables first to make global-variable
birthyear = 0
year = 0
age = 0

#create the function to count the age
def count():   
    birthyear = int(input("Birth year: "))
    year = int(input("Count your age when: "))
    age = year - birthyear

#show the result
print("your age is:")
print (str(age))

#Ok, if there's an error or something wrong, I'm so sorry
    
