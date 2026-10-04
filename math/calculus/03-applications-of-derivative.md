# Applications of Derivatives

## Extrema

By the *Extreme Value Theorem*, in any function $f$ with domain $[a, b]$, there exists $M$ and $m$ in the range of $f$ such that $m <= f(x) <= M$ for all $x$ in $[a,b]$.

In simple terms, every function has a maximum and minimum output value in a given domain.

To find extrema points, one must find all critical points.

> [!info] Critical Points
> A critical point is an interior point in the domain of $f(x)$  where $f'(x)$ is either zero or undefined.
> Points where the $f'(x)$ is zero are also referred to as stationary points. So critical points are the union of stationary points and non-differentiable points.

1. If the domain is restricted, consider the boundary points as well.
2. Find critical inputs using $f'(x)$. Remove any critical points not inside the domain.
3. Find $f(x)$ at all candidate values and determine the maximum/minimum output.

> [!tip] Local vs Absolute Extrema
> Absolute extrema is the largest/smallest point in the whole domain while local extrema are the largest/smallest points as compared to their surroundings.
> The latter is found through the steps listed above. An absolute extrema is automatically a local extema but not vice versa.
> To find all local extrema points, the `first derivative test` might be utilized

## Increasing / Decreasing Functions

> A function that is increasing or decreasing on an interval is said to be `monotonic` on that interval.

Finding monotonicity of a given function $f(x)$ is easy.

1. Find all critical points and points $f$ is undefined.
2. Pick a test point from each interval.
3. Find $f'(x)$ for all those test points.
	1. If $y' > 0$, the function is increasing in that interval.
	2. If $y' < 0$, the function is decreasing in that interval.

## Concavity

Concavity refers to the bending behaviour of the function as the first derivate itself changes behaviour.

Finding the concavity over an interval is easy.

1. Find the second derivative.
2. Find the points you want to check concavity at.
3. Find the second derivative at those points.
	1. If $f''(x) > 0$, the graph is concave up.
	2. If $f''(x) < 0$, the graph is concave down.

> [!tip] Remembering concavity
> Concave up means the arms go *UP*. The point where the concavity is found is the local minima.
> Concave down means the arms go *DOWN*. The point where the concavity is found is the local maxima.
## Related Rates

#todo