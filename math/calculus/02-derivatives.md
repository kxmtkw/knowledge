# Derivatives

## Definition

> The derivative of a functon $f(x)$ with respect to the variable $x$ is the function $f'$ whose value at $x$ is defined as:

$$ f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$


> [!info] Non-existent Limit
> It is obvious that if the limit does not exist at $x$, then $f'$ is undefined at $x$. This rule does not hold for boundary points.

> [!info] Differentiability -> Continuity
> If $f$ is differentiable at $x = c$, then it is continuous at $x$.

## Finding Derivatives

1. By defintion (also known as derivative from first principles)
2. Using rules.
	1. Sum
	2. Difference
	3. Product
	4. Quotient
	5. Power
	6. Exponents
3. By Chain Rule

## Derivative as Instantaneous Change

Derivative represents the instantaneous change of a quantity with respect to another quantity.

![Paradox of Derivatives](https://www.youtube.com/watch?v=9vKqVkMQHKk&pp=ygUmM2JsdWUxYnJvd24gdGhlIHBhcmFkb3ggb2YgZGVyaXZhdGl2ZXM%3D)

As 3Blue1Brown explains, it is kind of paradoxical for derivative to be *instantaneous change* as change is always recoreded over some difference. The derivative is actually an approximation of the change that occurs as the difference between the two reference values approaches zero. It never does reach zero but as it approaches zero, the "rate" of the graph between those two points approaches to a single value and that single value is what the derivative represents.

## Link with Tangents and Secants

Imagine a function $f(x)$ with a curved graph. 

A secant is a line that touches a graph at exactly two points. Imagine these points to be $a$ and $b$. The slope of the secant will then represent the average rate of change over the interval $[a, b]$ and is given by:
$$m = \frac{f(b)-f(a)}{b-a}$$
The tangent is a line that touches the graph at only point (say $c$). The slope of the tangent will represent the derivative of $f(x)$ at $x=c$. 

> [!tip] Tangents as Single Point Secants
> As derivatives are given when you decrease the distance between the two boundary points such that the distance approaches zero. Tangents are the same. As the two points of the secants are brought closer and closer, eventually a single point will be reached and it will look like a tangent.

## Chain Rule

Chain rule is used for taking the derivatives of composite or nested functions. Practically, it is just applying the dervative rules recursively until the expression cannot be further differentiated.

> [!note]
> Chain rule can also be used to find rates for related changes. 
> If $x$ -> $y$ and $y$ -> $z$ then $x$ -> $z$ change can also be found.

## Implicit Differentiation

1. Differentiate both sides of the equation with respect to $x$, treating $y$ as a differentiable function of $x$.
2. Collect the terms with $\frac{dy}{dx}$ on one side of the equation and solve for $\frac{dy}{dx}$.

# Applications of Derivatives

## Extrema

## Increasing / Decreasing Functions

## Concavity

#todo

