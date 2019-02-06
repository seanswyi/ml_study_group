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

<br><br>

#### 5. Compute $\vec{u} + \vec{v} + \vec{w}$ and $2\vec{u} + 2\vec{v} + \vec{w}$. How do you know $\vec{u}$, $\vec{v}$, and $\vec{w}$ lie in a plane?

$$\vec{u} = \begin{bmatrix}1\\\\2\\\\3\\\\\end{bmatrix},\ \vec{v} = \begin{bmatrix}-3\\\\1\\\\-2\\\\\end{bmatrix},\ \vec{w} = \begin{bmatrix}2\\\\-3\\\\-1\\\\\end{bmatrix}$$

  * _**Solution**_:
    * $\vec{u} + \vec{v} + \vec{w} = \begin{bmatrix}1-3+2\\\\2+1-3\\\\3-2-1\\\\\end{bmatrix} = \begin{bmatrix}0\\\\0\\\\0\\\\\end{bmatrix}$.
    * $2\vec{u} + 2\vec{v} + \vec{w} = \begin{bmatrix}2-6+2\\\\4+2-3\\\\6-4-1\\\\\end{bmatrix} = \begin{bmatrix}-2\\\\3\\\\1\\\\\end{bmatrix} = -\vec{w}$
    * We can see that the vector $\vec{w}$ can be expressed as a linear combination of the other two vectors in the given vector set, $\vec{u}$ and $\vec{v}$. This implies that there are only two axes we can work with because $\vec{u}$ and $\vec{v}$ account for two axes, but $\vec{w}$ lies on one of those axes.

<br><br>

#### 6. Every combination of $\vec{v} = (1, -2, 1)$ and $\vec{w} = (0, 1, -1)$ has components that add to *_____*. Find $c$ and $d$ so that $c\vec{v} + d\vec{w} = (3, 3, -6)$.

  * _**Solution**_:
    * *_____* = $(0, 0, 0)$
      * $c\vec{v} + d\vec{w} = \begin{bmatrix}c\\\\-2c+d\\\\c-d\\\\\end{bmatrix}$
      * $c + (-2c + d) + (c - d) = 0$
    * $c = 3$ and $d = 9$.

<br><br>

#### 7. In the $xy$ plane mark all nine of these linaer combinations: $c\begin{bmatrix}2\\\\1\\\\\end{bmatrix} + d\begin{bmatrix}0\\\\1\\\\\end{bmatrix}$ with $c = 0,\ 1,\ 2$ and $d = 0,\ 1,\ 2$.

  * _**Solution**_:
    * linear_combinations = $\begin{Bmatrix} \begin{bmatrix}0\\\\0\\\\\end{bmatrix},\ \begin{bmatrix}0\\\\1\\\\\end{bmatrix},\ \begin{bmatrix}0\\\\2\\\\\end{bmatrix},\ \begin{bmatrix}2\\\\1\\\\\end{bmatrix},\ \begin{bmatrix}4\\\\2\\\\\end{bmatrix},\ \begin{bmatrix}2\\\\2\\\\\end{bmatrix},\ \begin{bmatrix}2\\\\3\\\\\end{bmatrix},\ \begin{bmatrix}4\\\\3\\\\\end{bmatrix},\ \begin{bmatrix}4\\\\6\end{bmatrix}\end{Bmatrix}$
    
    * Graph:
    
    ![1.1 7](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_7.png?raw=true)

<br><br>

#### 8. The parallelogram in Figure 1.1 has diagnoal $\vec{v} + \vec{w}$. What is its other diagonal? What is the sum of the two diagonals? Draw that vector sum.

  * _**Solution**_
    * The other diagonal is $\vec{v} - \vec{w}$.
    * $(\vec{v} + \vec{w}) + (\vec{v} - \vec{w}) = 2\vec{v} = \begin{bmatrix}8\\\\2\end{bmatrix}$
    
    * Graph
    
    ![1-1 8](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_8.png?raw=true)

<br><br>

#### 9. If three corners of a parallelogram are $(1, 1)$, $(4, 2)$, and $(1, 3)$, what are all three of the possible fourth corners? Draw two of them.

  * _**Solution**_
    * The three possible points for the fourth corner are: $(-2, 2),\ (4, 0),\ (4, 4)$.

<br><br>

#### 10. Find vectors $\vec{v}$ and $\vec{w}$ so that $\vec{v} + \vec{w} = (4,\ 5,\ 6)$ and $\vec{v} - \vec{w} = (2,\ 5,\ 8)$. This is a question with *_____* unknown numbers, and an equal number of equations to find those numbers.

  * _**Solution**_
    * *_____* : 6 unknown numbers
    * $\vec{v} = \begin{bmatrix}v_1\\\\v_2\\\\v_3\\\\\end{bmatrix}\ \text{and}\ \vec{w} = \begin{bmatrix}w_1\\\\w_2\\\\w_3\\\\\end{bmatrix}$
