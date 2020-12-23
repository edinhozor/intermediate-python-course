def main():

  import random
  dice_rolls = 2
  dice_sum = 0

  print(f'Enter your name:')
  name1 = input()

  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    roll1 = random.randint(1,6)
    dice_sum = roll + roll1

  if roll == 1:
    print(f'First Roll {roll}! Critical Fail.')
  elif roll == 6:
    print(f'First Roll {roll}! Critical Success.')
  else:
    print(f'First Roll {roll}.')
  if roll1 == 1:
    print(f'Second Roll {roll1}! Critical Fail.')
  elif roll1 == 6:
    print(f'Second Roll {roll1}! Critical Success!')
  else:
    print(f'Second Roll {roll1}.')
  print(f'{name1} have rolled a total of {dice_sum}.')


if __name__== "__main__":
  main()