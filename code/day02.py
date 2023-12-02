import re

def stage1(run):
  colors = ['red', 'green', 'blue']
  maxAmount = {
    'red': 12,
    'green': 13,
    'blue': 14
  }

  sum = 0

  with open('../'+run+'/day2.txt') as f:
    lines = f.readlines()

  for line in lines:
    validGame = True
    game, content = line.split(':')
    gameID = int((re.findall(r'\d+', game))[0])
    foundColors = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    tries = content.split(';')
    for test in tries:
      test = test.strip()
      colorsFndInBag = test.split(',')
      for colorFnd in colorsFndInBag:
        colorCnt, colorInTry = (colorFnd.strip()).split(' ')
        if colorInTry in colors:
          if foundColors[colorInTry] < int(colorCnt):
            foundColors[colorInTry] = int(colorCnt)

    for colorFnd in foundColors:
      if foundColors[colorFnd] > maxAmount[colorFnd]:
        validGame = False
      
    # print(f"Found colors: red {foundColors['red']}, green {foundColors['green']}, blue {foundColors['blue']} - valid game: {validGame} - game ident: {gameID}")
    
    if validGame:
      sum = sum + gameID
  
  print(f'Stage 1 > total sum of {sum}')


def stage2(run):
  colors = ['red', 'green', 'blue']
  sum = 0

  with open('../'+run+'/day2.txt') as f:
    lines = f.readlines()

  for line in lines:
    validGame = True
    game, content = line.split(':')
    gameID = int((re.findall(r'\d+', game))[0])
    foundColors = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    tries = content.split(';')
    for test in tries:
      test = test.strip()
      colorsFndInBag = test.split(',')
      for colorFnd in colorsFndInBag:
        colorCnt, colorInTry = (colorFnd.strip()).split(' ')
        if colorInTry in colors:
          if foundColors[colorInTry] < int(colorCnt):
            foundColors[colorInTry] = int(colorCnt)
          

    power = foundColors['red'] * foundColors['green'] * foundColors['blue']    
    sum = sum + power
    # print(f'{gameID} - {power} - {sum}')  
    # print(f"Found colors: red {foundColors['red']}, green {foundColors['green']}, blue {foundColors['blue']} - valid game: {validGame} - game ident: {gameID}")
  
  print(f'Stage 2 > Total sum of powers of {sum}')

def main():
  stage1('input')
  stage2('input')

if __name__ == '__main__':
  main()