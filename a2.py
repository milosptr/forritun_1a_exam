# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1A - Spurning 2

numbers: list = []

while True:
  number:int = int(input("Sláðu inn tölu: "))
  if number == 0:
    break
  numbers.append(number)

if len(numbers) == 0:
  print(f'Fjöldi negatívra talna: 0')
  print("Engin tala slegin inn, ekkert meðaltal og engin lægsta talan")
  exit()

negative_numbers: list = list(filter(lambda number: number < 0, numbers))
print(f'Fjöldi negatívra talna: {len(negative_numbers)}')

average: float = sum(numbers) / len(numbers)
print(f'Meðaltal talna {round(average, 2)}')

smallest_number: int = min(numbers)
print(f'Lægsta tala {smallest_number}')
