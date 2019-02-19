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
  
  ![Vector Plot](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_02.png?raw=true)

<br><br>

#### 3. If $\vec{v} + \vec{w} = \begin{bmatrix}5\\\\1\\\\\end{bmatrix}$ and $\vec{v} - \vec{w} = \begin{bmatrix}1\\\\5\\\\\end{bmatrix}$, compute and draw $\vec{v}$ and $\vec{w}$.

  * _**Solution**_:
    * $\vec{v} = \begin{bmatrix}3\\\\3\\\\\end{bmatrix}$ and $\vec{w} = \begin{bmatrix}2\\\\-2\\\\\end{bmatrix}$.
    
    ![Vector_Plot](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_03.png?raw=true)

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
    
    ![1.1 7](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_07.png?raw=true)

<br><br>

#### 8. The parallelogram in Figure 1.1 has diagnoal $\vec{v} + \vec{w}$. What is its other diagonal? What is the sum of the two diagonals? Draw that vector sum.

  * _**Solution**_
    * The other diagonal is $\vec{v} - \vec{w}$.
    * $(\vec{v} + \vec{w}) + (\vec{v} - \vec{w}) = 2\vec{v} = \begin{bmatrix}8\\\\2\end{bmatrix}$
    
    * Graph
    
    ![1-1 8](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_08.png?raw=true)

<br><br>

#### 9. If three corners of a parallelogram are $(1, 1)$, $(4, 2)$, and $(1, 3)$, what are all three of the possible fourth corners? Draw two of them.

  * _**Solution**_
    * The three possible points for the fourth corner are: $(-2, 2),\ (4, 0),\ (4, 4)$.

<br><br>

#### 10. Which point of the cube is $\vec{i} + \vec{j}$? Which point is the vector sum of $\vec{i} = (1,\ 0,\ 0)$ and $\vec{j} = (0,\ 1,\ 0)$ and $\vec{k} = (0,\ 0,\ 1)$? Describe all points $(x,\ y,\ z)$ in the cube.

  * _**Solution**_
    * $\vec{i} + \vec{j} = (1,\ 1,\ 0) \to $ This is the bottom right corner that is "closer to us."
    * $\vec{j} + \vec{k} = (0,\ 1,\ 1) \to $ This is the top right corner that is "farther away from us."
    * All points in the cube $(x,\ y,\ z)$ are the linear combinations of vectors $\vec{i}$, $\vec{j}$, and $\vec{k}$.
    
<br><br>

#### 11. Four corners of the cube are $(0,\ 0,\ 0)$, $(1,\ 0,\ 0)$, $(0,\ 1,\ 0)$, and $(0,\ 0,\ 1)$. What are the other four corners? Find the coordinates of the center point of the cube. The center points of the six faces are *____*.

  * _**Solution**_:
    * The other four points of the cube are $(1,\ 1,\ 0)$, $(1,\ 0,\ 1)$, $(0,\ 1,\ 1)$, and $(1,\ 1,\ 1)$.
      * $\begin{cases}\vec{i} + \vec{j}\\\\\vec{i} + \vec{k}\\\\\vec{j} + \vec{k}\\\\\vec{i} + \vec{j} + \vec{k}\end{cases}$
    * The coordinates of the center point of the cube is $(\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2})$.
      * $\frac{1}{2}\vec{i} + \frac{1}{2}\vec{j} + \frac{1}{2}\vec{k}$
    * The center points of the six faces are $(1,\ \frac{1}{2},\ \frac{1}{2})$, $(\frac{1}{2},\ \frac{1}{2},\ 0)$, $(0,\ \frac{1}{2},\ \frac{1}{2})$, $(\frac{1}{2},\ \frac{1}{2},\ 1)$, $(\frac{1}{2},\ 0,\ \frac{1}{2})$, $(\frac{1}{2},\ 1,\ \frac{1}{2})$.
    
<br><br>

