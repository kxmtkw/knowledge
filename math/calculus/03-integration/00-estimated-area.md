# Estimated Area Under the Graph

To calculate (or rather estimate) the area under the graph, a technique can be used. The technique involves:

1. Dividing the domain into sub intervals.
2. Drawing rectangles at each sub interval whose length extend to the height of the graph.
3. Calculating the area of each rectangle.
4. Summing the area of all the rectangles.

Follow the model: `IRAS` Intervals, Rectangles, Area, Sum

There are three ways in total to find the estimated area.

## Upper Sum
`The height of each rectangle is the taken as the maxmimum output in that interval.`

+ This leads to the rectangles being longer than the graph itself over most of the interval.
+ It gives an estimated area *higher* than the actual area.
+ The formula for upper sum is as follows:
$$A = \Delta x(f(x_1) + f(x_2) + f(x_3) + \dots + f(x_n))$$
+ Here $n$ denotes the number of intervals.
+ The selection of $x$ for each interval depends on the max value of $y$ in that interval.

## Lower Sum
`The height of each rectangle is the taken as the minimum output in that interval.`

+ This leads to the rectangles being shorter than the graph itself over most of the interval.
+ It gives an estimated area *lower* than the actual area.
+ The formula for lower sum is as follows:
$$A = \Delta x(f(x_1) + f(x_2) + f(x_3) + \dots + f(x_n))$$
+ Here $n$ denotes the number of intervals.
+ The selection of $x$ for each interval depends on the min value of $y$ in that interval.

## Midpoint
`The height of each rectangle is the taken as the midpoint of the two boundary points of an interval.`

+ This leads to the rectangles being shorter than the graph itself over most of the interval.
+ It gives an estimated area which can be either *lower or higher* than the actual area.
+ The formula for lower sum is as follows:
$$A = \Delta x(f(\frac{x_1 + x_2}{2}) + f(\frac{x_2 + x_3}{2}) + f(\frac{x_3 + x_4}{2}) + \dots + f(\frac{x_{n-1} + x_n}{2}))$$
+ Here $n$ denotes the number of intervals.
+ The selection of $x$ for each interval depends on the midpoint of the boundary points in that interval.

> [!tip] Intervals
> If the number of intervals is $n$, then the size of each interval can be given by:
> $$\frac{b-a}{n}$$
> More intervals -> More accuracy -> Estimated area is closer to the actual answer
> Error in Area = Actual Area - Estimated Area



