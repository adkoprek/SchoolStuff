# Dynamical Equilibrium

## Introduction

### Problem

Two identical cylindrical containers with a cross-sectional area of $A$ are filled with $w_1$ and $w_2$ amounts of water. Two cylindrical tubes with cross-sectional areas $l$ and $m$ are then inserted into the containers until they touch the ground and are sealed. The water they contain is poured into the other container, and this process is repeated.

The functions $V_1(t)$ and $V_2(t)$ describe the volume of water in each container as a function of time. This leads to the equivalent functions $h_1(t) = \frac{V_1(t)}{A}$ and $h_2(t) = \frac{V_2(t)}{A}$, which represent the heights of the water in each container as functions of time.

### Quantification

This information leads to the following first-order differential equation:

$$
\frac{dV_1}{dt} = m \cdot h_2 - l \cdot h_1 = \frac{1}{A}(mV_2 - lV_1)
$$

$$
\frac{dV_2}{dt} = l \cdot h_1 - m \cdot h_2 = \frac{1}{A}(lV_1 - mV_2)
$$

With this information, we can construct the following vector $u(t) = (V_1(t), V_2(t))^T$, leading to the linear system:

$$
\frac{du}{dt} = \frac{1}{A}
\begin{pmatrix}
-l & m \\
l & -m
\end{pmatrix}
u
$$

The solution to this ODE has the general form:

$$
u(t) = c_1 e^{\lambda_1 t} x_1 + c_2 e^{\lambda_2 t} x_2,
$$

where $\lambda_i$ are the eigenvalues, $x_i$ are the eigenvectors, and $c_i$ are constants determined by initial conditions.

---

## Eigenvalues and Eigenvectors

### Eigenvalues

We compute the eigenvalues from the determinant:

$$
\begin{vmatrix}
-l - \lambda & m \\
l & -m - \lambda
\end{vmatrix}
= (-l - \lambda)(-m - \lambda) - lm
$$

$$
lm + m\lambda + l\lambda + \lambda^2 - lm = \lambda^2 + (m + l)\lambda = \lambda(\lambda + (m + l))
$$

Solving for the roots gives the eigenvalues $\lambda_{1,2} = \{ 0, -(m + l) \}$.  
Including the factor $\frac{1}{A}$ from the original matrix, we get:

$$
\lambda_{1,2} = \left\{ 0, -\frac{m + l}{A} \right\}
$$

### Eigenvectors

For $\lambda = 0$:

$$
\frac{1}{A}
\begin{pmatrix}
-l & m \\
l & -m
\end{pmatrix}
\begin{pmatrix} v_{11} \\ v_{12} \end{pmatrix} = 0
$$

Thus, the eigenvector is $v_1 = (m, l)^T$.

For $\lambda = -\frac{m + l}{A}$:

$$
\frac{1}{A}
\begin{pmatrix}
m & m \\
l & l
\end{pmatrix}
\begin{pmatrix} v_{21} \\ v_{22} \end{pmatrix} = 0
$$

The corresponding eigenvector is $v_2 = (1, -1)^T$.

---

## Solution

### Outline

We can now construct the general solution:

$$
u(t) = c_1 e^{\lambda_1 t} v_1 + c_2 e^{\lambda_2 t} v_2
$$

Substituting the computed eigenvalues and eigenvectors:

$$
u(t) = c_1
\begin{pmatrix}
m \\ l
\end{pmatrix}
+ c_2 e^{-\frac{(m + l)t}{A}}
\begin{pmatrix}
1 \\ -1
\end{pmatrix}
$$

### Boundary Conditions

The parameters $c_1$ and $c_2$ must satisfy the initial conditions $V_1(0) = w_1$ and $V_2(0) = w_2$:

$$
\begin{cases}
c_1 m + c_2 = w_1 \\
c_1 l - c_2 = w_2
\end{cases}
$$

Adding the two equations gives:

$$
c_1 (m + l) = w_1 + w_2 \quad \Rightarrow \quad c_1 = \frac{w_1 + w_2}{m + l}
$$

Solving for $c_2$:

$$
c_2 = w_1 - c_1 m = w_1 - \frac{m(w_1 + w_2)}{m + l} = \frac{l w_1 - m w_2}{m + l}
$$

---

### Complete Solution

$$
u(t) =
\frac{w_1 + w_2}{m + l}
\begin{pmatrix} m \\ l \end{pmatrix}
+
\frac{l w_1 - m w_2}{m + l}
e^{-\frac{(m + l)t}{A}}
\begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

This is the final closed-form solution, where the first component of $u(t)$ corresponds to $V_1(t)$ and the second to $V_2(t)$.

---

## Example

### Variables

Assume one container is filled with 60 units of liquid and the other with 40 units.  
The cross-sectional area is $A = \pi 10^2$.  
We also set $m = \pi$ and $l = \pi 2^2$.

### Code

```python
import numpy as np
import matplotlib.pyplot as plt

m = np.pi
l = np.pi * 2 ** 2
A = np.pi * 10 ** 2
w1 = 60
w2 = 40

x = np.linspace(0, 100, 1000)
v1 = (w1 + w2)/(m + l) * m + (l * w1 - m * w2)/(m + l) * np.exp(-(m + l)/A * x)
v2 = (w1 + w2)/(m + l) * l - (l * w1 - m * w2)/(m + l) * np.exp(-(m + l)/A * x)

plt.plot(x, v1, label='V1')
plt.plot(x, v2, label='V2')
plt.legend()
plt.xlabel('time')
plt.ylabel('volume')
plt.show()
```

### Plot

![](/home/adkoprek/.var/app/com.github.marktext.marktext/config/marktext/images/2025-10-18-11-20-16-Screenshot%20From%202025-10-18%2010-58-58.png)

### Conclusion

The plot shows that the initial conditions at $t = 0$ are satisfied and that mass conservation is maintained, since the total water volume remains $w_1 + w_2$ at all times.

## Interpretation

### Asymptotics

The eigenvalues are $0$ and negative, since $m$ and $l$ are both positive.  
As $t \to \infty$, the exponential term vanishes, and the system reaches equilibrium:

$$
V_1 \to c_1 m = \frac{m(w_1 + w_2)}{m + l}
$$

$$
V_2 \to c_1 l = \frac{l(w_1 + w_2)}{m + l}
$$

### End-State Ratio

Knowing the asymptotic behavior, we can determine the ratio of the final states:

$$
\frac{m(w_1 + w_2)}{m + l} = k \frac{l(w_1 + w_2)}{m + l}
$$

$$
m(w_1 + w_2) = k l (w_1 + w_2) \quad \Rightarrow \quad k = \frac{m}{l}
$$

Thus, as $t \to \infty$:

$$
V_1 = \frac{m}{l} V_2
$$

$$
V_1 \cdot l = V_2 \cdot m
$$

### Chemical Interpretation

We can normalize the above formula by dividing by the total volume $V = V_1 + V_2$:

$$
\frac{V_1}{V} \cdot l = \frac{V_2}{V} \cdot m
$$

Here, $\frac{V_1}{V}$ is the concentration of the liquid from the first container (denoted $f_1$), and similarly, $\frac{V_2}{V} = f_2$.  
This leads to:

$$
f_1 \cdot l = f_2 \cdot m
$$

This satisfies the condition for **chemical dynamic equilibrium**, assuming $f_1$ and $f_2$ represent concentrations of two reacting substances and $l$, $m$ are their respective reaction rates.
