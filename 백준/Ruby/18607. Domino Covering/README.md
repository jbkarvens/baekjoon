# [Ruby II] Domino Covering - 18607 

[문제 링크](https://www.acmicpc.net/problem/18607) 

### 성능 요약

메모리: 166216 KB, 시간: 15636 ms

### 분류

조합론, 분할 정복을 이용한 거듭제곱, 수학

### 문제 설명

<p>Elizur has an empty n × m grid, and he wants to use some 1 × 2 and 2 × 1 dominoes to cover the entire grid. In the grid, each domino ought to cover exactly two adjacent squares and each square ought to be covered by exactly one domino. Two squares are adjacent if and only if they share a common side.</p>

<p>Obviously, he can achieve that if and only if at least one of n and m is even: otherwise, there is always a square that must be left empty. Hence, he wants to know in how many ways he can cover the entire grid. Two ways are considered different if and only if there exist two dominoes, one from the first covering and one from the other, such that one of the squares cover is the same but the other is different.</p>

<p>Can you help him determine the answer? The answer may be exceedingly large, so he only asks you to find it modulo a <strong>prime number</strong> p</p>

### 입력 

 <p>The first line contains a single integer T (1 ≤ T ≤ 20 000), indicating the number of questions.</p>

<p>Each of the next T lines contains three integers, n (1 ≤ n ≤ 35), m (1 ≤ m ≤ 10<sup>18</sup>), and p (2 ≤ p ≤ 2<sup>30</sup>, p is prime), describing one question.</p>

<p>It is guaranteed that no more than 1000 cases satisfy n > 5 or m > 10<sup>9</sup>.</p>

### 출력 

 <p>For each question, output a single line with a single integer: the answer modulo p.</p>