#### 12. How many corners does a cube have in 4 dimensions? How many 3D faces? How many edges? A typical corner is $(0,\ 0,\ 0,\ 0)$. A typical edge goes to $(0,\ 1,\ 0,\ 0)$.

  * _**Solution**_:
    * This isn't really a linear algebra problem, but more of a combinatorics problem. Anyway,
      * 16 corners, 8 cells, and 24 edges.
      
<br><br>

#### 13.

  #### (a) What is the sum $V$ of the twelve vectors that go from the center of a clock to the hours 1:00, 2:00, ... , 12:00?
  #### (b) If the 2:00 vector is removed, why do the 11 remaining vectors add to 8:00?
  #### (c) What are the components of that 2:00 vector $\vec{v} = (\cos{\theta},\ \sin{\theta})$?
  
  * _**Solution**_:
    * (a) The sum of the vectors is the zero vector $\mathbf{0}$. The reason si because they all cancel each other out with their opposite vectors.
    * (b) The opposite vector of 2:00 is 8:00. If we remove 2:00, then there is nothing to cancel out the 8:00 vector. Therefore, we only have the 8:00 left after summing all the 11 vectors.
    * (c) On a clock, the angle between 2:00 and 3:00 is approximately $30^\text{o}$ (or $\frac{\pi}{6}$. The components of the vector pointing to 2:00 are $\sin({\frac{\pi}{6}) = \frac{1}{2}, \cos({\frac{\pi}{6}}) = \frac{\sqrt{3}}{2}}$.
      * $\vec{v} = \begin{bmatrix}\frac{\sqrt{3}}{2}\\\\\frac{1}{2}\end{bmatrix}$

<br><br>

#### 14. Suppose the twelve vectors start from 6:00 at the bottom instead of $(0,\ 0)$ at the center. The vector to 12:00 is doubled to $(0,\ 2)$. Add the new twelve vectors.

  * _**Solution**_
    * Just move all arrows down, but stretch the upmost-pointing vector (i.e. 12:00 vector) twice as long (so that its tip is unchanged).
  
<br><br>

#### 15. Figure 1.5a shows $\frac{1}{2}\vec{v} + \frac{1}{2}\vec{w}$. Mark the points $\frac{3}{4}\vec{v} + \frac{1}{4}\vec{w}$ and $\frac{1}{4}\vec{v} + \frac{1}{4}\vec{w}$.

  * _**Solution**_
    
    ![1-1-15](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_15.png?raw=true)
    
<br><br>

#### 16. Mark the point $-\vec{v} + 2\vec{w}$ and any other combination $c\vec{v} + d\vec{w}$ with $c + d = 1$. Draw the line of all combinations that have $c + d = 1$.

  * _**Solution**_
        
    ![-1-1-16](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_16.png?raw=true)
    
<br><br>

#### 17. Locate $\frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$ and $\frac{2}{3}\vec{v} + \frac{2}{3}\vec{w}$. The combinations of $c\vec{v} + c\vec{w}$ fill out what line?

  * _**Solution**_
        
    ![1-1-17](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_17.png?raw=true)
    
<br><br>

#### 18. Restricted by $0 \le c \le 1$ and $0 \le d \le 1$, shade in all combinations $c\vec{v} + d\vec{w}$.

  * _**Solution**_
    * The parallelogram shaded in dark blue is the area that represents all combinations of $c\vec{v} + d\vec{w}$ under the given restrictions.
      * Vector $\vec{v}$ is the case where $c = 1$ and $d = 0$, and the opposite case applies for $\vec{w}$. The upper right corner of the parallelogram is the case where $c = 1$ and $d = 1$. Everything else falls in inside this region.
      
    ![1-1-18](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_18.png?raw=true)
    
<br><br>

#### 19. Restricted by only $c \ge 0$ and $d \ge 0$ draw the "cone" of all combinations of $c\vec{v} + d\vec{w}$.

  * _**Solution**_
    * The graph is restricted, but the green area extends until infinity. Hence, a "cone."
    
    ![1-1-19](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_19.png?raw=true)
    
<br><br>
    
#### 20. Locate $\frac{1}{3}\vec{u} + \frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$ and $\frac{1}{2}\vec{u} + \frac{1}{2}\vec{w}$ in Figure 1.5b. Challenge problem: Under what restrictions on $c$, $d$, $e$, will the combinations $c\vec{u} + d\vec{v} + e\vec{w}$ fill in the dashed triangle? To stay in the triangle, one requirement is $c \ge 0$, $d \ge 0$, $e \ge 0$.

  * _**Solution**_
    * This is basically an extension of the previous problems 15-19. Again, it helps to think of vectors as points rather than arrows.
    * One minor difference is that for this problem, we'll use the _**head-to-tail method**_.
      * This is simple and I like to think of it as "half the parallelogram method." Recall how when we used the parallelogram method, we're drawing the same vectors on the opposite sides, and we're adding the two.
      * If you think about it, you can just abuse the fact that (from the physics perspective) you can move a vector in any direction as long as the magnitude (length) and directions are the same.
    * To first find $\frac{1}{3}\vec{u} + \frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$, we start from the origin and sequentially add one-thirds of each vector.
      * It's important to stay parallel with the vectors we're adding, in accordance to the parallelogram method.
      * Starting from $\frac{1}{3}\vec{u}$, we keep building on top of the previous vector and adding it.
    * The same rule applies to $\frac{1}{2}\vec{u} + \frac{1}{2}\vec{w}$.
    
    * **Challenge Problem**
      * This may seem a bit tricky, but again it's just an extension of earlier problems. Take a look at figure 1.5a. It's a triangle and our starting point is the origin, right? This $\Bbb{R}^3$ version is the exact same, except our points are not $\{\mathbf{0},\ \vec{v},\ \vec{w}\}$. Our points are now $\{\vec{w},\ \vec{u} - \vec{W},\ \vec{v} - \vec{w}\}$. Take note that the three points can be anything, it just depends on what vector your foucsing on (in this case I focused on $\vec{w}$).
      * All the combinations of the vectors can be expressed as $\vec{w} + \alpha(\vec{u} - \vec{w}) + \beta(\vec{v} - \vec{w})$.
        * Here, there are some restrictions: $\alpha + \beta \le 1$ (look at #16 if this is unclear).
      * And now the two equations must equal: $c\vec{u} + d\vec{v} + e\vec{w} = \vec{w} + \alpha(\vec{u} - \vec{w}) + \beta(\vec{v} - \vec{w})$.
      * If we clear up the two equations, we come up with the following:
        * $c\vec{u} + d\vec{v} + e\vec{w} = \alpha\vec{u} + \beta\vec{v} + (1 - \alpha - \beta)\vec{w}$
        * $\begin{cases}\alpha = c\\\\\beta = d\\\\(1 - \alpha - \beta) = e\end{cases}$
        * We arrive at the following answer: $c + d + e = 1\ \text{and}\ c \ge 0, d \ge 0, e \ge 0$
      
    ![1-1-20](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_20.png?raw=true)
    
<br><br>

#### 21. The three sides of the dashed triangle $\vec{v} - \vec{w}$ and $\vec{w} - \vec{v}$ and $\vec{u} - \vec{w}$. Their sum is $_____$. Draw the the head-to-tail addition around a plane triangle of $(3,\ 1)$ plus $(-1,\ 1)$ plus $(-2,\ -2)$.

  * _**Solution**_
    * $_____$ : $(\vec{v} - \vec{u}) + (\vec{w} - \vec{v}) + (\vec{u} - \vec{w}) = 0$
    * The triangle is as follows:

![1-1-21](https://github.com/seankala/ml_study_group/blob/master/Images/Math/ch1_1-1_21.png?raw=true)

<br><br>

#### 22. Shade in the pyramid of combinations $c\vec{u} + d\vec{v} + e\vec{w}$ with $c \ge 0$, $d \ge 0$, $e \ge 0$ and $c + d + 1 \le 1$. Mark the vector $\frac{1}{2}(\vec{u} + \vec{v} + \vec{w})$ as inside or outside this pyramid.

  * _**Solution**_
    * The shaded pyramid (or more precisely the tetrahedron or triangular pyramid) is the tetrahedron whose four points are the origin, $\vec{u}$, $\vec{v}$, and $\vec{w}$.
    * The vector $\frac{1}{2}(\vec{u} + \vec{v} + \vec{w})$ lies outside the pyramid. This is easily verifiable using the parallelogram adding method (if this is unclear, please reference #20).
    
<br><br>

#### 23. If you look at _all_ combinations of those $\vec{u}$, $\vec{v}$, and $\vec{w}$, is there any vector that can't be produced from $c\vec{u} + d\vec{v} + e\vec{w}$? Different answer if $_____$.

  * _**Solution**_
    * No, there is no vector that cannot be produced from the combination $d\vec{u} + d\vec{v} + e\vec{w}$ (assuming the same restraints from #22 hold).
    * $_____$ : "they are all in the same plane"
      * Building on top of the intuition of linear combinations and linear (in)dependence, if the three vectors all lie in the same plane it means that one is a multiple of another. This restricts the vectors that we can draw to 2D, which means that we cannot fill out the 3D tetrahedron.
      
<br><br>

#### 24. Which vectors are combinations of $\vec{u}$ and $\vec{v}$ and _also_ combinations of $\vec{v}$ and $\vec{w}$?

  * _**Solution**_
    * Vectors that are combinations of both $c\vec{u} + d\vec{v}$ and $d\vec{v} + e\vec{w}$ are simply vectors in $d\vec{v}$.
      * You can either just look at the two equations and see what they have in common (i.e. $d\vec{v}$), or you can visualize it geometrically.
        * Each equation "draws" on side of the tetrahedron. The common vectors of two sides would be the line that is connecting them. Hence, the linear combinations of a single vector.
        
<br><br>

#### 25. Draw vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ so that their combinations $c\vec{u} + d\vec{v} + e\vec{w}$ fill only a line. Find vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ so that their combinations $c\vec{u} + d\vec{v} + e\vec{w}$ fill only a plane.

  * _**Solution**_
    * If we want all of the combination of the three vectors to only fill a line, we must make sure that they are all the same.
      * You could also say that one vector could be the inverse of the other (e.g. $\vec{u} = $-\vec{v}$), but that wouldn't apply to this situation since we have the constrains of the coefficients to be nonnegative.
    * For the combinations of the three vectors to fill a plane, we just need to assure that one vector is the linear combination of the other two.
    
<br><br>

#### 28. Find vectors $\vec{v}$ and $\vec{w}$ so that $\vec{v} + \vec{w} = (4,\ 5,\ 6)$ and $\vec{v} - \vec{w} = (2,\ 5,\ 8)$. This is a question with *_____* unknown numbers, and an equal number of equations to find those numbers.

  * _**Solution**_
    * *_____* : 6 unknown numbers
      * $\vec{v} = \begin{bmatrix}v_1\\\\v_2\\\\v_3\\\\\end{bmatrix}\ \text{and}\ \vec{w} = \begin{bmatrix}w_1\\\\w_2\\\\w_3\\\\\end{bmatrix}$
        * $\begin{cases}v_1 + w_1 = 4\\\\v_2 + w_2 = 5\\\\v_3 + w_3 = 6\\\\v_1 - w_1 = 2\\\\v_2 - w_2 = 5\\\\v_3 - w_3 = 8\\\\\end{cases}$
    * $\vec{v} = \begin{bmatrix}3\\\\5\\\\7\\\\\end{bmatrix}\ \text{and}\ \vec{w} = \begin{bmatrix}1\\\\0\\\\-1\\\\\end{bmatrix}$
