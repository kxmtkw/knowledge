## One-Sided Limits

A normal limit can approach from either side but a one sided limit allows the limit to be approached from either the left ($-ve$):
$$\lim_{x \to c-} f(x)$$
or right ($+ve$) side:
$$\lim_{x \to c+} f(x)$$

A limit of a function at $c$ only exists if:
$$ \lim_{x \to c-} f(x) = \lim_{x \to c+} f(x)$$
i.e.
1. Both the left and the right limit exists.
2. Both limits are equal.

If any of the above two do not hold, then the limit **Does Not Exist (DNE)**.

> [!info]  For polynomials
> Limits exist at all points for polynomial functions.

> [!info] Approaching different values
> The left and right hand limits can approach different values. In that case, the limit does not exist because *condition 2* was invalidated.

## Continuity

> A function is said to continuous at a point $c$ if:

1. $f(c)$ exists, i.e. $c$ is in the domain of $f$.
2. $\lim_{x \to c} f(x)$ exists (both the right and left limits exist, and they are equal).
3. $\lim_{x \to c} f(x) = f(c)$ holds.

If a function is continuous at $c$, it basically means that there are no jumps around or at $c$.

> [!info] Differentiability implies continuity
> If a function $f(x)$ is differentiable at $c$ i.e. $f'(c)$ exists, then $f(x)$ is continous at $c$.

### One-Sided Continuity

A function can also be continuous from one side if $f(c)$ equals either the left or right hand limit but not both. The function is said to be right continous or left continous appropriately.
## Relation with Graphs

1. If the above conditions of continuity hold:
	+ The graph is completely continous at that point.
2. If RHL = LHL but $f(c)$ is not equal to either of them:
	+ The graph has a hole at that point.
3. If RHL != LHL but $f(c)$ is equal to one of them:
	+ The graph has jump at that point.
4. If RHL or LHL do not exist:
	+ The graph has an endpoint at that point.
