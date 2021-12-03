import circles
import addEdges
import fullAnimation

prompt = """Enter a number:\n
  circles: 1  - basic drawing skills in pygame\n
  add edges: 2 - adding graph edges to drawing\n
  full animation: 3 - full animation to the graph
  """
  
choice = input(prompt)

if choice == '1': circles.run()
if choice == '2': addEdges.run()
if choice == '3': fullAnimation.run()

print("run again and type 1, 2, or 3 only")