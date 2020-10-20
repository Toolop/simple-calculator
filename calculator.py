print("--- Welcome ---")    //tambah komen diatas 

run = True

while run:
  print()
  print("Menu\n1. (+)\n2. (-)\n3. (*)\n4. (/)")
  menu = int(input("Select the operator : "))
  a = int(input("Input value of A = "))
  b = int(input("Input value of B = "))

  if menu == 1:
      c = a + b
  elif menu == 2:
      c = a - b
  elif menu == 3:
      c = a * b
  elif menu == 4:
      c = a / b

  print("Total = ", c)
  ans = input("Want to this again? (Y/N) ").upper()

  if ans == "Y":
    run = True
  elif ans == "N":
    run = False

print()
print("--- Bye ---")
