Problem :  Height of a Binary Tree<br>
URL : https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem <br>
Tags : Easy , Data - Structures,Tree<br>
There can be two solutions : Recursive , Iterative  For explanation please refer to GeeksForGeeks<br>
# Iterative : LEVEL ORDER TRAVERSAL <br>
<p>The idea is to traverse level by level. Whenever move down to a level, increment height by 1 (height is initialized as 0). Count number of nodes at each level, stop traversing when count of nodes at next level is 0.
Following is detailed algorithm to find level order traversal using queue.</p>
