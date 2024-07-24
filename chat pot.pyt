
import random

def math_quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    print( f"What is {num1} {operator} {num2}?" )
    user_answer = input("Your answer: ")
    
    try:
        user_answer = int(user_answer)
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer}.")

    except ValueError:
        print("Please enter a valid number.")

while True :
  userinput =(input(">"))

  if userinput=="hi" or userinput ==  "hallo" :
    print("hi,wellcom to match chat pot.")

  elif userinput=="can you help me" :
    print("of corce ")
    print ("whate should i do for you ")

  elif userinput == "iam borde" or userinput == "can we have some entertainment":
    print("sure lets have some math ")
    math_quiz()

  elif userinput == "again" :
     math_quiz()

  elif userinput == "bye" :
            print("Goodbye!")
            break
  
  else : 
     print ("Sorry, I didn't understand that.") 