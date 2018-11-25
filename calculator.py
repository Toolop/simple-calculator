print("Welcome")

run = True

while run: 
  print()
  a = int(input("Input value of A = "))
  b = int(input("Input value of B = "))
  c = a + b
  print("A + B = ", c)
  
  ans = input("Want to this again? (Y/N) ").upper()
  
  if ans == "Y":
    run = True
  elif ans == "N":
    run = False

print()
print("Bye")
