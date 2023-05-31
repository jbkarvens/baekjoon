# [Platinum V] Knights - 3326 

[문제 링크](https://www.acmicpc.net/problem/3326) 

### 성능 요약

메모리: 166044 KB, 시간: 488 ms

### 분류

다이나믹 프로그래밍, 게임 이론

### 문제 설명

<p>Alice and Bob are playing a game. Initially K black Knights are placed on a N × N chessboard. Now the players take turns. On each turn, a player moves every knight that has at least one valid move left. The following four moves are valid, as long as they do not move the knight off the board:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/041a2700-d7a8-4220-b6cf-678c9d9ae1aa/-/preview/" style="width: 290px; height: 305px;"></p>

<p>A knight with no valid moves left remains at its current position. The first player who is not able to move any of the knights loses the game. Note that during the game several knights are allowed to occupy the same square.</p>

<p>You are given the locations of the knights on the chessboard. Alice begins the game. Determine whether she can win the game, assuming that both players play optimally. If she can win, output a possible first move for each knight. In the beginning, there is at least one valid move for each knight, and no two knights are placed on the same square of the chessboard.</p>

### 입력 

 <p>The first line contains the two integers K (1 ≤ K ≤ 200 000) and N (1 ≤ N ≤ 1 000 000) separated by a single space. This line is followed by K lines describing the positions of the knights.</p>

<p>Line i + 1 contains two integers x<sub>i</sub> and y<sub>i</sub> (1 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ N) separated by a single space, the coordinates of knight i.</p>

### 출력 

 <p>Output a single line containing the word <code>NO</code> if Alice cannot win the game. Otherwise, output K + 1 lines with <code>YES</code> on the first line and coordinates x'<sub>i</sub> , y'<sub>i</sub> on line i + 1, giving a destination that Alice may choose for knight i in the first turn in order to win the game.</p>

