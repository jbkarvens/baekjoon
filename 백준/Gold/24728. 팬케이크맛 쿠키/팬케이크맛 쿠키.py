from typing import Optional, List, Tuple

class PanCakeCookie:
    def __init__(self, w: int, h: int, maxC: int, u: int, d: int):
        self.__w = w
        self.__h = h
        self.__x = 0
        self.__y = 0
        self.__t = 0
        self.__score = 0
        self.__maxC = maxC
        self.__curC = maxC
        self.__u = u
        self.__d = d
        self.__path=[[0,0,0,maxC,0]]

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def getU(self) -> int:
        return self.__u

    def getD(self) -> int:
        return self.__d

    def getScore(self) -> int:
        return self.__score

    def getC(self) -> int:
        return self.__curC

    def reset(self) -> None:
        self.__x = self.__y = self.__t = 0
        self.__score = 0
        self.__curC = self.__maxC
        self.__path=[[0,0,0,self.__maxC,0]]

    def setU(self, x: int) -> None:
        if 1<=x<=1000:
            self.__u = x
            self.reset()

    def setD(self, x: int) -> None:
        if 1<=x<=1000:
            self.__d = x
            self.reset()

    def setC(self, x: int) -> None:
        if 1<=x<=1000:
            self.__maxC = x
            self.reset()

    def setT(self, t: int) -> None:
        if t<0 or t>=self.__w:
            return
        t_cur = self.__t
        if t<t_cur:
            self.__path=self.__path[:t+1]
            x,y,t_cur,curC,score = map(int,self.__path[-1])
        else:
            maxC=self.__maxC
            curC=self.getC()
            x = self.getX()
            y = self.getY()
            u = self.getU()
            d = self.getD()
            w = self.__w
            h = self.__h
            score = self.getScore()
            while t_cur<t:
                down = max(y-d,0)
                up = min(y+u,h)
                if up>=down and curC>0:
                    score +=up
                    x+=1
                    y = up
                    t_cur+=1
                    curC-=1
                else:
                    score+=down
                    x+=1
                    y=down
                    t_cur+=1
                    curC=min(curC+1,maxC)
                self.__path.append([x,y,t_cur,curC,score])
        self.__x=x
        self.__y=y
        self.__t=t_cur
        self.__curC=curC
        self.__score=score