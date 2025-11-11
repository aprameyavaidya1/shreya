try:
  age=int(input("Enter your age:"))
  if age >=18:
    print("your are eligible")
  else:
    print("your are not eligible")
except ValueError:
  print("please enter a valid integer for age.")
