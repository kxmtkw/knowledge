## Link with Tangents and Secants

Imagine a function $f(x)$ with a curved graph. 

A secant is a line that touches a graph at exactly two points. Imagine these points to be $a$ and $b$. The slope of the secant will then represent the average rate of change over the interval $[a, b]$ and is given by:
$$m = \frac{f(b)-f(a)}{b-a}$$
The tangent is a line that touches the graph at only point (say $c$). The slope of the tangent will represent the derivative of $f(x)$ at $x=c$. 

> [!tip] Tangents as Single Point Secants
> As derivatives are given when you decrease the distance between the two boundary points such that the distance approaches zero. Tangents are the same. As the two points of the secants are brought closer and closer, eventually a single point will be reached and it will look like a tangent.

### Mean Value Theorem

The above formula for $m$ is given by the *Mean Value Theorem*. The theorem states that:

> Suppose $y = f(x)$ is continuous over the closed interval $[a,b]$ and differentiable over the open interval $(a,b)$. Then there is atleast one point $c$ in $(a,b)$ at which:`
> $$f'(c) = \frac{f(b)-f(a)}{b-a}$$

Now this may seem a bit weird since the left side gives the average rate of change which is not equal to the instantaneous rate of change.
Actually the derivate simply states that in between $a$ and $b$, there exists atleast one $c$ where both the average and instantaneous rates are equal to eachother.
