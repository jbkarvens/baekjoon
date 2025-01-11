# [Unrated] Word Crosses - 9957 

[문제 링크](https://www.acmicpc.net/problem/9957) 

### 성능 요약

메모리: 109540 KB, 시간: 96 ms

### 분류

분류 없음

### 제출 일자

2025년 1월 11일 21:19:59

### 문제 설명

<p>A word cross is formed by printing a pair of words, the first horizontally and the second vertically, so that they share a common letter. A leading word cross is one where the common letter is as near as possible to the beginning of both words, i.e. the sum of the positions of the common letter is minimised. If there are several minimal sums, choose the one that minimises the position of the matching letter in the first word of the pair. Thus MATCHES and CHEESECAKE could cross on 'A' (2+8 = 10), 'C' (4 + 1 = 5), 'H' (5+2 = 7), 'E' (6 + 3 = 9) and 'S' (7 + 5 = 12). The minimum is 5, so we use the 'C'. Double leading word crosses use two pairs of words arranged so that the two horizontal words are on the same line and each pair forms a leading word cross.</p>

<p>Write a program that will read in sets of four words (two pairs) and form them (if possible) into double leading word crosses, i.e. crossing the words in each pair separately, as in the example input below.</p>

### 입력 

 <p>Input will consist of a series of lines, each line containing four words (two pairs) and terminated by a line consisting of a single #. In this problem, a word consists of 1 to 10 upper case letters.</p>

### 출력 

 <p>Output will consist of a series of double leading word crosses as defined above. Leave exactly three spaces between the horizontal words. If it is not possible to form both crosses, write the message ‘Unable to make two crosses’. Do not print any trailing blanks. Leave one blank line between output sets.</p>

