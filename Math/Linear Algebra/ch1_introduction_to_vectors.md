# Chapter 1: Introduction to Vectors

_The first chapter attempts to give the reader a basic understanding of the basic units of operation/computation for linear algebra: vectors and matrices._

* 1.1 - Vectors and Linear Combinations
* 1.2 - Lengths and Dot Products
* 1.3 - Matrices

---

## 1.1 Vectors and Linear Combinations

### Video material
  * [3Blue1Brown - Vectors, what even are they? (Essentials of Linear Algebra Ch. 1)](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1)

  * [3Blue1Brown - Linear combination, span, and basis vectors. (Essentials of Linear Algebra Ch. 2)](https://www.youtube.com/watch?v=k7RM-ot2NWY&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=2)


### Vector Addition

Vector addition is simple. Just think of it as adding the same coordinates with each other. For example let's say we have two vectors,

$$\vec{v} = \begin{bmatrix}
1\\\\
2\\\\
\end{bmatrix}$$
and
$$\vec{w} = \begin{bmatrix}
3\\\\
4\\\\
\end{bmatrix}$$

The result of adding these two vectors would be

$$\vec{v} + \vec{w} = \begin{bmatrix}
1+3\\\\
2+4\\\\
\end{bmatrix}$$


At the start of the chapter, Professor Strang states that "You can't add apples and oranges." This makes sense because we can only add objects that are the same.

※ Note: The algebraic commutative property of $a + b = b + a$ also applies to vectors.


### Scalar Multiplication

Scalar multiplication is also simple. You're just multiplying ("broadcasting") the scalar to each component of the vector. If we take the vector $\vec{v}$ from earlier,

$$
\begin{align}
\vec{v} & = 2 \times \begin{bmatrix}
1\\\\
2\\\\
\end{bmatrix} \\\\
& = 
\begin{bmatrix}
2\\\\
4\\\\
\end{bmatrix}
\end{align}
$$


### Linear Combinations

By definition, a _**linear combination**_ is combining addition and scalar multiplication.

In simpler terms, the sum of the vectors multiplied by any scalar(s) is called a linear combination. $c\vec{v} + d\vec{w}$ is a linear combination of the vectors $\vec{v}$ and $\vec{w}$.

_**§ The three notions of vector addition, scalar multiplication, and linear combinations are central to linear algebra. We'll get into more detail later and why they're so important.**_


### Vectors in Three Dimensions

Vectors in three dimensions are analogous to vectors in two dimensions. The only difference is that they have an extra component to account for the third dimension.


### The Important Questions

This section addresses some important geometric aspects of linear algebras.

1. What is the picture of _all_ combinations on $c\vec{u}$?
2. What is the picture of _all_ combinations $c\vec{u} + d\vec{v}$?
3. What is the picture of _all_ combinations $c\vec{u} + d\vec{v} + e\vec{w}$?

The answers to these questions is relatively simple and even intuitive if you put your focus on the fact that a vector is essentially _pointing to a certain point_.

This means that if we have a vector $\vec{u}$ that is pointing to a certain point in space, then the linear combinations of all of the different points that make up $c\vec{u}$ will essentially be a line. For example, let's say that the vector $\vec{u}$ is as follows:

$$\vec{u} =
\begin{bmatrix}
1\\\\
2\\\\
\end{bmatrix}
$$

Now, let's say that the values for the scalar $c$ in $c\vec{u}$ are $0$,$\ 0.5$,$\ 1$,$\ 1.5$,$\ 2$, and$\ 2.5$. In other words, $c = \\{0,\  0.5,\ 1,\ 1.5,\ 2,\ 2.5 \\}$.

The linear combinations, then, of $c\vec{u}$ would be:

$$c\vec{u} =
\begin{Bmatrix}
\begin{bmatrix}
  0\\\\
  0\\\\
\end{bmatrix},\ 
\begin{bmatrix}
  0.5\\\\
  1\\\\
\end{bmatrix},\ 
\begin{bmatrix}
  1\\\\
  2\\\\
\end{bmatrix},\ 
\begin{bmatrix}
  1.5\\\\
  3\\\\
\end{bmatrix},\ 
\begin{bmatrix}
  2\\\\
  4\\\\
\end{bmatrix},\ 
\begin{bmatrix}
  2.5\\\\
  5\\\\
\end{bmatrix}
\end{Bmatrix}
$$

Let's write some code to visualize these results. As stated earlier, it's convenient if we think of vectors as essentially _**arrows that point to a specific point in space**_. The $x$-values would be the first components of each vector, and the $y$-values are the second. The code to visualize this is as follows:

```Python
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 3, 0.5)
y = np.array([(num * 2) for num in x])
zeros = (np.zeros(x.shape[0]), np.zeros(x.shape[0]))
colors = ['r', 'b', 'g', 'c', 'm', 'y']

plt.quiver(*zeros, x, y, color=colors, angles='xy', scale_units='xy', scale=1)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()

plt.show()
```

This code produces the following image:

![Vector $\vec{u}$ linear combinations](https://github.com/seankala/ml_study_group/blob/master/Images/Math/vector_plots.png?raw=true)

It's not difficult to see that if we were to take every single real value of $c$ and multiplied it to the vector $\vec{u}$, we would eventually get a straight line.

The plots for the second and third questions are a bit harder to visualize (I'm actually not sure if it's possible to simply visualize it without actual animations), so I'll leave it out but if you feel the need for visual stimulus then I highly recommend watching the 3Blue1Brown videos posted at the start.

---

## 1.2 Lenghts and Dot Products

### Video Material:

[3Blue1Brown - Dot Products and Duality | Essence of linear algebra, chapter 9](https://www.youtube.com/watch?v=LyGKycYT2v0&t=2s)

The _**dot product**_ is another word for the _**inner product**_. The name is derived from the literal "dot" in between two vectors.

The actual computation is as follows:

Let's say we have two vectors, $\vec{v}$ and $\vec{w}$ each with a total of $n$ components. Their dot product, $\vec{v} \cdot \vec{w}$ would be:

$$\begin{align}
\vec{v} \cdot \vec{w} & = \sum_{i = 1}^{n}v_iw_i\\\\
& = v_1w_1 + v_2w_2 + \ldots + v_nw_n
\end{align}
$$

The significance of the dot product is that it measures _**"how much of one vector is in the direction of the other."**_

The 3Blue1Brown video says that the dot product of two vectors is **(length of projection of first vector onto second vector) $\times$ (length of second vector)**.

Let's look at an example:

![alt-text](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-2_example1.png?raw=true)

In the above figure, we have two vectors: $\vec{v}$ (blue) and $\vec{w}$ (orange). There are also two extra lines: the red line represents the _**component of $\vec{w}$ on $\vec{v}$**_ and the black line is just a line that illustrates that the component of one vector on the other is obtained by drawing a perpendicular line.

The component of $\vec{w}$ on $\vec{v}$ simply signifies _**how much of $\vec{w}$ is in the direction of $\vec{v}$**_.
  * This can be easily understood by keeping in mind the parallelogram method. Let's say we had another vector $\vec{u}$ that went in the same direction in the same amount as the perpendicular black dotted line. Then $\vec{w}$ would equal the sum of $\vec{u}$ along with the vector whose magnitude is $\text{comp}_{\vec{v}}\vec{w}$. The following figure depicts it:
  
![alt-text](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-2_example2.png?raw=true)

In this image, we can see that $\vec{w}$ can be composed of the two vectors to its left, hence the *component of $\vec{w}$ on $\vec{v}$*. Technically speaking, this is the projection of $\vec{w}$ on $\vec{v}$, but you get the message.

※ The component of $\vec{v}$ onto $\vec{w}$ is also known as the _**scalar projection**_, since its taking the length (i.e. a scalar value) of the projection. The computational calculation is as follows:

$$\text{$\mathbf{comp}$}_{\vec{v}}\vec{w} = \frac{\vec{v} \cdot \vec{w}}{\Vert \vec{v} \Vert}$$

Some applications of the dot product are when finding out the angle between two vectors, calculating work done in physics, etc.

<br>

### Lengths and Unit Vectors

* The _**length**_ of a vector $\vec{v}$ is the square root of $\vec{v} \cdot \vec{v}$ (its dot product with itself):

$$\text{$\mathbf{length}$}(\vec{v}) = \Vert \vec{v} \Vert = \sqrt{\vec{v} \cdot \vec{v}}$$

* A _**unit vector**_ is a vector whose length is $1$. If you want to obtain the unit vector that is in the same direction as vector $\vec{v}$, simply divide $\vec{v}$ by its length $\Vert \vec{v} \Vert$.

$$\vec{u}_\vec{v} = \frac{\vec{v}}{\Vert \vec{v} \Vert}$$

<br>

### The Angle Between Two Vectors

* The dot product between two vectors is $0$ when they are perpendicular.
  * If two vectors are perpendicular, then the length of their projection onto the other is $0$.
  
* **Cosine Formula**
  * If $\vec{v}$ and $\vec{w}$ are nonzero then
$$\frac{\vec{v} \cdot \vec{w}}{\Vert \vec{v} \Vert \Vert \vec{w} \Vert} = \cos{\theta}$$

* [**Cauchy-Schwarz Inequality**](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality#Applications)
  * $\vert \vec{v} \cdot \vec{w} \vert \le \Vert \vec{v} \Vert \Vert \vec{w} \Vert$
