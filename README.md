# exercises-python-code
---------------------
Alternating Characters
----------------------
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters AA and BB only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format

The first line contains an integer TT, i.e. the number of test cases.
The next TT lines contain a string each.

Output Format

For each test case, print the minimum number of deletions required.

Constraints

1≤T≤101≤T≤10
1≤1≤ length of string ≤105≤105

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output

3
4
0
0
4

Explanation

AAAA ⟹⟹ A, 3 deletions
BBBBB ⟹⟹ B, 4 deletions
ABABABAB ⟹⟹ ABABABAB, 0 deletions
BABABA ⟹⟹ BABABA, 0 deletions
AAABBB ⟹⟹ AB, 4 deletions because to convert it to AB we need to delete 2 A's and 2 B's


Introduction to Sets
--------------------

Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
Average=SumofDistinctHeightsTotalNumberofDistinctHeights
Average=SumofDistinctHeightsTotalNumberofDistinctHeights

Input Format

The first line contains the integer, NN, the total number of plants.
The second line contains the NN space separated heights of the plants.

Constraints

0<N≤1000<N≤100

Output Format

Output the average height value on a single line.

Sample Input

10
161 182 161 154 176 170 167 171 170 174

Sample Output

169.375

---------------------------
---------------------------

