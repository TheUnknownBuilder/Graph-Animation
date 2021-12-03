import circles
import addEdges

prompt = """Enter a number:\n
  circles: 1  - basic drawing skills in pygame\n
  add edges: 2 - adding graph edges to drawing
  """
  
choice = input(prompt)

if choice == '1': circles.run()
if choice == '2': addEdges.run()

print("run again and type 1, 2, or 3 only")