print("Starting...")

from Image_Translator import imageToCode

i = 0
r = "r"

while r == "r":
  a = input("Would you like to save the code to a file, or print it in the command line? ('f' for file, 'c' for command line): ")

  while a != "f" and a != "c":
    i += 1
    a = input("Your input was invalid. Would you like to save the code to a file, or print it in the command line? (f for file, c for command line): ")

  if i >= 5:
    print("You finally entered a valid input.")

  if a == "f":
    imageToCode(input("Type the file path of the image you want to encode here. Make sure to include the file extension!: "), input("Type the directory you would like to save the code to. Do NOT add the file extension!: ")).saveToFile()
    r = input("Enter 'r' to encode another image, or anything else to close. ")
  else:
    imageToCode(input("Type the file path of the image you want to encode here. Make sure to include the file extension!: ")).printCode()
    r = input("Enter 'r' to encode another image, or anything else to close. ")