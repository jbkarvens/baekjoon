# [Gold V] Kaladėlės - 30070 

[문제 링크](https://www.acmicpc.net/problem/30070) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

해 구성하기, 자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2024년 12월 27일 12:42:26

### 문제 설명

<p>Linas gimtadienio proga gavo <em>Lego</em> konstruktorių, sudarytą iš <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> įvairiaspalvių kaladėlių. Visas kaladėles Linas sudėliojo į eilę ir užrašė kiekvienos spalvą kaip didžiąją lotynišką raidę:</p>

<p><code>B D A A R A R B K A A</code></p>

<p>Bežaisdamas su kaladėlėmis, Linas jas perdėliojo taip, kad jokios tos pačios spalvos kaladėlės nebūtų viena šalia kitos:</p>

<p><code>A B R A K A D A B R A</code></p>

<p>Linui kilo klausimas: ar kito konstruktoriaus kaladėles taip pat pavyktų perdėlioti taip, kad tos pačios spalvos kaladėlės nebūtų greta?</p>

<p>Parašykite progamą, kuri nustatytų, ar įmanoma perdėlioti kaladėles norimu būdu, ir jei įmanoma, išvestų perdėliotų kaladėlių spalvų seką.</p>

### 입력 

 <p>Pirmoje eilutėje įrašytas kaladėlių kiekis <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>.</p>

<p>Antroje eilutėje įrašyta <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> tarpais atskirtų didžiųjų lotyniškų raidžių.</p>

### 출력 

 <p>Jeigu įmanoma seką perdėlioti taip, kad greta nebūtų vienspalvių kaladėlių, išveskite <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> tarpais atskirtų raidžių, atitinkančių kaladėlių spalvas. Jeigu yra daugiau nei vienas teisingas atsakymas, išveskite bet kurį.</p>

<p>Jeigu neįmanoma – išveskite žodį <code>NE</code>.</p>

