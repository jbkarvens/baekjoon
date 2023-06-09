# [Platinum I] 최대공약수 기댓값 - 14862 

[문제 링크](https://www.acmicpc.net/problem/14862) 

### 성능 요약

메모리: 117696 KB, 시간: 1308 ms

### 분류

수학, 뫼비우스 반전 공식, 모듈로 곱셈 역원, 정수론

### 문제 설명

<p>크기가 K인 두 수열 A와 B가 주어진다. 수열 X는 A와 B를 이용해서 만들 수 있으며, X<sub>i</sub>는 A<sub>i</sub>보다 크거나 같고, B<sub>i</sub>보다 작거나 같은 정수 중에서 랜덤하게 고른다. </p>

<p>수열 A와 B가 주어졌을 때, GCD(X<sub>0</sub>, X<sub>1</sub>, ..., X<sub>K-1</sub>)의 기댓값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 50)가 주어진다.</p>

<p>각 테스트 케이스의 첫째 줄에는 K (2 ≤ K ≤ 5)가 주어진다. 다음 K개의 줄에는 A<sub>i</sub>와 B<sub>i</sub>가 한 줄에 하나씩 주어진다. (1 ≤ A<sub>i</sub> ≤ B<sub>i</sub> ≤ 200000)</p>

### 출력 

 <p>문제의 정답이 P/Q인 경우에, 10<sup>9</sup>+7로 나누어 떨어지는 P+Q×N을 찾고, 그 때 N (0 ≤ N ≤ 10<sup>9</sup>+6)을 첫째 줄에 출력한다. 만약, N이 존재하지 않으면 -1을 출력한다.</p>

