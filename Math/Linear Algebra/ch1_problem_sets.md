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
    * In the figure below, 
      * blue arrow $\rightarrow$ $\vec{v}$
      * red arrow $\rightarrow$ $\vec{w}$
      * magenta dot $\rightarrow$ $u$
      * cyan dot $\rightarrow$ $\frac{3}{4}\vec{v} + \frac{1}{4}\vec{w}$
      * green dot $\rightarrow$ $\frac{1}{4}\vec{v} + \frac{1}{4}\vec{w}$
      * yellow dot $\rightarrow$ $\vec{v} + \vec{w}$
        * Each blue dotted line represents the reflection of the portion of vector $\vec{v}$, and each red dotted line represents the reflection of the portion of vector $\vec{w}$.
          * These are used to find the points using the parallelogram method.
    
    ![1-1-15](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_15.png?raw=true)
    
<br><br>

#### 16. Mark the point $-\vec{v} + 2\vec{w}$ and any other combination $c\vec{v} + d\vec{w}$ with $c + d = 1$. Draw the line of all combinations that have $c + d = 1$.

  * _**Solution**_
    * In the figure below,
      * blue arrow $\rightarrow$ $-\vec{v}$
        * We just flipped the original vector $\vec{v}$ across the origin.
      * red arrow $\rightarrow$ $2\vec{w}$
      * green dot $\rightarrow$ $-\vec{v} + 2\vec{w}$
      * magenta dot $\rightarrow$ $\frac{1}{2}\vec{v} + \frac{1}{2}\vec{w}$
      * two black arrows $\rightarrow$ original $\vec{v}$ and $\vec{w}$
      * black dotted line $\rightarrow$ line that passes through all combinations of $c + d = 1$
        * The equation of this line can't be determined, but if we assume that $\vec{v} = (3,\ 1)$ and $\vec{w} = (1,\ 3)$ then the equation would be $y = -x + 4$.
        
    ![-1-1-16](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_16.png?raw=true)
    
<br><br>

#### 17. Locate $\frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$ and $\frac{2}{3}\vec{v} + \frac{2}{3}\vec{w}$. The combinations of $c\vec{v} + c\vec{w}$ fill out what line?

  * _**Solution**_
    * In the figure below,
      * blue arrow $\rightarrow$ $\vec{v}$
      * red arrow $\rightarrow$ $\vec{w}$
      * green dot $\rightarrow$ $\frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$
      * magenta dot $\rightarrow$ $\frac{2}{3}\vec{v} + \frac{2}{3}\vec{w}$
      * black dotted line is the line that $c\vec{v} + c\vec{w}$ fill out
        * The equation for this line is $y = x$.
        
    ![1-1-17](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_17.png?raw=true)
    
<br><br>

#### 18. Restricted by $0 \le c \le 1$ and $0 \le d \le 1$, shade in all combinations $c\vec{v} + d\vec{w}$.

  * _**Solution**_
    * In the figure below,
      * blue arrow $\rightarrow$ $\vec{v}$
      * red arrow $\rightarrow$ $\vec{w}$
    * The parallelogram shaded in dark blue is the area that represents all combinations of $c\vec{v} + d\vec{w}$ under the given restrictions.
      * Vector $\vec{v}$ is the case where $c = 1$ and $d = 0$, and the opposite case applies for $\vec{w}$. The upper right corner of the parallelogram is the case where $c = 1$ and $d = 1$. Everything else falls in inside this region.
      
    ![1-1-18](https://github.com/seankala/ml_study_group/blob/master/Images/ch1_1-1_18.png?raw=true)

#### 28. Find vectors $\vec{v}$ and $\vec{w}$ so that $\vec{v} + \vec{w} = (4,\ 5,\ 6)$ and $\vec{v} - \vec{w} = (2,\ 5,\ 8)$. This is a question with *_____* unknown numbers, and an equal number of equations to find those numbers.

  * _**Solution**_
    * *_____* : 6 unknown numbers
      * $\vec{v} = \begin{bmatrix}v_1\\\\v_2\\\\v_3\\\\\end{bmatrix}\ \text{and}\ \vec{w} = \begin{bmatrix}w_1\\\\w_2\\\\w_3\\\\\end{bmatrix}$
        * $\begin{cases}v_1 + w_1 = 4\\\\v_2 + w_2 = 5\\\\v_3 + w_3 = 6\\\\v_1 - w_1 = 2\\\\v_2 - w_2 = 5\\\\v_3 - w_3 = 8\\\\\end{cases}$
    * $\vec{v} = \begin{bmatrix}3\\\\5\\\\7\\\\\end{bmatrix}\ \text{and}\ \vec{w} = \begin{bmatrix}1\\\\0\\\\-1\\\\\end{bmatrix}$
