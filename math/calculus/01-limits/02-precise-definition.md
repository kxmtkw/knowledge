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
