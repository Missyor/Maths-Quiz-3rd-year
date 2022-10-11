##Creating a maths quiz with python 

##Task1 Create a message welcoming people to your quiz. 
print("Welcome to my quiz") 

##Task2 Create a variable asking the user for their name 
userName = input("Enter your name: ")
 
##Task3 Print a message that says "Hello *user* good luck with the maths quiz" 
print("Hello",userName, "good luck with the maths quiz" )
 
##We will create an algebra quiz  so we need 10 questions 
##TASK4 Print your first question 
print("What is 2x + 3x")

##Task 5 Create a variable called answer and ask the user to input an answer. 
answer = input("Enter your answer: ")
 
##Create a variable called correctAnswer and set it equal to the correct answer 
correctAnswer = "5x" 

## Task 6  NEW CODE if the answer = correctAnswer print "You're Correct", otherwise print ("Incorrect") 
### Using conditional statement - if/else
if answer == correctAnswer:
  print("Well Done!", userName)
else:
  print("Hard luck", userName)
##Task 7 Repeat steps 4 to 6 to make 10 questions. 
##Task8  After the 10 questions print a message to say "Thank you *user *for playing my quiz" 