# Problem Sets for Chapter 1: Introduction to Vectors

## Problem Set 1.1

#### 1. Describe geometrically (line, plane, or all of $\Bbb{R^3}$) all linear combinations of:
  * (a) $\begin{bmatrix}1\\\\2\\\\3\\\\\end{bmatrix}$ and $\begin{bmatrix}3\\\\6\\\\9\\\\\end{bmatrix}$
  * (b) $\begin{bmatrix}1\\\\0\\\\0\\\\\end{bmatrix}$ and $\begin{bmatrix}0\\\\2\\\\3\\\\\end{bmatrix}$
  * (c) $\begin{bmatrix}2\\\\0\\\\0\\\\\end{bmatrix}$ and $\begin{bmatrix}0\\\\2\\\\2\\\\\end{bmatrix}$ and $\begin{bmatrix}2\\\\2\\\\3\\\\\end{bmatrix}$
  
    * _**Solution**_:
      * (a) **line** $\rightarrow$ They are in each others spans (i.e. they are linearly dependent).
      * (b) **plane** $\rightarrow$ They are linearly independent and therefore the second vectors adds new dimensionality.
      * (c) $\Bbb{R^3}$ $\rightarrow$ All three are linearly independent and therefore add a total of three axes.
      
<br><br>

#### 2. Draw $\vec{v} = \begin{bmatrix}4\\\\1\\\\\end{bmatrix}$ and $\vec{w} = \begin{bmatrix}-2\\\\2\\\\\end{bmatrix}$ and $\vec{v} + \vec{w}$ and $\vec{v} - \vec{w}$ in a single $xy$ plane.

  * _**Solution**_:
  
  ![Vector Plot](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_2.png?raw=true)

<br><br>

#### 3. If $\vec{v} + \vec{w} = \begin{bmatrix}5\\\\1\\\\\end{bmatrix}$ and $\vec{v} - \vec{w} = \begin{bmatrix}1\\\\5\\\\\end{bmatrix}$, compute and draw $\vec{v}$ and $\vec{w}$.

  * _**Solution**_:
    * $\vec{v} = \begin{bmatrix}3\\\\3\\\\\end{bmatrix}$ and $\vec{w} = \begin{bmatrix}2\\\\-2\\\\\end{bmatrix}$.
    
    ![Vector_Plot](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_3.png?raw=true)

<br><br>

#### 4. From $\vec{v} = \begin{bmatrix}2\\\\1\\\\\end{bmatrix}$ and $\vec{w} = \begin{bmatrix}1\\\\2\\\\\end{bmatrix}$, find the components of $3\vec{v} + \vec{w}$ and $c\vec{v} + d\vec{w}$.

  * _**Solution**_:
    * $3\vec{v} + \vec{w} = \begin{bmatrix}6 + 1\\\\3 + 2\\\\\end{bmatrix} = \begin{bmatrix}7\\\\5\\\\\end{bmatrix}$ and $c\vec{v} + d\vec{w} = \begin{bmatrix}2c + d\\\\c + 2d\\\\\end{bmatrix}$.
    * Components are $\lbrace 7,\ 5,\ 2c + d,\ c + 2d \rbrace$.
