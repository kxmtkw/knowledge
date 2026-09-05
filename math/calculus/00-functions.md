## Functions
A mapping from set X to set Y. $$y = f(x)$$
- Domain: X
- Co-Domain: Y
- Range: R (subset of Y)

#### Function Examples
- Ceiling function / Least integar
- Floor function / Greatest integar
- Square root function
- Square function
- Absolute function

> Imagine ceiling and floor functions as actual floors of a building with the integars as the floor numbers.

- Even functions
$$
f(-x) = f(x)
$$
- Odd functions
$$
f(-x) = -f(x)
$$
- Linear functions
$$
y = mx + b
$$
- Constant functions
	- `Slope is zero for such functions`

- Power function
- Algebraic functions
- Trigonometric functions
- Exponential functions
- Logarithmic functions

## Vertical Line Test
- Intesect once -> Function
- Intersect multiple times -> Not a function

## Horizontal Line Test
- Intersect once -> Each y is only given by one x -> one-one function -> inverse exists
- Intersect multiple times -> A single y is given by multiple x -> not one-one -> inverse does not exist

### Piece-Wise Defined Function
A function that is defined differently depending upon its input. For these functions, both the left and the right hand limit must be evaluated b
efore finding the limit.
### Increasing / Decreasing Functions
A function such that $f(x)$ increases as $x$ is increased is an increasing function and a function such that $f(x)$ decreases as $x$ is increased is a decreasing function.

> For the latter, the derivative is positive while for the former, the derivative is negative.

### Proportionality
`Two variables y and x are proportional to one another if one is a constant multiple of the other.`
$$
y = kx
$$
Inversely proportional if it is a multiple of `1/x`

## Combining Functions

### Via operations
Functions f and g can be added, subtracted, multiplied and divided. In each case, domain is:
$$
D(f.g) = D(f) \cap D(g)
$$
- Where $.$ maybe: $+ - * /$
- $g(x) \neq 0$ if $.$ is $/$

### Via composition
Functions f and g are combined.
$$
(f.g)(x) = fg(x) = f(g(x))
$$
- Range of g lies in the domain of f.
- The domain of fg is the set of numbers for which g(x) lies in the domain of f.
- fg != gf

## Shifting and Scaling Function Graphs

### Shifts

#### Vertical Shift
$$
y = f(x) + k
$$
- k > 0 -> graph shifts up
- k < 0 -> graph shifts down
- Think of just modifiying the output.

#### Horizontal Shift
$$
y = f(x + h)
$$
- h > 0 -> graph shifts left
- h < 0 -> graph shifts right
- Its opposite because x has to adapt to the shift to get the same value of y.

### Scaling

For c > 1:
- $y = cf(x)$ causes vertical stretch.
- $y = (1/c)f(x)$ causes vertical compression.
- $y = f(cx)$ causes horizontal compression.
- $y = f(x/c)$ causes horizontal stretch.

> Vertical stretch = Horizontal compress & Vertical compress = Horizontal stretch

> All scaling is done by the factor of c.

#### Refection
For c = -1:
- $y = -f(x)$ causes reflection across x axis.
- $y = f(-x)$ causes reflection across y axis.
- $y = -f(-x)$ causes reflection across the origin.


## Determining Domains and Ranges

### Domains
For domains, simply assume the domain to be $R$ and then determine the intervals in the function is defined or not.

### Ranges
Ranges are a bit hard. Few strategies include:
- Finding inverse and determining where the function $x = f^{-1}(y)$ is defined. The domain of the inverse is the range of the original.
- Split the function into intervals where it becomes invertible (if not invertible). Intervals must be strictly increasing or decreasing so horizontal line test can pass.
- Use calculus. Determine critical points and edges. The range is within the absolute extrema.
- For standard functions like say the parabola, $y = ax^2 + bx + c$, the range is $[a, \infty)$ if $a>0$ else  $(-\infty, a]$
