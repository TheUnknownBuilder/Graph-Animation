import circles
import addEdges
import fullAnimation

prompt = """
BFS Visualiser

Enter 1 for circles: basic drawing skills in pygame
Enter 2 to add edges: adding graph edges to drawing
Enter 3 to see full animation

Enter option
  """
# keepRunning = True

# while (keepRunning):
choice = input(prompt)

if choice == '1': circles.run()
elif choice == '2': addEdges.run()
elif choice == '3': fullAnimation.run()
else: print("run again and type 1, 2, or 3 only")

# userInp =  input ("Enter 0 to exit, any key to continue")

# print(userInp)
# keepRunning = True
