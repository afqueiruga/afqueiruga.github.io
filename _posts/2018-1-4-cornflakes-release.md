---
layout: post
title: "Source Release of Cornflakes/Popcorn"
date: 2018-1-4
categories: codes
---

# Intro

I have released the source code of my new scientific packages, cornflakes
and popcorn. They are located on my Bitbucket repositories at

- [https://bitbucket.org/afqueiruga/cornflakes](https://bitbucket.org/afqueiruga/cornflakes)
- [https://bitbucket.org/afqueiruga/popcorn](https://bitbucket.org/afqueiruga/popcorn)

This package has been under development for the last two years as I've
developed a variety of numerical codes.
It is finally at the point where I am comfortable putting it out in the wild.
It is still not quite ready for actual usage by people other than myself,
but it is suitable as a case study in scientific package architecture.

The names are puns on "kernel": Cornflakes is the serial assembly of kernels. Popcorn transforms compact kernel specifications in large and fluffy C code implementations. Husks are filled with kernels. (Cornflakes will run in parallel though, but I still liked the pun.)

# Example

[See the example notebook in the repository, /examples/spring_example.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/afqueiruga/cornflakes/raw/5aa3b33210a61951d923846e2747c52076471f33/examples/spring_example.ipynb)

# Usages

Cornflakes the main library for a number of different of codes I write at LBNL.
The following publications and conference presentations are a small
selection. The poster has a good
description of the algorithm that was possible using cornflakes.

- [Queiruga, A. F. and G. J. Moridis, “NG21A-1806: Numerical 
  Simulation of Hydraulic Fracture Propagation using 
  Fully-Coupled Peridynamics, Thin-Film Flow, and Darcian Flow”, 
  AGU Fall Meeting, San Francisco, CA, December 2016. (poster linked)](/assets/source-release-cornflakes/afq_poster_AGU2016.pdf)
- Queiruga, A. F. and G. J. Moridis, "Numerical experiments on 
  the convergence properties of state-based peridynamic laws and 
  influence functions in two-dimensional problems." Computer 
  Methods in Applied Mechanics and Engineering 322 (2017): 
  97-122.
- Moridis, G. J., A. F. Queiruga, and M. T. Reagan, “The T+H+M 
  Code for the Analysis of Coupled Flow, Thermal, Chemical and 
  Geomechanical Processes in Hydrate-Bearing Geologic Media,” 9th 
  International Gas Hydrates Conference, Denver, CO, June, 2016.


Consider the follow diagram of the simulation for hydraulic fracture extension described in the above poster:  
![diagram](/assets/source-release-cornflakes/3waydiagram.png){: .center-image }  
It involves three different types of discretizations for three different sets of physics:

1. a Peridynamics grid for mechanics and fracture,
2. a 2D Finite Element mesh for porous flow, and
3. a 1D Finite Element mesh for fracture transport that's dynamically remeshed

that are fully coupled.
A visualization of the simulation is included in the research gallery on this slide, and
the poster linked above describes the algorithm.
How does one even program this? Well, it took me less than a year because in that type,
I wrote my own langauge and runtime to express it with!
Using cornflakes, that model overview can be decomposed into the following (hand drawn) kernels:
![six kernels](/assets/source-release-cornflakes/kernels.png){: .center-image }

There are three classes of hypervertexes in this problem

- Peridynamics points, $P$
- Peridynamics bonds, $B$
- Background mesh nodes, $Q$

The schematic illustrates the physical meaning of the edge, and the bottom list shows the
ordering of the hypervertices inside the hyperedge that corresponds to one kernel call.
From left to right, top to bottom, these are

- For state-based peridynamics: A point with vertex id $P_0$ surrounded by points with ids $P_1$ to $P_n$,
connected with bonds
who themselves have vertex ids $B_1$ to $B_n$;
- For Darcy flow with FEM: A simple four-node quad whose nodes are vertices $Q_0$ to $Q_3$;
- For fracture-matrix leakage connected a four node quad with a line segment: The four-node quad ($Q_0$ to $Q_3$) PLUS
a two-node line, $B_0$ and $B_1$;
- A single bond $B_0$ between points $P_0$ and $P_1$;
- A line segment FEM connecting the bonds $B_0$ and $B_1$, which is directly coupled to the four peridynamics points
defining the bond; and
- A quad with a set of points inside of it.

The vertex ids are just integers, with $P$, $B$, and $Q$ just denoting different ranges. E.g., if there are 100
peridynamics points, 800 bonds, and 40 fem nodes, the last vertex has the id 939. The ranges would be 0-99 for $P$,
$100-899$ for $B$, and 900-939 for $Q$. The labels mean absolutely nothing to cornflakes, but we use these types
of schematics to figure out what the $DofSpaces$ and $DofMaps$ need to look like to fetch the data we need for
each kernel. Note that the first and last kernel are variable length! The edges of a hypergraph don't require the
same length, and popcorn kernels can take in variable length arguments, given an `l_edge` parameter, and the
DSL can express Loops over symbolic ranges.


# Stylistic Choices

I chose Python/C because it was, and still is, the state of the art when I
started writing.
At the time I began, I felt that [Julia](https://julialang.org) wasn't quite ready.
Originally, I wanted cornflakes to have a pure C API that didn't require Python
to make it easy to link to preexisting code.
Julia requires the runtime and doesn't support outputting linkable objects,
but I have abandoned that decision and am okay with that now. 
The latest version of TOUGH+ has an embedded Python interpretter that
executes the Python/C-based mechanics library 

Julia doesn't have its own symbolic library, and the Python interface was wonky when
I experimented with it.

A few other things I would do differently:
1. I wanted a pure C API at first, [but this gets out of hand quickly.](https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule)
Just embed a higher level language when you need to interact with legacy codes.
It's easier than expressing complicated simulations in pure C or Fortran.
2. I used SWIG as the Python/C binding since it's worked well enough for me
in the past.
I probably won't use it again.
This has caused tons of headaches with allocation tracking and memory leaks.
I even had to make direct calls to the Python API. 
3. If you look carefully at the C source, you'll notice that I hand-coded my own
polymorphic object system.
Don't do this! This is bad practice! I'm a crazy person!
I just hate the C++ class system.
(My latest C++ code has a hacked vtable, too, for virtual template methods.)

# Future

The hypergraph partitioning algorithm has been implemented and tested in
another development code using PETSc, but hasn't made its way into cornflakes
yet. I am still debating on major syltistic changes before parallelizing cornflakes.

I'll probably be rewriting it all in Julia.
