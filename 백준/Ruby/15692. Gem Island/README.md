# [Ruby V] Gem Island - 15692 

[문제 링크](https://www.acmicpc.net/problem/15692) 

### 성능 요약

메모리: 135616 KB, 시간: 3932 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 문제 설명

<p>Gem Island is a tiny island in the middle of the Pacific Ocean. Until recently, it was known as one of the poorest, but also most peaceful, places on Earth. Today, it is neither poor nor peaceful. What happened?</p>

<p>One sunny morning, not too long ago, all inhabitants of Gem Island woke up to a surprise. That morning, each of them suddenly held one sparkling gem in their hand. The gems had magically appeared overnight. This was cause for much rejoicing – everybody was suddenly rich, they could finally afford all the things they had ever dreamed of, and the name of their island made so much more sense now.</p>

<p>The next morning, one of the inhabitants woke up to another surprise – her gem had magically split into two gems! The same thing happened on each of the following nights, when exactly one of the gems (apparently uniformly at random among all the gems on the island) would split into two.</p>

<p>After a while, the inhabitants of Gem Island possessed a widely varying number of gems. Some had a lot and many had only a few. How come some inhabitants had more gems than others? Did they cheat, were they just lucky, or was something else at work?</p>

<p>The island elders have asked for your help. They want you to determine if the uneven distribution of gems is explained by pure chance. If so, that would greatly reduce tensions on the island.</p>

<p>The island has n inhabitants. You are to determine the gem distribution after d nights of gem splitting. In particular, you are interested in the expected number of gems collectively held by the r people with the largest numbers of gems. More formally, suppose that after d nights the numbers of gems held by the n inhabitants are listed in non-increasing order as a<sub>1</sub> ≥ a<sub>2</sub> ≥ . . . ≥ a<sub>n</sub>. What is the expected value of a<sub>1</sub> + · · · + a<sub>r</sub>?</p>

### 입력 

 <p>The input consists of a single line containing the three integers n, d, and r (1 ≤ n, d ≤ 500, 1 ≤ r ≤ n), as described in the problem statement above.</p>

### 출력 

 <p>Display the expected number of gems that the top r inhabitants hold after d nights, with an absolute or relative error of at most 10<sup>−6</sup>.</p>

