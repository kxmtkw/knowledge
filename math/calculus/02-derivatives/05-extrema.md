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
