#!/bin/python3

'''
<div id="main-splitpane-left" class="coding-question__left-pane"><section class="question-view__title-wrapper"><h1 class="question-view__title">1. Password Decryption</h1></section><section class="question-view__instruction"><div class="candidate-rich-text"><div id="bdfkfnld4gp-instruction"><style type="text/css">.ps-content-wrapper-v0 div { margin: 0 auto; overflow: auto; } .ps-content-wrapper-v0 div.preheader { display: none; } .ps-content-wrapper-v0 p { white-space: pre-wrap; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 p.section-title { font-weight: bold; padding-bottom: 0px; } .ps-content-wrapper-v0 ol.plain-list, .ps-content-wrapper-v0 ul.plain-list { list-style-type: none; padding: 4px; } .ps-content-wrapper-v0 li { white-space: normal; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 code { color: black; } .ps-content-wrapper-v0 pre { background-color: #f4faff; border: 0; border-radius: 2px; margin: 8px; padding: 10px; } .ps-content-wrapper-v0 pre.scrollable-full-json { overflow-x: scroll; white-space: pre; } .ps-content-wrapper-v0 pre.scrollable-json { height: 300px; overflow-y: scroll; display: inline-grid; white-space: pre-wrap; padding-left: 8px; padding-right: 8px; padding-top: 4px; padding-bottom: 4px; } .ps-content-wrapper-v0 div.equation-parent { width: 400px; text-align: center; border: 1px solid #000; padding: 8px; } .ps-content-wrapper-v0 div.equation-parent.equation { width: 100%; display: inline-block; } .ps-content-wrapper-v0 figure { background-color: transparent; display: table; margin-top: 8px; margin-bottom: 8px; text-align: center; margin-left: auto; margin-right: auto; } .ps-content-wrapper-v0 figcaption { text-align: center; display: table-caption; caption-side: bottom; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 img { width: auto; max-width: 100%; height: auto; } .ps-content-wrapper-v0 details { background-color: transparent; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; } .ps-content-wrapper-v0 details details { padding-left: 8px; padding-right: 8px; } .ps-content-wrapper-v0 details summary { background-color: #39424e; color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px; } .ps-content-wrapper-v0 details details summary code { color: black; font-weight: bold; padding-left: 2px; padding-right: 2px; padding-top: 4px; padding-right: 4px; margin-left: 4px; } .ps-content-wrapper-v0 details div.collapsable-details { margin: 0 auto; padding-left: 4px; padding-right: 4px; padding-top: 0px; padding-bottom: 2px; overflow: auto; } .ps-content-wrapper-v0 details div.collapsable-details pre { margin-left: 4px; margin-right: 4px; margin-top: 4px; margin-bottom: 4px; } .ps-content-wrapper-v0 table.normal { border: 1px solid black; border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; width: 96%; table-layout: fixed; } .ps-content-wrapper-v0 table.normal tbody { display: block; overflow-x: auto; overflow-y: hidden; } .ps-content-wrapper-v0 table.normal tbody tr:first-child th { font-weight: bold; white-space: normal; } .ps-content-wrapper-v0 table.normal tbody tr th, .ps-content-wrapper-v0 table.normal tbody tr td { font-weight: normal; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; } .ps-content-wrapper-v0 table.database-table { border-collapse: collapse; border-color: darkgray; border: 1px solid black; width: auto; margin-left: 4px; margin-top: 8px; margin-bottom: 8px; padding: 8px; } .ps-content-wrapper-v0 table.database-table tbody { overflow-x: auto; overflow-y: hidden; border: none; } .ps-content-wrapper-v0 table.database-table tbody tr th, .ps-content-wrapper-v0 table.database-table tbody tr td { font-weight: normal; white-space: nowrap; text-align: center; vertical-align: middle; border: 1px solid black; border-color: darkgray; padding: 8px; } .ps-content-wrapper-v0 table.database-table tbody tr th { font-weight: bold; border: 1px solid black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(2) td { border: 1px solid black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(n+2) td:first-child { border-left-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr:nth-child(n+2) td:last-child { border-right-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr:last-child td { border-bottom-color: black; } .ps-content-wrapper-v0 table.database-table tbody tr td.description { text-align: left; white-space: pre-wrap; } .ps-content-wrapper-v0 table.normal tbody tr th.description { width: 60%; } .ps-content-wrapper-v0 table.function-params tbody tr:first-child td.headers { border-bottom-width: 2px; } .ps-content-wrapper-v0 table.function-params tbody tr:last-child td { border-top-width: 2px; border-top-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.headers { width: 25%; font-weight: bold; text-align: center; border: 1px solid black; border-right-width: 2px; border-color: darkgray; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell { width: 100%; height: 100%; padding: 0px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table { width: 100%; height: 100%; padding: 0px; margin: 0px; border: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td.code { white-space: normal; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th { border-top: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr th:last-child { border-right: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr:last-child td { border-bottom: 0; border-top-width: 1px; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:first-child { border-left: 0; } .ps-content-wrapper-v0 table.function-params tbody tr td.params-table-cell table.params-table tbody tr td:last-child { border-right: 0; } .ps-content-wrapper-v0 table.sudoku { border-collapse: collapse; border-color: darkgray; margin: 0 auto; margin-top: 8px; margin-bottom: 8px; padding: 8px; } .ps-content-wrapper-v0 table.sudoku colgroup, tbody { border: 3px solid black; } .ps-content-wrapper-v0 table.sudoku td { border: 1px solid black; height: 25px; width: 25px; text-align: center; padding: 0; } .ps-content-wrapper-v0 .left { text-align: left; } .ps-content-wrapper-v0 .right { text-align: right; } .ps-content-wrapper-v0 .code { font-family: monospace; white-space: nowrap; } .ps-content-wrapper-v0 .json-object-array ol, .ps-content-wrapper-v0 .json-object-array ol ul { margin-top: 0px; padding-left: 14px; } .json-object-array li { float: left; margin-right: 30px; margin-left: 10px; } .json-object-array pre { padding: 4px; margin-left: 0px; }
</style>
<div class="ps-content-wrapper-v0">
<p>In a computer security course, you just learned about password decryption. Your fellow student has created their own password encryption method, and they've asked you to test how secure it is. Your task is to recover the original password given the encrypted password provided to you by your classmate.</p>

<p>&nbsp;</p>

<p>At first, it seems impossible. But one day after class, you catch a peek of your classmate's notebook where the encryption process is noted. You snap a quick picture of it to reference later. It says this:</p>

<p>&nbsp;</p>

<p>Given string <em>s</em>, let <em>s[i]</em> represent the <em>i</em><sup>th</sup> character in the string <em>s</em>, using 0-based indexing.</p>

<ol>
	<li>Initially i = 0.</li>
	<li>If <em>s[i]</em> is lowercase and the next character <em>s[i+1]</em> is uppercase, swap them, add a '*' after them, and move to <em>i+2</em>.</li>
	<li>If <em>s[i]</em> is a number, replace it with <em>0</em>,<em>&nbsp;</em>place the original number at the start, and move to <em>i+1</em>.</li>
	<li>Else, move to <em>i+1</em>.</li>
	<li>Stop if <em>i </em>is more than or equal to the string length. Otherwise, go to step 2.</li>
</ol>

<p>&nbsp;</p>

<p>There's even an example mentioned in the notebook. When encrypted, the string "hAck3rr4nk" becomes "43Ah*ck0rr0nk". (<em>Note</em>: the original string, "hAck3rr4nk", does not contain the character <em>0</em>.)</p>

<p>&nbsp;</p>

<p>Note:</p>

<ul>
	<li>The original string always contains digits from 1 to 9 and does not contain 0.</li>
	<li>The original string always contains only alpha-numeric characters.</li>
</ul>

<p>&nbsp;</p>

<p>Using this information, your task is to determine the original password (before encryption) when given the encrypted password from your classmate.</p>

<p>&nbsp;</p>
<strong>Function Description</strong>

<p>Complete the function <em>decryptPassword</em> in the editor below. <em>decryptPassword</em> must return the original password string before it was encrypted by your classmate.</p>

<p>&nbsp;</p>

<p><em>decryptPassword</em> has the following parameter:</p>

<p>&nbsp;&nbsp;&nbsp; <em>s:</em>&nbsp; the password string after it was encrypted by your classmate</p>

<p>&nbsp;</p>

<p class="section-title">Constraints</p>

<ul>
	<li>
	<p>1 ≤ length of <em>s</em> ≤ 10<sup>5</sup></p>
	</li>
	<li>
	<p><em>s</em> can contain Latin alphabet characters (a-z, A-Z), numbers (0-9), and the character '*'.</p>
	</li>
</ul>

<p>&nbsp;</p>

<details><summary class="section-title">Input Format For Custom Testing</summary>

<div class="collapsable-details">
<p>The first line contains the password string obtained after it was encrypted by your classmate.</p>
</div>
</details>
<!-- </StartOfInputFormat> DO NOT REMOVE THIS LINE-->

<details><summary class="section-title">Sample Case 0</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<pre>51Pa*0Lp*0e
</pre>

<p class="section-title">Sample Output</p>

<pre>aP1pL5e</pre>

<p class="section-title"><span class="ps-content-wrapper-v0"><span class="collapsable-details">Explanation</span></span></p>

<p>If we apply the sequence of operations on the string aP1pL5e, we get the string 51Pa*0Lp*0e.</p>

<ol>
	<li>We start at the letter&nbsp;<em>a</em> since i = 0.</li>
	<li>Since a is lowercase and the next character <em>P&nbsp;</em>is uppercase, we swap them, add a '*' after, and move to the next designated character (i+2). So currently it is <strong>Pa*1pL5e</strong>.</li>
	<li>Now we're on the character <em>1</em>. This is a number, so we replace it with <em>0</em>, put the original number <em>1</em>&nbsp;at the start, and continue to the next character (i+1). Now it is <strong>1Pa*0pL5e</strong>.</li>
	<li>We're still in the middle of the string (<em>i</em> does not equal the string length), so we repeat the process again.</li>
</ol>

<p>&nbsp;</p>

<p>After that, <strong>1Pa*0<span style="color:#e74c3c;">p</span>L5e</strong> becomes <strong>1Pa*0<span style="color:#e74c3c;">Lp*</span>5e</strong>. Then, <strong>1Pa*0Lp*<span style="color:#e74c3c;">5</span>e</strong> becomes <strong><span style="color:#e74c3c;">5</span>1Pa*0Lp*<span style="color:#e74c3c;">0</span>e</strong>. Since <em>e</em>&nbsp;is at the end of the string, it can't be swapped with the next character. Thus, aP1pL5e becomes 51Pa*0Lp*0e when encrypted.</p>
</div>
</details>

<details><summary class="section-title">Sample Case 1</summary>

<div class="collapsable-details">
<p class="section-title">Sample Input For Custom Testing</p>

<pre>pTo*Ta*O</pre>

<p class="section-title">Sample Output</p>

<pre>poTaTO</pre>

<p class="section-title"><span class="ps-content-wrapper-v0"><span class="collapsable-details">Explanation</span></span></p>

<p>If we apply the sequence of operations on the string poTaTO, we get the string pTo*Ta*O.</p>

<ol>
	<li>We start at the letter&nbsp;<em>p</em> since i = 0.</li>
	<li>The character&nbsp;<em>p</em>&nbsp;is lowercased, but the next character is also lowercased. So there's no need to swap them.</li>
	<li>We move on to the next character (i+1), which is&nbsp;<em>o</em>. Now, since&nbsp;<em>o</em>&nbsp;is followed by capital&nbsp;<em>T</em>, we swap them, add a '*' after, and move to the next designated character (i+2). So currently it is <strong>pTo*aTO</strong>.</li>
	<li>Moving to character&nbsp;<em>a</em>, it is followed by a capitalized letter, so we likewise swap these, add a '*' after, and move to i+2. Now it is <strong>pTo*Ta*O</strong>.</li>
	<li>
<em>O</em>&nbsp;is at the end of the string, we stop there.</li>
</ol>

<p>&nbsp;</p>

<p>Thus, poTaTO becomes pTo*Ta*O when encrypted.</p>
</div>
</details>
</div>
</div></div></section></div>

'''
import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
  # Write your code here
  skip_count = 0
  digit_q = []
  pwd = ''
  for i in range(len(s)):
    if skip_count > 0:
      skip_count -= 1
      continue
    c = s[i]
    if c == '0':
      pwd += digit_q.pop()
    elif c.isalpha() and c.isupper() and i+2 < len(s) and s[i+1].islower and s[i+2] == '*':
      pwd += s[i+1] + s[i]
      skip_count = 2 # skip next two
    elif c.isdigit():
      digit_q.append(c)
    else:
      pwd += c
  return pwd



if __name__ == '__main__':
  e_pwd = "43Ah*ck0rr0nk"
  pwd = decryptPassword(e_pwd)

  print(pwd)