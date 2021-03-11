#!/bin/python3

'''
<div id="main-splitpane-left" class="coding-question__left-pane"><section class="question-view__title-wrapper"><h1 class="question-view__title">1. Python: Reverse Words and Swap Cases</h1></section><section class="question-view__instruction"><div class="candidate-rich-text"><div id="99f8cik52st-instruction"><div class="ps-content-wrapper-v0">
<p>Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those words but in the reverse order and such that all cases of letters in the original string are swapped, i.e. lowercase letters become uppercase and uppercase letters become lowercase.</p>

<p>&nbsp;</p>

<p><strong>Example</strong></p>

<p><em>sentence = </em>"rUns dOg"</p>

<p>&nbsp;</p>

<p>Reverse the word order and swap the case of all letters, then return the string "DoG RuNS".</p>

<p>&nbsp;</p>

<p class="section-title">Function description</p>

<p>Complete the function <em>reverse_words_order_and_swap_cases</em> in the editor below.</p>

<p>&nbsp;</p>

<p>The function has the following parameter(s):</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<em>string</em> <em>sentence:</em>&nbsp;a given string of space-separated words</p>

<p>Returns:</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<em>string : </em>a string containing all the words from the sentence but in the reverse order and such that all cases of letters in the sentence string are swapped.</p>

<p class="section-title">&nbsp;</p>

<p class="section-title">Constraints</p>

<ul>
	<li>
<em>sentence</em> contains only English letters and spaces.</li>
	<li>
<em>sentence</em> begins and ends with a letter.</li>
	<li>There are no two consecutive spaces in <em>sentence.</em>
</li>
	<li>There are at most 10 words in <em>sentence.</em>
</li>
	<li>The lengths of each of the words is at most 10.<br>
	&nbsp;</li>
</ul>
<!--       <StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Input Format Format for Custom Testing</summary>

<div class="collapsable-details">
<p>Input from stdin will be processed as follows and passed to the function<em>.</em></p>

<p>&nbsp;</p>

<p>The first and only line contains the string, <em>sentence,</em> that will be passed to the function.</p>
</div>
</details>
<!--        </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details open="open"><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input</p>

<pre>STDIN                 Function 
-----                 -------- 
aWESOME is cODING&nbsp;&nbsp;→&nbsp;&nbsp;sentence = "aWESOME is cODING"

</pre>

<p>&nbsp;</p>

<p class="section-title">Sample Output</p>

<pre>Coding IS Awesome
</pre>

<p>&nbsp;</p>

<p class="section-title">Explanation</p>

<p>sentence = "aWESOME is cODING"</p>

<p>Reverse the word order: "cODING IS aWESOME"</p>

<p>Swap the case: "Coding IS Awesome"</p>

<p>The order of the words is reversed and the case of all letters are swapped.</p>
</div>
</details>

<details><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input</p>

<pre>STDIN    Function
-----    --------
fUn&nbsp;&nbsp; →&nbsp;&nbsp;sentence = "fUn"

</pre>

<p>&nbsp;</p>

<p class="section-title">Sample Output</p>

<pre>FuN</pre>

<p>&nbsp;</p>

<p class="section-title">Explanation</p>
&nbsp;

<p>sentence = "fUn"</p>

<p>Reverse the word order: The sentence contains only one word "fUn"</p>

<p>Swap the case of all letters: "FuN"</p>
</div>
</details>
</div>
<style type="text/css"><p><em>1 ≤ |source| ≤ 10^6 </em></p>.ps-content-wrapper-v0 div { margin: 0 auto; overflow: auto; } .ps-content-wrapper-v0 div.preheader { display: none; } .ps-content-wrapper-v0 p { white-space: pre-wrap; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 p.section-title { font-weight: bold; padding-bottom: 0px; } .ps-content-wrapper-v0 ol.plain-list, .ps-content-wrapper-v0 ul.plain-list { list-style-type: none; padding: 4px; } .ps-content-wrapper-v0 li { white-space: normal; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 code { color: black; } .ps-content-wrapper-v0 pre { background-color: #f4faff; border: 0; border-radius: 2px; margin: 8px; padding: 10px; } .ps-content-wrapper-v0 figure { background-color: transparent; display: table; margin-top: 8px; margin-bottom: 8px; text-align: center; margin-left: auto; margin-right: auto; } .ps-content-wrapper-v0 figcaption { text-align: center; display: table-caption; caption-side: bottom; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 img { width: auto; max-width: 100%; height: auto; } .ps-content-wrapper-v0 details { background-color: transparent; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 details summary { background-color: #39424e; color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px; } .ps-content-wrapper-v0 details div.collapsable-details { margin: 0 auto; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; overflow: auto; } .ps-content-wrapper-v0 details div.collapsable-details pre { margin-left: 4px; margin-right: 4px; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 table { border: 1px solid black; border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; width: 96%; table-layout: fixed; } .ps-content-wrapper-v0 table tbody tr th, .ps-content-wrapper-v0 table tbody tr td { font-weight: bold; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; } .ps-content-wrapper-v0 table tbody tr th.description { width: 60%; } .ps-content-wrapper-v0 table tbody tr td { font-weight: normal; white-space: normal; } .ps-content-wrapper-v0 table.function-params tbody tr:first-child td.headers { border-bottom-width: 2px; } .ps-content-wrapper-v0 table.function-params tbody tr:last-child td { border-top-width: 2px; border-top-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.headers { width: 25%; font-weight: bold; text-align: center; border: 1px solid black; border-right-width: 2px; border-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell { width: 100%; height: 100%; padding: 0px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table { width: 100%; height: 100%; padding: 0px; margin: 0px; border: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td.code { white-space: normal; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th { border-top: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:last-child { border-right: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr:last-child td { border-bottom: 0; border-top-width: 1px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:last-child { border-right: 0; } .ps-content-wrapper-v0 .left { text-align: left; } .ps-content-wrapper-v0 .right { text-align: right; } .ps-content-wrapper-v0 .code { font-family: monospace; white-space: nowrap; } .ps-content-wrapper-v0 .json-object-array ol, .ps-content-wrapper-v0 .json-object-array ol ul { margin-top: 0px; padding-left: 14px; } .json-object-array li { float: left; margin-right: 30px; margin-left: 10px; } .json-object-array pre { padding: 4px; margin-left: 0px; }
</style>
</div></div></section></div>

'''

#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    ss = sentence.swapcase().split(" ")
    ss.reverse()
    return " ".join(ss)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # sentence = input()

    # result = reverse_words_order_and_swap_cases(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
    print(reverse_words_order_and_swap_cases("aWESOME is cODING"))