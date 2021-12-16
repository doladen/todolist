myToDo =['finish missing assignments', 'buy some cat food','clean my room ']
print(myToDo)
print(len(myToDo))
print(myToDo.index('buy some cat food'))
print('myToDo')
print(f'{len(myToDo)} thing(s) left to do')
for task in myToDo:
  print(task)
myToDo.append('learn more coding')
print(len(myToDo))
for task in myToDo:
  print(task)
myToDo.remove('learn more coding')
for task in myToDo:
  print(task)
if len(myToDo) == 3:
  print("what would you like to add?")
  add = input()
  myToDo.append(add)

  print("My To Do List")
  #PRINT LENGTH OF TO DO LIST
  print(f'{len(myToDo)} thing(s) left to do')


def addtolist(speedy):
  myToDo.append(speedy)
def removefromlist(speedy):
  myToDo.remove(speedy)
def checkthe

myToDo =[] 
addtolist("christmas shopping")
addtolist("Make dinner")
addtolist("christmas shopping")
addtolist("Wrap gifts")
removefromlist("christmas shopping")
for task in myToDo:
  print(task)