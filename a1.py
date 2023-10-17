# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1A - Spurning 1


while True:
  first_number:float = float(input("Fyrsta tala: "))
  second_number:float = float(input("Önnur talan: "))
  third_number:float = float(input("Þirða talan: "))

  # summ of all numbers, when divided by 3,
  # if equal to first number, then all numbers are equal
  sum_of_numbers:float = first_number + second_number + third_number

  if sum_of_numbers / 3 == first_number:
    print(f'Allar tölurnar eru eins {round(float(first_number), 1)}')
  elif first_number == second_number:
    print(f'Fyrsta og önnur talan eru eins {round(float(first_number), 1)}')
  elif first_number == third_number:
    print(f'Fyrsta og þriðja talan eru eins {round(float(first_number), 1)}')
  elif second_number == third_number:
    print(f'Önnur og þriðja talan eru eins {round(float(second_number), 1)}')
  else:
    print(f'Engar tvær tölur eru eins')

  should_continue:str = input("Viltu endurtaka: (J eða j ef já) ").lower()
  if should_continue != "j":
    break
