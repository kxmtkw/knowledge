# Limits

> If $f(x)$ is defined in an interval containing $c$ (not necessarily at $c$) and $f(x)$ approaches to $L$ as $x$ approaches to $c$, then $L$ is called the limit of $f(x)$ as $x$ approaches $c$.

## Laws & Formulas

### Arithmetic

1. Sum rule
$$\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$$
2. Difference rule
$$\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)$$
3. Constant multiple rule
$$\lim_{x \to a} [c \cdot f(x)] = c \cdot \lim_{x \to a} f(x)$$
4. Product rule
$$\lim_{x \to a} [f(x) \cdot g(x)] = \left(\lim_{x \to a} f(x)\right) \cdot \left(\lim_{x \to a} g(x)\right)$$
5. Quotient rule
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{where } \lim_{x \to a} g(x) \neq 0$$
6. Power rule
$$\lim_{x \to a} [f(x)]^n = \left[\lim_{x \to a} f(x)\right]^n$$
7. Root rule
$$\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}$$

### Polynomial Rule

For any polynomial function $f(x)$, the limit as $x \to c$ is always strictly equal to $f(c)$:
$$\lim_{x \to c} f(x) = f(c)$$

### Sandwich Theorem

Suppose that $g(x) \le f(x) \le h(x)$ for all $x$ in some open interval containing $c$, except possibly at $x = c$ itself. Suppose also that:
$$\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$$
Then:
$$\lim_{x \to c} f(x) = L$$

### L' Hopital Rule
...

### Solving Limits

1. Direct subsitution in case of simple polynomials.
2. Factoring to remove the undefined state from $0/0$, $\infty/\infty$ and $c/0$ forms
3. Rationalization, multiplying by conjugates.
4. Divide every term by the highest power, useful for $x \to \infty$ limits.
5. Apply theorem/formulas.

> [!tip] FFRD
> Remmber how to solve limits using `FFRD`:
> + F -> Formulas
> + F -> Factorization
> + R -> Rationalization
> + D -> Division by highest power

## Limits by Precise Definition

This is also called the epsilon-delta definition of the limit. It does not calculate a limit but proves whether a proposed limit is true or not.
So you cannot use the precise definition to solve an unknown limit but you can use it to verify one.

Given a limit $lim_{x \to a} f(x) = L$ and  an arbitrary $\epsilon$ ,find $\delta$ where $abs(x-a) < \delta$ such that $abs(f(x) - L) < \epsilon$.

### As a Game
Think of it as game:
1. Your opponent will you give you an $\epsilon$ which indicates the minimum deviation from $L$.
2. Your goal is to find $\delta$ such that all $x$ around $c$ at a distance of $\delta$ will give $f(x)$ that is within $\epsilon$ distance of $L$.

Mathematically,
1. Find $\delta$ with the propery that: $$abs(x - c) < \delta$$
2. Such that: $$abs(f(x)-L) < \epsilon$$

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

## Asymptotes

> A line on which a function graph settles as it reaches extreme values is referred to as an asymptote.

The function graph *can* touch the line and even cross it, the asymtote is just a line on which the graph seems to settle.

### Horizontal Asymptote

For horizontal asymptote, the graph settles on a horizontal line as $x \to \infty$ or $x \to -\infty$.
If the $x$ approaches infinity, the graph would settle on a single value $L$ which would give the $y$ value (basically the line is $y = L$).
$$\lim_{x \to \infty} f(x) = L$$
$$ y = L $$

### Vertical Asymptote

For a vertical asymptote, the graph settles on a vertical line as  $x \to c$. In this case, $y$ is the one approaching $\infty$. For a particular value of $x$, the graph would go to infinity.
$$\lim_{x \to c} f(x) = \infty$$
$$x = c$$
### Slanted / Oblique Asymptotes

For such asymptotes, the graph settles on a slanted line instead of a horizontal or vertical one.
For these graphs, no extreme value is required, the graph naturally settles to that line due to its slope.

#### For a function f(x) = P(x)/Q(x)

1. `Degree of Numerator < Degree of Denominator` The asymptote is horizontal and it is always the line $y = 0$. I.e. the graph approaches the x axis.
2. `Degree of Numerator = Degree of Denominator` The asymptote is horizontal and it is the line $y = a/b$ where $a$ is the leading coefficient of the numerator and $b$ is the leading coefficient of the denominator.
3. `Degree of Numerator > Degree of Denominator` No asymptote exists.
4. `Denominator = 0` A vertical asymtote exists at $x= c$ where $c$ is causes the denominator to become zero.
5. `Degree of Numerator - Degree of Denominator = 1` When degree of numerator is one greater than the denominator, then a slanted asymptote exists. The slope of this asymptote is $a/b$ where $a$ and $b$ are the leading coefficients of the numerator and denominator respectively.