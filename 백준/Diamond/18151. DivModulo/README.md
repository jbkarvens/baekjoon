# [Diamond IV] DivModulo - 18151 

[문제 링크](https://www.acmicpc.net/problem/18151) 

### 성능 요약

메모리: 117184 KB, 시간: 6928 ms

### 분류

중국인의 나머지 정리, 분할 정복을 이용한 거듭제곱, 수학, 모듈로 곱셈 역원, 정수론

### 문제 설명

<p>Modulo (mod) is a very common operator on integers. For two integers n and d with d > 0, r ≡ (n mod d) is defined where 0 ≤ r < d and there exists an integer q, such that n = q × d+r. For example, (200 mod 5) ≡ 0 means that the remainder of 200 divided by 5 is 0. Here is another new operator called DivModulo (dmod) defined as follows. For two integers n and d with d > 0, r ≡ (n dmod d) is defined where there exists two integers m and h, such that r ≡ (m mod d), n = m × d<sup>h</sup>, and d is not a factor of m. For example, (200 dmod 5) ≡ 3, since (200 dmod 5) ≡ (8 × 5<sup>2</sup> dmod 5) ≡ (8 mod 5) ≡ 3.</p>

<p>Consider the factorials and the combination function. For an integer M ≥ 0, the factorial M! is defined as M! = M × (M −1) × (M −2) × · · · × 3 × 2 × 1, and 0! = 1 is defined. For integers M and N with 0 ≤ N ≤ M, the combination function C(M, N) is defined as C(M, N) = M!/(N!×(M−N)!). Now given three integers M, N, D with D > 0, please compute C(M, N) dmod D. For example, (C(9, 2) dmod 3) ≡ (36 dmod 3) ≡ (4 × 3<sup>2</sup> dmod 3) ≡ (4 mod 3) ≡ 1.</p>

### 입력 

 <p>Three integers M, N and D are given in one line.</p>

### 출력 

 <p>Please output C(M, N) dmod D in one line.</p>

