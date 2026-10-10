# Summation
-> Summing up expressions
$$\sum_{k=1}^{n} c_k = c_1 + c_2 + c_3 + \dots + c_n$$
It is basically a `for loop` that counts till it reaches the ending index. In coding, it would basically translate to:

```c
for (int k = 1; k <= n; k++) {
	sum += f(k)
}
```

## Natural Number Sums

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2$$

> [!note] Proofs!
> Proofs of the above three formulas is really important and must be remembered.

## Estimated Sums in Summation Notation

Following this, the estimated sums in the previous note can be rewritten as:
$$A = \Delta x \cdot \sum_{k=1}^{n} f(c_k) $$
Where:
+ $n$ -> Number of intervals
+ $\Delta x$ -> Size of each interval
+ $c_k$ -> Minimum/Maximum for lower/upper sum respectively, or midpoint for midpoint method. 

## Rules

Some rules to remember:
1. Sum Rule (distributes over $+$)
2. Different Rule (distributes over $-$)
3. Constant Multiple Rule (if a constant $c$ exists in all terms, it can be taken common)
4. Constant Rule (if the sum is just for a constant $c$, then the sum is just $n \cdot c$)