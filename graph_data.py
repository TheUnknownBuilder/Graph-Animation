#xy coord 
#adjacent node list (list indexes)
#we can add more node elements later
graph = [ 
# Node 0
[ (50, 210), # x,y position
  (1, 2, 4, 6, 7) # adjacent nodes
],
# Node 1
[ (50, 350), 
  (0, 3)
],
[ (100, 420), # Node 2
  (0, 1, 2, 5, 9, 10)
],
[ (210, 50), # Node 3
  (11, 8, 6)
],
[ (210, 210), # Node 4
  (0, 6, 7, 11, 12)
],
[ (210, 490), # Node 5
  (3, 10)
],
[ (280, 140), # Node 6
  (0, 2, 3, 4, 11)
],
[ (280, 280), # Node 7
  (0, 4, 9, 12)
],
[ (350, 170), # Node 8
  (11, 3)
],
[ (350, 350), # Node 9
  (2, 7, 10, 12, 13, 15)
],
[ (350, 490), # Node 10
  (2, 5, 9, 13, 14, 15)
],
[ (420, 160), # Node 11
  (3, 4, 6, 8, 12, 16, 17)
],
[ (420, 300), # Node 12
  (4, 7, 9, 11, 17)
],
[ (420, 420), # Node 13
  (9, 10, 15)
],
[ (500, 500), # Node 14
  (10, 18, 15)
],
[ (560, 420), # Node 15
  (9, 10, 13, 14, 17, 18)
],
[ (630, 750), # Node 16
  (17, 11)
],
[ (630, 210), # Node 17
  (11, 12, 15, 16, 18)
],
[ (750, 320), # Node 18
  (17, 14, 15)
],
]