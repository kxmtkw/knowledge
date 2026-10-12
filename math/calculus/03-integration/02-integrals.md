# Integrals

## Deriving from Summation

As it is know, the estimated area under the graph, using the summation notation, can be expressed as:
$$A = \Delta x \cdot \sum_{k=1}^{n} f(c_k) $$
As these intervals can be of different widths, the above formula can be more accurately written as:
$$A = \sum_{k=1}^{n} \Delta x_k \cdot f(c_k) $$
This sum $A$ is known as the `Riemann Series` over an interval. The above formula can also be written as:
$$A = \sum_{k=1}^{n} \Delta x_k \cdot f(a + \Delta x \cdot k)$$
Where $a$ is the starting point of the interval over which the series is applied.

Now, assume that we can change the number of intervals. As we know, more intervals -> more closer to actual area. Applying limit,
$$A = \lim_{n \to \infty} \sum_{k=1}^{n} \Delta x_k \cdot f(c_k)$$
The above formula basically tells us what the area approaches as the number of intervals of the estimated sum reach infinity.
*As the intervals get smaller and smaller, the rectangles more precisely fit the shape of the graph and their overall sum appraoches to the actual area of the graph.*

This is basically the definite intergral.

![Estimation turns into reality](https://www.youtube.com/watch?v=WUvTyaaNkzM)

## Applying the Definite Integral

The general form of the definite integral is:
$$\int_{a}^{b} f(x) dx$$
This calculates the area of the graph from $a$ to $b$. To calculate the definite integral, however, one must find the function whose dervative gives $f(x)$, or basically find the indefinite integral of $f(x)$.

## Finding the Area under the Graph

Some things to keep note of when finding the area under the graph:

1. `Area cannot be negative.` If a negative value is obtained at the end, take its absolute.
2. `Area can also cancel out.` In some cases, when both the graph and the interval is symmetric, the areas can actually cancel eachother out and give zero which is not correct.
	1. For this, first find the points where $f(x) = 0$.
	2. if any of those points lie in $[a, b]$, the graph *might* make a flip so just divide the intervals.
	3. Take the absolute for negative areas and then add.
3. `Flipping the upper and lower limits negates the area`
4. `Average area over an interval be found.` Just divide the definite integral by $1/(b-a)$

#todo