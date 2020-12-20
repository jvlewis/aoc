from collections import defaultdict

def initializeCube(state, N):
      cube = defaultdict(int)
      N = N - 2
      z = [0] * N

      for y, row in enumerate(state):
        for x, col in enumerate(row):
            if col == '#':
              cube[(x, y, *z)] = col 
      return cube 

def cycleCube3D(cube):
  stateRange = [-1, 0, 1]
  nextState = defaultdict(int)
  nextCube = defaultdict(int)

  for pt in cube:
    x = pt[0]
    y = pt[1]
    z = pt[2]

    for nx in stateRange:
      for ny in stateRange:
        for nz in stateRange:
          if nx == ny == nz == 0:
            continue
          nextState[(x+nx,y+ny,z+nz)] += 1 
  for pt in nextState:
    if pt in cube and nextState[pt] in (2, 3):
      nextCube[pt] = '#'
    elif pt not in cube and nextState[pt] == 3:
      nextCube[pt] = '#'
  return nextCube

def cycleCube4D(cube):
  stateRange = [-1, 0, 1]
  nextState = defaultdict(int)
  nextCube = defaultdict(int)

  for pt in cube:
    x = pt[0]
    y = pt[1]
    z = pt[2]
    w = pt[3]

    for nx in stateRange:
      for ny in stateRange:
        for nz in stateRange:
          for nw in stateRange:
            if nx == ny == nz == nw == 0:
              continue
            nextState[(x+nx,y+ny,z+nz,w+nw)] += 1 
  for pt in nextState:
    if pt in cube and nextState[pt] in (2, 3):
      nextCube[pt] = '#'
    elif pt not in cube and nextState[pt] == 3:
      nextCube[pt] = '#'
  return nextCube

if __name__ == "__main__":
  initialState = open("input.txt", "r").read().splitlines()
  acive = 0
  cycles = 6
  active = '#'
  cube3 = initializeCube(initialState, 3)
  cube4 = initializeCube(initialState, 4)

  for _ in range(cycles):
    cube3 = cycleCube3D(cube3)
    cube4 = cycleCube4D(cube4)

  print('The cube has %d active cubes after %d cycles.' 
    % (sum(1 for x in cube3.values() if x == active), cycles))
  print('The cube has %d active cubes after %d cycles.' 
    % (sum(1 for x in cube4.values() if x == active), cycles))