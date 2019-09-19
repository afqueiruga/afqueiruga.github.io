---
layout: page
title: Research
permalink: /research/
---

Sometimes I make cool videos in my research. This page is a small collection of the cooler ones
I've made for various research topics over the years. 

Warning: Each of the videos below is approximately 1MB.

# Equation of State Reparameterization with Unsupervised Phase Labeling

An autoencoder is used to learn a new representation of complex multiphase equations of state. Below is an animation of the training process on a dataset of water spanning solid, liquid, gas, and the supercritical regime, without phase labels. "Phases" are learned as features that select different curve fits. 

<center><video controls preload="none"
poster="images/phases.thumbnail.jpg" width="500">
<source src="https://www.ocf.berkeley.edu/~afq/media/phase_training.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>

The trained model is inserted directly into balance laws, building differential algebraic equations on the latent space that can be solved easily (with automatic differentiation.)

![integrating on autoencoders](images/autoencoder_balance_detailed.png)

# Hydraulic Fracture Extension

A peridynamics model is used to simulate the hydraulic fracturing process fully coupled to finite-element models of porous flow and fracture flow. The growth of the fracture is modeled by weakening and breaking bonds between peridynamic material points in response to the strain. Fluid injection drives the growth of the initial hydraulic fracture and interacting with a natural fracture to the left. Below the peridynamic points are plotted, colored by the y displacement, and the fields for matrix-pore pressure and fracture pressure on the left. The fracture is dynamically remeshed.

<center><video controls preload="none"
poster="images/natural_crack.thumbnail.png" width="700">
<source src="https://www.ocf.berkeley.edu/~afq/media/fracturing.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>

But remember, videos are not results! It turns out this method does not work. 
The video shows oscilations that form vertical stripes in the
point coloring, which motivated the study published in
["Numerical experiments on the convergence properties of state-based peridynamic laws and influence functions in two-dimensional problems"](http://www.sciencedirect.com/science/article/pii/S0045782516311598)
and [PeriFlakes](https://github.com/afqueiruga/PeriFlakes). 
A hyperparameter search on possible Peridynamics schemes failed to find a method that passed the most basic tests, despite producing plausible illustrations and videos.


# Microstructure Simulation of Electronic Textiles

A woven-beam finite element simulation with multiphysics contacts is
used to perform material property perdiction.

<center><video controls preload="none" poster="images/fibrils.thumbnail.jpg" width="700">
<source src="https://www.ocf.berkeley.edu/~afq/media/fibrils.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>


# Electronic Textiles in Ballistic Impacts

High strength textiles are a fundamental component of armors in multiple applications, where they are coupled with metal and ceramic plates and various other systems. In this research, the effect of applying electromagnetic fields to a ballistic fabric undergoing impact is explored, wherein an external magnetic field induces deformation in an electrified sheet to influence the behavior of the projectile.

<center><video controls preload="none"
poster="images/V_loose.thumbnail.jpg" width="500">
<source src="https://www.ocf.berkeley.edu/~afq/media/V_loose.small.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>


# Image Processing in Impact Experimentation

A silicone ballistic block was embedded with a grid using thread and ink. A baseball is fired at the block, and custom image processing software is used to track the grid. A better camera is needed to be able to follow all of the points.

<center><video controls preload="none"
poster="images/fast_block.thumbnail.jpg" width="500">
<source src="https://www.ocf.berkeley.edu/~afq/media/fast_block.small.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>



# DEM Simulations of a Granular Shear Cell

A discrete Element simulation is used to obtain local flow properties of a granular media inside of an anular shear cell. Particles are affixed to the inside wheel of the shear cell that rotates at a constant rate. Contacts between particles and between particles and the boundary resolved by a soft-sphere Hertzian spring-dashpot normal force and a history-based frictional force.


<center><video controls preload="none"
poster="images/gsc.thumbnail.jpg" width="500">
<source src="https://www.ocf.berkeley.edu/~afq/media/gsc.small.3.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></center>

