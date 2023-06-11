# [Diamond IV] Phibonacci - 10908 

[문제 링크](https://www.acmicpc.net/problem/10908) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학, 정수론

### 문제 설명

<p><strong>피보나치(Fibonacci)</strong> 수는 아래의 점화식으로 정의되는 수열이다.</p>

<p>\[F_n = \begin{cases} 0 & \textrm{if}\;n =0; \\ 1 & \textrm{if}\;n =1; \\ F_{n-1} + F_{n-2} & \textrm{if}\; n > 1.\end{cases}\]</p>

<p>피보나치 수와 \(x^2 = x + 1\)의 두 근 중 하나인 황금비 \(\varphi = \frac{\sqrt{5}+1}{2}\)는 매우 연관이 깊은 수이다. 이에 관한 예를 들자면 피보나치 수의 일반항을 \(F_n = \frac{\varphi^n - \left(1-\varphi \right)^n}{\sqrt{5}}\)로 나타낼 수 있다는 점 등이 있다. 이제 \(\varphi\)를 이용해 <strong>파이보나치(Phibonacci)</strong> 수를 아래의 점화식으로 정의하고자 한다.</p>

<p>\[P_n = \begin{cases} 1 & \textrm{if}\;n =0; \\ \varphi & \textrm{if}\;n =1; \\ P_{n-1} + P_{n-2} & \textrm{if}\; n > 1.\end{cases}\]</p>

<p>편의를 위해 \(F_{-1} = 1\)이라고 하면, 놀랍게도 \(P_n = F_n\varphi + F_{n-1} \left(n \ge 0 \right)\)로 나타낼 수 있다! 이제 우리가 관심 있는 것은 \(\left(P_n\right)^k\)를 두 정수 \(A\), \(B\)를 이용해 \(A \varphi^k + B\) 꼴로 표현할 수 있느냐는 것이다. 표현 가능하다면, \(A\)와 \(B\)를 출력하고, 불가능하다면 -1을 출력하라.</p>

### 입력 

 <p>첫 번째 줄에 두 정수 \(n\) (0 ≤ \(n\) ≤ 10<sup>12</sup>), \(k\)가 공백으로 구분되어 주어진다.</p>

<p>1 ≤ \(k\) ≤ 10<sup>12</sup>인 입력이 주어진다</p>

### 출력 

 <p>첫 번째 줄에 \(\left(P_n\right)^k = A \varphi^k + B\)가 되는 두 정수 \(A\), \(B\)를 1,000,000,007로 나눈 나머지를 공백으로 구분하여 출력한다. 만약 이런 두 정수가 존재하지 않는 경우 -1을 출력한다</p>

