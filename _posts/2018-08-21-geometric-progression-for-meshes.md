---
layout: post
title: "The geometric progression for structured arc meshes"
date: 2018-08-21
categories: simulation
---

## The geometry

It seems simple, and like there should be a built-in feature.
I couldn't find any formula when I googled, so I derived it myself and post it
in hopes that whoever is reading it managed to find it.
Future me will probably consult this page.


We want the ratio between the first division and it's arc-length to be same as
the last division and it's arc-length.
The arc-lengths are $L_1=2\pi R_1 \theta$ and $L_2=2\pi R_2 \theta$, so their
ratio is the same is as the ratio between the radii.
We want to find a relationship between $h_1$ and $h_2$ that will yield the same
ratio. $h_1=a$ and $h_2=a r^N$


After forgetting everything I learned in middle school and looking it up on wikipedia, the formula for the total distance is

\begin{equation}
R_2-R_1 = a \frac{1-r^N}{1-r}
\end{equation}

GMSH will solve for the $a$ given an $N$. We need to provide the $r$ that
satisifies
\begin{equation}
\text{Find}\quad r \quad \text{s.t.} \quad \frac{a}{a r^{N-1} } = \frac{L_2}{L_1}
\end{equation}
which comes out to
\begin{equation}
r=\left( \frac{R_2}{R_1} \right)^{1/(N-1)}
\end{equation}

## gmsh Snippet

Here is the line where I use this in formula in a gmsh script:
```
// The radial edges
Transfinite Line {7, -8} = 18/Mesh.CharacteristicLengthFactor
    Using Progression (2.5/0.2)^(Mesh.CharacteristicLengthFactor/(17.0-1.0));
// The arc edges
Transfinite Line {1, 6} = 12/Mesh.CharacteristicLengthFactor Using Progression 1.0;
// Set the mode
Transfinite Surface {5} Alternate;
```
7 and 8 are the line segments with define the radially oriented sides, and
segments 1 and 6 are the arcs.
The arcs use a uniform progression, which means the meshed segments of 1 and 6
will have the different lengths discussed above. The section was defined to go
from $R_1=0.2$ to $R_2=2.5$. The base case has 17 elements along the radius and 12 elements around the arc.
The -8 is there to flip the line so that the progression goes in the same
direction as 7; this needs to be verified by looking at the GUI.

This code will also automatically scale the number of elements based on the size
 factor.
This is useful when scaling the mesh from the command line.
Here's the little snippet  where a python script generates a new mesh for a
convergence study:

```python
os.system("gmsh ../quarter_plane.geo -2 -clscale {0} -o ../gen_{0}.msh ".format(clscale))
os.system("dolfin-convert ../gen_{0}.msh ../gen_{0}.xml".format(clscale))
```

<!-- The mesh looks pretty, but that solution is wrong =[. -->
