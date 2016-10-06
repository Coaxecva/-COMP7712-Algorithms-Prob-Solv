T(n) = n^2 + 4T(n/2) is in Theta(n^2 log n)
T(n) = n^3 + 4T(n/2) is in Theta(n^3)
T(n) = n^3 + 10T(n/2) is in Theta(n^log_2(10))  3 = log_2(8) < log_2(10)

T(n) = n^d + aT(n/b)
(1) if d=log_b(a), T(n) in Theta(n^d * log n)
(2) if d != log_b(a), T(n) in Theta(n^max{d, log_b(a)})