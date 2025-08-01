# # pratice 1 

# username = str(input("Enter your firstname : "))

# print(len(username))

# # pratice 2 

# string  =  """You cannot be sure how HTML will be displayed.

# Large or small screens, and resized windows will create different results.

# With HTML, you cannot change the display $ by adding extra spaces or extra lines in your HTML code.

# The browser will automatically remove any extra spaces and lines when the page is displayed"""

# # print(string[(int(string.find("create"))-1) : int(string.find("$"))])
# print(string.count("$"))

# conditions pactice 

# prctice 1 

# inputNum = int(input("Please enter a number : "))
# # print(inputNum % 2)
# if (inputNum % 2 == 0) : print("This is even nuber")
# else : print("This is odd nuber")

# Pratice 2


# print("Input your three number, those number should be deffirent")

# numone = int(input("Num one : "))
# numtwo = int(input("Num two : "))
# numthree = int(input("Num thee : "))


# if numone >= numtwo and numone >= numthree: print("Number one is bigger then others")
# elif numtwo >=  numthree  : print("Number two is bigger then others")
# else : print("Number three is bigger then others")

# num = int(input("Enter a number : "))

# if num % 7 == 0 : print("Yes it's possbile to multiply with 7 also resutl is = ", num * 7)
# else : print("Not possilbe to multiply by 7")


# list and truble 

# marks = [52.5, 21.5, 16.54, 45.8, 44.5, 46.54, 4.4]
# marks.append(5)
# marks.sort()

# marks.remove(4.4)
# print(marks)

# practice 1 
# movelist = []

# move1 = input("Enter you first favorit move : ")
# move2 = input("Enter you second favorit move : ")
# move3 = input("Enter you third favorit move : ")

# movelist.append(move1)
# movelist.append(move2)
# movelist.append(move3)

# print(movelist)

# practice 2

number = [1,4,7,5,74,4,1]

cpNumber = number.copy()
cpNumber.reverse()
print(cpNumber)


if number == cpNumber : print("This list of Palindrome")
else : print("This list is not palindrome")