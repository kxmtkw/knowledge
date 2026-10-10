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
