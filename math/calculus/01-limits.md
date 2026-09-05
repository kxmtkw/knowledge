## Limits
If $f(x)$ is defined in an interval containing $c$ (not necessarily at $c$) and $f(x)$ approaches to $L$ as $x$ approaches to $c$, then $L$ is called the limit of $f(x)$ as $x$ approaches $c$.

## Laws & Formulas
#### Arithmetic Laws
- Sum rule
- Difference rule
- Constant multiple rule
- Product rule
- Quotient rule
- Power rule
- Root rule
#### Polynomial Rule
For any polynomial function $f(x)$, the limit as $x \to c$ is always strictly equal to $f(c)$:
$$\lim_{x \to c} f(x) = f(c)$$
#### Sandwich Theorem
Suppose that $g(x) \le f(x) \le h(x)$ for all $x$ in some open interval containing $c$, except possibly at $x = c$ itself.Suppose also that:
$$\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$$
Then:
$$\lim_{x \to c} f(x) = L$$
#### L' Hopital Rule
...

### Solving Limits
- Direct subsitution
- Factoring to remove the undefined state from $0/0$, $\infty/\infty$ and $c/0$ forms
- Rationalization, multiplying by conjugates.
- Divide every term by the highest power, useful for $x \to \infty$ limits.
- Apply theorem/formulas.

## Continuity of a Limit
For a function to be continuous at $c$, the left hand and right hand limits must be equal, even if the function is undefined at $c$.

If a function is defined at $c$ but the left and right hand limits are not equal, then the function is not continous.

## Limits by Precise Definition
This is also called the epsilon-delta definition of the limit. It does not calculate a limit but proves whether a proposed is true or not.
So you cannot use the precise definition to solve an unknown limit but you can use it to verify one.

Given a limit $lim_{x \to a} f(x) = L$ and  an arbitrary $\epsilon$ ,find $\delta$ where $abs(x-a) < \delta$ such that $abs(f(x) - L) < \epsilon$.

### As a Game
Think of it as game:
1. Your opponent will you give you an $\epsilon$ which indicates the minimum deviation from $L$.
2. Your goal is to find $\delta$ such that all $x$ around $c$ at a distance of $\delta$ will give $f(x)$ that is within $\epsilon$ distance of $L$.

Mathematically,
1. Find $\delta$ with the propery that: $$abs(x - c) < \delta$$
2. Such that: $$abs(f(x)-L) < \epsilon$$