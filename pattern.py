# Loop from 1 to 5
for i in range(1,6):
  
  # Nested loop from 1 to i and print a star without a space
  for j in range(1,i+1):
    print("*",end="")
  print()

# Loop from 4 to 0
for i in range(4,0,-1):
  
  # Nested loop from 1 to i and print a star without a space
  for j in range(1,i+1):
    print("*",end="")
  print()
