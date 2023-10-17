# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1A - Spurning 3

# generate a mask
mask:str = 'X-XXX-XXXXX-X'

# get input from user
isbn:str = input("ISBN númer: ")


# checking if they have equal length
if len(isbn) != len(mask):
  print("Rangt ISBN númer")
  exit()


for i in range(len(mask)):
  # if current index in a mask expect X here
  if mask[i] == 'X':
    # and the current index in the input is not digit
    # return that its an incorrect ISBN number
    if not isbn[i].isdigit():
      print("Rangt ISBN númer")
      exit()
  # if there is no - on expected index
  # return that its an incorrect ISBN number
  elif mask[i] != isbn[i]:
    print("Rangt ISBN númer")
    exit()

# in any other case, the input is correct ISBN number
print("ISBN númer er rétt")
