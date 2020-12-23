map=[[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1 ],
          [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self, dir):
        if dir =='up':
            self.y += 1
        elif dir =='down':
            self.y -= 1
        elif dir =='left':
            self.x -= 1
        elif dir =='right':
            self.x += 1
        pass
    def get_position(self):
        return (self.x, self.y)

class MazeGame:
    def __init__(self, map=None):
        self.map = map
        self.player = Player()
        self.path = []
        self.direction = []

    def play(self):
        for r in range(len(self.map)):    # self.map와 같은 크기의 리스트 생성하기
            self.direction.append([])
            for c in range(len(self.map)):
                self.direction[-1].append([])

        for r in range(len(self.map)):      #각 index에서 갈 수 있는 index적기
            for c in range(len(self.map)):
                try:
                    if self.map[r+1][c] == 0:
                        self.direction[r][c].append((r+1,c))
                except:
                    pass
                try:
                    if self.map[r-1][c] == 0:
                        self.direction[r][c].append((r-1,c))
                except:
                    pass
                try:
                    if self.map[r][c+1] == 0:
                        self.direction[r][c].append((r,c+1))
                except:
                    pass
                try:
                    if self.map[r][c-1] == 0:
                        self.direction[r][c].append((r,c-1))
                except:
                    pass
        self.direction[len(self.map)-1][len(self.map)-1].append((-1,-1))
        self.escRoot(0, 0, None)
        self.path.reverse()

    def escRoot(self, pr, pc, prv):
        for tmp in self.direction[pr][pc]:
            if (-1, -1) == tmp:
                self.path.append((pr, pc))
                return 1

        self.path.append((pr, pc))
        for pos in self.direction[pr][pc]:
            if prv == pos:
                self.path.remove(pos)
                continue
            if pos in self.path:
                self.path.remove(pos)
                continue
            if self.escRoot(pos[0], pos[1], (pr, pc)) == 1:
                return 1

    def get_map(self):
        return self.map

    def get_path(self):
        return self.path


game1 = MazeGame(map)
game1.play()
print(game1.get_map())
print(game1.get_path())