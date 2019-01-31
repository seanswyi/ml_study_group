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
\vec{v} & = 2\ \times\ \begin{bmatrix}
1\\\\
2\\\\
\end(bmatrix)
& = \begin{bmatrix}
2\\\\
4\\\\
\end{bmatrix}
$$
