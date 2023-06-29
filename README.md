# Project-Euler-1-Multiples-of-3-and-5-rounding-error
Project Euler #1: Multiples of 3 and 5 rounding error is part of some Hackerrank's "ProjectEuler+" challenges. <br />
The goal is to find the sum of all multiples of 3 or 5 below N, for a list of T lines as an input containing Ni. <br />
It might look trivial to solve, but N could be anything between 1 and 10^9 so my first approximation of iterating and identifying multiples of 3 and 5 wasn't an option. <br />
For example, N=10^9 took 30.2 seconds to run. Then I started to think about implementing the formula to calculate sum of ‘n’ natural numbers: Sn = n(n+1)/2 <br />
We obtain 2 summations that contain the terms corresponding to the multiplies of 3 and 5, but when adding them we include 2 times the multiplies of 15, then we proceed to subtract the summation of these multiplies leaving: sum3+sum5-sum15. <br />
Adapting this to our code we get a significant optimization from our previous time, getting down to 1ms of runtime for the previous N=10^9 example, a 30.000 times faster code. <br />
Finally, replacing the divisions by integer divisions to avoid rounding errors for borderline cases, we get our final code. <br />
