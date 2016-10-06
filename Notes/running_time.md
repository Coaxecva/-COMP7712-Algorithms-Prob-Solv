- Running time is proportional to the number of "steps".
- Running time is relative to c * (number of steps).

O(n^2) - it takes at most proportional to n^2 steps.

If f(n) is in O(n^2) then, f(n) <= c*n^2, when n is large. For some number c>0.

O(n^2) = { n^2, 2n^2, 3n^2, 0.5n^, 10.7n^2, .... , 10n+5 , ...}
10n+5 <= 10n^2 + 5n^2 = 15n^2.   c=15.
f(n)=10+5 <= 15*n^2.  Therefore, f(n) is in O(n^2)

Definition: if f(n) is in O(g(n)), then f(n) <= c * g(n), when n is large.
Definition: if f(n) is in Omega(g(n)), then f(n) >= c * g(n), when n is large.

f(n) = 10n^2 + 5n >= 1 * n^2 for n>1. Therefore, f(n) is in Omega(n^2)

10n^2 + 5n is in O(n^3)???

Is is true? 10n^2 + 5n >= c * n^3, when n is large.  Not possible. 10n^2+5n is
NOT in Omega(n^3).

10n^2 + 5n is in Omega(n^2)? True, c=1.
10n^2 + 5n is in Omega(n)? True, c=1
10n^2 + 5n >= n, for n>1

5n is in Omega(1)?  True, c=1
5n >= 1*1 for n>1.

Definition: 



