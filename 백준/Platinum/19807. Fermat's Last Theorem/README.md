# [Platinum V] Fermat's Last Theorem - 19807 

[문제 링크](https://www.acmicpc.net/problem/19807) 

### 성능 요약

메모리: 31256 KB, 시간: 68 ms

### 분류

수학

### 문제 설명

<p>As you probably know, for all positive integers $a$, $b$, $c$ and $n$ with $n \ge 3$ the following inequality holds: $a^n + b^n \neq c^n$. But all existing proofs of this fact are hard to verify, so a group of software engineers has decided to write their own proof that will be, in their opinion, easier to verify.</p>

<p>This group has written a program that iterates over all quadruples of positive integers $(a, b, c, n)$ such that $n \ge 3$, in increasing order of the maximums of its elements, and in case of equality of maximums --- in the lexicographical order.</p>

<p>Thus first the quadruple $(1, 1, 1, 3)$ will be considered, then the quadruple $(1, 1, 2, 3)$, and so on. And, for example, the quadruple $(3, 3, 3, 3)$ will be followed by the quadruple $(1, 1, 1, 4)$.</p>

<p>For each quadruple the program compares the values $a^n + b^n$ and $c^n$, and prints the corresponding inequality: $a^n + b^n > c^n$ or $a^n + b^n < c^n$.</p>

<p>Now the software engineers want to verify their proof. They ask you to repeat their calculations and output the inequalities printed by their program, from the $l$-th to the $r$-th one, inclusive.</p>

### 입력 

 <p>The first line contains two integers $l$ and $r$ ($1 \le l \le r \le {10}^{12}$; $r - l \le {10}^4$).</p>

### 출력 

 <p>Output the part of the printed proof, from the $l$-th inequality to the $r$-th one, each on a separate line. To denote exponentiation, use a caret ('<code>^</code>', the ASCII character with code 94). Don't output any spaces.</p>

