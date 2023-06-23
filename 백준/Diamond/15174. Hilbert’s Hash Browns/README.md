# [Diamond III] Hilbert’s Hash Browns - 15174 

[문제 링크](https://www.acmicpc.net/problem/15174) 

### 성능 요약

메모리: 114788 KB, 시간: 132 ms

### 분류

중국인의 나머지 정리, 수학, 정수론

### 문제 설명

<p>You may have heard of Hilbert’s Hotel. It has infinitely many rooms, and can cater for infinitely many guests. Each room has a number so even if it seems full, room for an extra guest can be found by asking every guest to move from room i to room i + 1, thus freeing up room 0. Unfortunately, the restaurant attached to the hotel, Hilbert’s Hash Browns, is not infinite, although the number of tables is very large.</p>

<p>To make matters worse, the waiter is very lazy. Rather than keep a record of which tables are available, he just assigns people to a table using a simple formula: when someone arrives at the restaurant, the waiter asks them their hotel room number. He raises this number to the power of p, and adds q. Since this gives very big numbers and there are only n tables (numbered 0 to n − 1), the waiter takes the remainder when dividing by n, and directs the customer to that table. Of course, sometimes the table is already occupied, in which case the customer goes away hungry</p>

<p>The waiter uses a different value for p and q every day and he has noticed that some days a table never gets used no matter how many patrons turn up. For example if n = 3, p = 2 and q = 1, then table number 0 will never be used because there is no number x such that x<sup>2</sup> + 1 ≡ 0 mod 3.</p>

<p>The waiter is lazy but he would like to appear competent. Can you help him determine the maximum number of tables that can be assigned for given values of p, q and n?</p>

### 입력 

 <p>The input consists of a single line containing three integers p (1 ≤ p < 2<sup>31</sup>), q (0 ≤ q < 2<sup>31</sup>) and n (2 ≤ n < 2<sup>31</sup>).</p>

### 출력 

 <p>Display the maximum number of tables that could be used.</p>

