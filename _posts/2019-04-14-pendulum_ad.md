---
layout: post
title: "Solving the Pendulum via Automatic Differentiation"
date: 2019-4-15
categories: programming
--- 
# Solving Physics with Automatic Differentiation

Do we need to derive equations by hand? Can't our computer just solve it?

There are lots of ways to implement this kind of thought. We could employ
symbolic differentiation on our mathematical relations, and then generate code
from the symbolic expressions our algorithm needs. This is the strategy I used
for [Popcorn](https://github.com/afqueiruga/popcorn), where I really wanted to
operate in Vector algebra and calculus. [FEniCS](https://fenicsproject.org) is
another example of this type of system. But this gets slow, and the workflow is
complicated:

\begin{equation}
f(x)\rightarrow Tool \left[\rightarrow \frac{\partial f(x)}{\partial x}
\rightarrow expressions
\rightarrow generate\,code \rightarrow compile \, and \, link\right]\rightarrow
module \rightarrow user\,program
\end{equation}

This gives us a three-language problem: the symbolic language used to express
and manipulate the equation (Popcorn/SymPy, UFL, or TensorFlow), the low-level
code that implements it efficiently (C/C++/CUDA), and the high-level code that
embeds the langauge and orchestrates the workflow (Python). The user might not
care what's inside the blackbox, but I as the developer care. The user will care
if the system is faster and easier to use.

If the user can type in some implementation of an equation, we can generate what
we need directly from the program, if we have a sufficiently advanced and
flexible programming language. That's why this is a Julia notebook.

I'm using [Zygote](https://github.com/FluxML/Zygote.jl) to do differentiation on
Julia code. 

**In [1]:**

```python
using Zygote
using LinearAlgebra
using Plots
```
 
The simplest example I can think of is the pendulum with a spring penalty on its
length. Let us use vector points $x=[x_1,x_2]$ and $v=[v_1,v_2]$ such that its
Lagrangian is:
\begin{equation}
L = \frac{m}{2} v^2 + \frac{k}{2}\left( \sqrt{x^2}- L\right)^2 - mgx_2
\end{equation}
which we can write as a one-liner function: 

**In [53]:**

```python
m = 1
k = 20
g = 9.81
L(x,v) = 1/2*m*dot(v,v)-1/2*k*(sqrt(dot(x,x))-1.0)^2 - m*g*x[2]
```




    L (generic function with 1 method)


 
That's all the "physicist" needs to specify, directly in Julia.
To get the eqations of motion, physics students are taught the basic equation of
Lagrangian mechanics:
\begin{equation}
\frac{\mathrm{d}}{\mathrm{d}t} \frac{\partial L}{\partial v} = \frac{\partial
L}{\partial x}
\end{equation}
We can directly build the tools we need from the one-line computer program
above: 

**In [60]:**

```python
dLdx(x,v) = Zygote.forward_jacobian(xd->L(xd,v),x)[2];
dLdv(x,v) = Zygote.forward_jacobian(vd->L(x,vd),v)[2];
```
 
We're using the `forward_jacobian` method because vector values cause problems
to the more advanced algorithms that are works-in-progress in Zygote. We can
check to see that the gradient with respect to $x$ extracts out the force due to
gravity when the spring is relaxed: 

**In [61]:**

```python
dLdx([1.0,0.0],[0.0,0.0])
```




    2×1 Array{Float64,2}:
     -0.0 
     -9.81


 
We can now implement a trapezoidal Runge-Kutta integrator (for energy-
conservative A-stability) to discretize the time derivative as an implicit
equation in $x$ and $v$: 

**In [102]:**

```python
aii = 0.5;
Δt = 0.1;
lhs(x,v) = dLdv(x,v) - Δt*aii * dLdx(x,v);
rhs(x,v) = dLdv(x,v) + Δt*(1.0-aii) * dLdx(x,v);
```
 
We will solve the equation
\begin{equation}
lhs(x_i,v_i) = rhs(x_0,v_0).
\end{equation}
Then, we take the pieces we need to solve the equation using Newton's method. We
need two K's on each argument because we're solving a second-order ODE by
substituting $dx/dt=v$ into the system of equations. 

**In [103]:**

```python
fwd_Kx(x,v) = Zygote.forward_jacobian((xd)->lhs(xd,v),x)[2];
fwd_Kv(x,v) = Zygote.forward_jacobian((vd)->lhs(x,vd),v)[2];
fwd_K_tot(x,v) = fwd_Kv(x,v) + Δt * aii * fwd_Kx(x,v);
```
 
We can check to make sure this gives us an expected result too, a 2-by-2 matrix
equal to
\begin{equation}
(m=1)\mathbf{I} + (\Delta t \, a_{ii} = 0.05)^2 (k=20) e_2 \otimes e_2
\end{equation} 

**In [106]:**

```python
fwd_K_tot([0.0,1.0],[0.,0.])
```




    2×2 Array{Float64,2}:
     1.0  0.0 
     0.0  1.05


 
# Looping in time 
 
Now we just do Newton's method for each timestep to integrate forwards in time: 

**In [104]:**

```python
x0 = [1.0,0.0];
v0 = [0.0,0.0];
series = []
for i = 1:100
    rhs0 = rhs(x0,v0)
    xi = x0
    vi = v0
    for k = 1:10
        R = rhs0-lhs(xi,vi)
        Kt = fwd_K_tot(xi,vi)
        Δv = Kt\R
        vi = vi + Δv
        xi = x0 + Δt*((1.0-aii)*v0 + aii*vi)
        #println(k,Δv,R,Kt);
        if dot(Δv,Δv)<1.0e-14 break end
    end
    push!(series,(xi,vi))
    v0 = vi
    x0 = xi
end
```
 
We can now plot the $x(t)$ and $y(t)$ curves to make sure they look right: 

**In [105]:**

```python
plot([s[1][1] for s in series],label='x')
plot!([s[1][2] for s in series],label='y')
```



 
![svg]({{ BASE_PATH }}/assets/pendulum_ad_files/pendulum_ad_18_0.svg) 


 
Note how we're solving the nonlinear pendulum. Let's also plot it in $y(x)$: 

**In [97]:**

```python
plot([s[1][1] for s in series],[s[1][2] for s in series],marker=:hexagon,label="")
```



 
![svg]({{ BASE_PATH }}/assets/pendulum_ad_files/pendulum_ad_20_0.svg) 


 
We started from just a one-liner expression of the lagrangian $L(x,v)$ in direct
Julia code, and used differentiation on the program itself. Not only did we let
the programming language do the heavy-lifting in deriving expressions, this is
also *waaayyy* faster than an equivalent pure-Python implementation since Julia
is a compiled language. (It's also way faster than a TensorFlow implementation;
speeding up some other TensorFlow projects is the motivation for this.) 
 
## Unfortunarly vector returns don't work.

The full capabilities of Zygote only handle scalar returns yet. I should dig
into this. 

**In [98]:**

```python
Kx(x,v) = Zygote.derivative((xd)->lhs(xd,v),x)
Kv(x,v) = Zygote.derivative((vd)->lhs(x,vd),v)
K_tot(x,v) = Kv(x,v) + Δt * Kx(x,v)
```




    K_tot (generic function with 1 method)



**In [None]:**

```python
K_tot([0.0,0.0],[0.0,0.0])
```


    KERNEL EXCEPTION

    UndefVarError: S not defined

    

    Stacktrace:

     [1] show(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Type{Zygote.Pullback{Tuple{Type{UnionAll},TypeVar,Type{Type{#s4<:Tuple}}},T} where T}) at /Users/afq/.julia/packages/Zygote/mlF4T/src/compiler/show.jl:12

     [2] show_datatype(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::DataType) at ./show.jl:526

     [3] show(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::DataType) at ./show.jl:436

     [4] print(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Type) at ./strings/io.jl:31

     [5] print(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::String, ::Type, ::Vararg{Any,N} where N) at ./strings/io.jl:42

     [6] (::getfield(Base, Symbol("##372#373")))(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}) at ./show.jl:1481

     [7] #with_output_color#671(::Bool, ::Function, ::Function, ::Symbol, ::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}) at ./util.jl:366

     [8] with_output_color(::Function, ::Symbol, ::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}) at ./util.jl:364

     [9] show_tuple_as_call(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Symbol, ::Type) at ./show.jl:1470

     [10] show_spec_linfo(::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Base.StackTraces.StackFrame) at ./stacktraces.jl:262

     [11] #show#9(::Bool, ::Function, ::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Base.StackTraces.StackFrame) at ./stacktraces.jl:272

     [12] #show at ./none:0 [inlined]

     [13] #show_trace_entry#641(::String, ::Function, ::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Base.StackTraces.StackFrame, ::Int64) at ./errorshow.jl:479

     [14] (::getfield(Base, Symbol("#kw##show_trace_entry")))(::NamedTuple{(:prefix,),Tuple{String}}, ::typeof(Base.show_trace_entry), ::IOContext{Base.GenericIOBuffer{Array{UInt8,1}}}, ::Base.StackTraces.StackFrame, ::Int64) at ./none:0

     [15] show_backtrace(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Array{Union{Ptr{Nothing}, InterpreterIP},1}) at ./errorshow.jl:582

     [16] show_bt(::Base.GenericIOBuffer{Array{UInt8,1}}, ::Symbol, ::Array{Union{Ptr{Nothing}, InterpreterIP},1}, ::UnitRange{Int64}) at /Users/afq/.julia/packages/IJulia/9ajf8/src/display.jl:136

     [17] #sprint#340(::Nothing, ::Int64, ::Function, ::Function, ::Symbol, ::Vararg{Any,N} where N) at ./strings/io.jl:101

     [18] sprint at ./strings/io.jl:97 [inlined]

     [19] #error_content#34(::Symbol, ::String, ::Function, ::UndefVarError, ::Array{Union{Ptr{Nothing}, InterpreterIP},1}) at /Users/afq/.julia/packages/IJulia/9ajf8/src/display.jl:147

     [20] error_content(::UndefVarError, ::Array{Union{Ptr{Nothing}, InterpreterIP},1}) at /Users/afq/.julia/packages/IJulia/9ajf8/src/display.jl:147

     [21] execute_request(::ZMQ.Socket, ::IJulia.Msg) at /Users/afq/.julia/packages/IJulia/9ajf8/src/execute_request.jl:138

     [22] #invokelatest#1 at ./essentials.jl:742 [inlined]

     [23] invokelatest at ./essentials.jl:741 [inlined]

     [24] eventloop(::ZMQ.Socket) at /Users/afq/.julia/packages/IJulia/9ajf8/src/eventloop.jl:8

     [25] (::getfield(IJulia, Symbol("##15#18")))() at ./task.jl:259

 
## References 
 
- https://github.com/afqueiruga/popcorn
- https://github.com/FluxML/Zygote.jl
- https://fluxml.ai/2019/02/07/what-is-differentiable-programming.html
- https://julialang.org/blog/2019/01/fluxdiffeq 

**In [None]:**

```python

```
