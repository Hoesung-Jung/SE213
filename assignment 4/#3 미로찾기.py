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
        self.sol = []
        self.maposition = []

    def play(self):
        mapsize = int((len(map) - 1) / 2)  # map 생김새를 고려해야 함
        for r in range(1, mapsize + 1):
            self.maposition.append([])
            for c in range(1, mapsize + 1):
                self.maposition[-1].append([])

        for r in range(1, mapsize * 2, 2):  # r,c는 현재 좌표고 rr, cc과 방좌표
            for c in range(1, mapsize * 2, 2):
                rr, cc = int((r + 1) / 2) - 1, int((c + 1) / 2) - 1
                if self.map[r - 1][c] == 0:
                    if rr-1 >= 0:
                        self.maposition[rr][cc].append((rr - 1, cc))
                if self.map[r + 1][c] == 0:
                    self.maposition[rr][cc].append((rr + 1, cc))
                if self.map[r][c - 1] == 0:
                    if cc - 1 >= 0:
                        self.maposition[rr][cc].append((rr, cc - 1))
                if self.map[r][c + 1] == 0:
                    self.maposition[rr][cc].append((rr - 1, cc + 1))
        self.maposition[mapsize - 1][mapsize - 1].append((-1, -1))
        self.escRoot(0, 0, None)
        self.sol.reverse()

        self.path.append(self.player.get_position())
        self.player.move('up')
        self.path.append(self.player.get_position())
        self.player.move('right')
        self.path.append(self.player.get_position())

        for lv in range(len(self.sol)):
            r, c = self.sol[lv]
            rr = self.sol[lv + 1][0] - r
            cc = self.sol[lv + 1][1] - c
            if rr == 1 and cc == 0:
                self.player.move('up')
                self.path.append(self.player.get_position())
            if rr == 0 and cc == 1:
                self.player.move('right')
                self.path.append(self.player.get_position())
            if rr == -1 and cc == 0:
                self.player.move('down')
                self.path.append(self.player.get_position())
            if rr == 0 and cc == -1:
                self.player.move('left')
                self.path.append(self.player.get_position())

    def get_map(self):
        return self.map

    def get_path(self):
        return self.path

    def escRoot(self, pr, pc, prv):
        for tmp in self.maposition[pr][pc]:
            if (-1, -1) == tmp:
                self.sol.append((pr, pc))
                return 1

        for pos in self.maposition[pr][pc]:
            if prv == pos:
                continue
            if self.escRoot(pos[0], pos[1], (pr, pc)) == 1:
                self.sol.append((pr, pc))
                return 1


game1 = MazeGame(map)
game1.play()
print(game1.get_map())
print(game1.get_path())








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
m1=[ [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
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
          [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]
m2= [[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
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
          [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
          [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ] ]
m3=[ [ 0, 1, 1, 1, 1, 1],
          [ 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 1, 1, 1, 0, 0 ],]

m4=[ [ 0, 1, 1, 1, 1, 1],
          [ 0, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 1, 1, 1 ],
          [ 1, 0, 0, 0, 0, 1 ],
          [ 1, 0, 1, 1, 0, 1 ],
          [ 1, 1, 1, 1, 0, 0 ],]

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
        self.sol = []
        self.maposition = []

    def play(self):
        mapsize = int((len(map) - 1) / 2)  # map 생김새를 고려해야 함
        for r in range(1, mapsize + 1):
            self.maposition.append([])
            for c in range(1, mapsize + 1):
                self.maposition[-1].append([])

        for r in range(1, mapsize * 2, 2):  # r,c는 현재 좌표고 rr, cc과 방좌표
            for c in range(1, mapsize * 2, 2):
                rr, cc = int((r + 1) / 2) - 1, int((c + 1) / 2) - 1
                if self.map[r - 1][c] == 0:
                    if rr >= 0 and rr < 6 and cc - 1 >= 0 and cc < 6:
                        self.maposition[rr][cc].append((rr - 1, cc))
                if self.map[r + 1][c] == 0:
                    if rr >= 0 and rr < 6 and cc - 1 >= 0 and cc < 6:
                        self.maposition[rr][cc].append((rr + 1, cc))
                if self.map[r][c - 1] == 0:
                    if rr >= 0 and rr < 6 and cc - 1 >= 0 and cc < 6:
                        self.maposition[rr][cc].append((rr, cc - 1))
                if self.map[r][c + 1] == 0:
                    if rr >= 0 and rr < 6 and cc - 1 >= 0 and cc < 6:
                        self.maposition[rr][cc].append((rr - 1, cc + 1))
        self.maposition[mapsize - 1][mapsize - 1].append((-1, -1))
        self.escRoot(0, 0, None)
        self.sol.reverse()

        self.path.append(self.player.get_position())
        self.player.move('up')
        self.path.append(self.player.get_position())
        self.player.move('right')
        self.path.append(self.player.get_position())
        self.path.append((len(map)-1,len(map)-1))

        for lv in range(len(self.sol)):
            r, c = self.sol[lv]
            rr = self.sol[lv + 1][0] - r
            cc = self.sol[lv + 1][1] - c
            if rr == 1 and cc == 0:
                self.player.move('up')
                self.path.append(self.player.get_position())
            if rr == 0 and cc == 1:
                self.player.move('right')
                self.path.append(self.player.get_position())
            if rr == -1 and cc == 0:
                self.player.move('down')
                self.path.append(self.player.get_position())
            if rr == 0 and cc == -1:
                self.player.move('left')
                self.path.append(self.player.get_position())



    def get_map(self):
        return self.map

    def get_path(self):
        return self.path

    def escRoot(self,pr,pc,prv):
        for tmp in self.maposition[pr][pc]:
            if (-1,-1) == tmp:
                self.sol.append((pr,pc))
                return 1

        for pos in self.maposition[pr][pc]:
            if prv == pos:
                continue
            if self.escRoot(pos[0],pos[1],(pr,pc)) == 1:
                self.sol.append((pr,pc))
                return 1

if __name__ == "__main__" :
    game1 = MazeGame(map)
    game1.play()
    print(game1.get_map())
    print(game1.get_path())