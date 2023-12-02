import re

def stage1(run):
  sum = 0
  with open('../'+run+'/day1.txt') as f:
    lines = f.readlines()
  for line in lines:
    numbers = re.findall(r'\d', line)
    # print(f"The found numbers are {numbers[0]} and {numbers[-1]}")
    sum = sum + int(numbers[0]+numbers[-1])
  
  print(f"Stage 1\n--> The sum of the found numbers is: {sum}")

def stage2(run):
  sum = 0
  with open('../'+run+'/day1.txt') as f:
    lines = f.readlines()

  needle = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  for line in lines:
    first_occurrence_index = float('inf')
    last_occurrence_index = -1

    first_needle = '0'
    last_needle = '0'
    for substring in needle:
      index = line.find(substring)
      lastidx = line.rfind(substring)
      if index != -1 and index < first_occurrence_index:
        first_occurrence_index = index
        first_needle = line[index:(index + len(substring))]
      if lastidx != -1 and lastidx > last_occurrence_index:
        last_occurrence_index = lastidx
        last_needle = line[lastidx:(lastidx + len(substring))]
        # print(f'Last IDX: {index} - last needle: {last_needle} - SUBSTR: {substring}')
    # print(f"The found numbers are {first_needle} and {last_needle}")

    if needle.index(first_needle) < 10:
      first_needle = str(needle.index(first_needle))
    if needle.index(last_needle) < 10:
      last_needle = str(needle.index(last_needle))
    sum = sum + int(first_needle+last_needle)
  
  print(f"Stage 2\n--> The sum of the found numbers is: {sum}")

def main():
  stage1('input')
  stage2('input')


if __name__ == '__main__':
  main()