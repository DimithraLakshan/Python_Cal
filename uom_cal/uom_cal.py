import os
def history(num1, choice, num2,claculation):
    his_file = open("history.txt", "a")
    his_file.write(str(num1) + " " + str(choice) + " " + str(num2) + "=" + str(claculation) + "\n")
    #his_file.write("{} {} {} = {}".format(str(num1), str(choice), str(num2), str(claculation)))
    



def add(a,b):
  return a+b
  
def subtract(a,b):
  return a-b
  
def multiply (a,b):
  return a*b

def divide(a,b):
  try:
    return a/b
  except Exception as e:
    print(e)
def power(a,b):
  return a**b
  
def remainder(a,b):
  return a%b
  
def select_op(choice):
  if (choice == '#'):
    return -1
  elif (choice == '$'):
    return 0
  elif (choice in ('+','-','*','/','^','%','?')):
    if choice == '?':
        if os.path.getsize('history.txt') == 0:
                print('File is empty')
        else:
            his_file = open("history.txt", "r")
            my_txt = his_file.read()
            print(my_txt)
            #his_file.close()
        
        
        return
    while (True):
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    result = 0.0
    #last_calculation = ""
    if choice == '+':
      result = add(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
      history(num1, choice, num2, add(num1, num2))
    elif choice == '-':
      result = subtract(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
      history(num1, choice, num2, subtract(num1, num2))
    elif choice == '*':
      result = multiply(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
      history(num1, choice, num2, multiply(num1, num2))
    elif choice == '/':
      result =  divide(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
      history(num1, choice, num2, divide(num1, num2))
    elif choice == '^':
      result = power(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
      history(num1, choice, num2, power(num1, num2))
    elif choice == '%':
      result = remainder(num1, num2)
      print(num1, " ", choice, " ", num2, " = ", result)
     


    #elif choice == '?':
     #   his_file = open("history.txt", "r")
      #  my_txt = his_file.read()
       # print(my_txt)
        #his_file.close()
    else:
      print("Something Went Wrong")
      
    #last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
    #print(last_calculation )
    
  else:
    print("Unrecognized operation")
    
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    file = open("history.txt", "r+")
    file. truncate(0)
    file. close()
    exit()