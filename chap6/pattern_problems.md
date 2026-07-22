Pattern 1



\*

\*\*

\*\*\*

\*\*\*\*

\*\*\*\*\*



total number of lines : 5

Outer loop runs 5 times 



| outer loop(i)|inner loop(j)|print|
|-|-|-|
|1|1|\*|
|2|2|\*\*|
|3|3|\*\*\*|
|4|4|\*\*\*\*|
|5|5|\*\*\*\*\*|



**j = i**



Pattern 2



1

22

333

4444

55555



total number of lines : 5

outer loop runs 5 times



|outer loop (i)|inner loop (j)|print|
|-|-|-|
|1|1|1|
|2|2|2|
|3|3|3|
|4|4|4|





**print(i)**

**j = i**



pattern 3

&#x20;   

&#x20;   \*

&#x20;  \*\*\*

&#x20; \*\*\*\*\*

&#x20;\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*



total number of lines = n = 5



|outer loop i|inner loop for gaps|inner loop for stars|
|-|-|-|
|1|4|1|
|2|3|3|
|3|2|5|
|4|1|7|
|5|0|9|



gaps + i = n

=> gaps = n - i



stars = 2 \* i - 1





