# Project-Euler-1-Multiples-of-3-and-5
This problem is part of some of Hackerrank's "ProjectEuler+" challenges. The goal is to find the sum of all multiples of 3 or 5 below N, given a list of T lines as input, where each line contains an integer Ni. <br />
At first glance, this may seem trivial, but since N can range between 1 and 10^9, my initial approach of iterating and identifying multiples of 3 and 5 wasn't feasible. For example, with N = 10^9, my code took 30.2 seconds to run. <br />
I then considered using the formula for the sum of the first ‘n’ natural numbers: S_n = n(n+1)/2. From this, we can derive two sums for the multiples of 3 and 5. However, when summing them, the multiples of 15 are counted twice, so we subtract the sum of the multiples of 15. This leaves us with the formula: sum3 + sum5 - sum15.<br />
By adapting this formula to the code, I achieved a significant optimization, reducing the runtime to just 1ms for the N = 10^9 case — a 30,000x speed improvement.<br />
Finally, I arrived at the final solution by using integer division to avoid rounding errors in edge cases. <br />
<br />
Both solutions — the older, iterative one, and the new arithmetic one — can be found in the repository as "solution_old.py" and "solution.py," respectively.
