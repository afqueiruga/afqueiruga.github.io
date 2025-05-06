---
layout: post
title: (Circa 2018) Design for Scientific Software
date: 2025-03-16
categories: workflow
---

> This is a transformation of a talk I gave some years ago while I was at LBNL.


1. Design
2. Engineering
3. Architecture

--

### Scientific software is particularly challenging.

### We don't know what we're trying to do when we start.

# Testing  (comes first)

Kanewala and Bieman, "Testing Scientific Software: A systematic literature review." Information and Software Technology, 2014.

> Testing challenges that occur due to cultural differences between scientists and the software engineering community.
> - Challenges due to a limited understanding of testing concepts such as viewing the code and the model it implements as inseperable entities.
> - Challenges due to limited understanding of testing processes resulting in the use of ad-hoc or unsystematic testing methods.
> -  Challenges due to not applying known testing methods such as unit testing.
> - Testing is done only with respect to the initial specific scientific problem addressed by the code. Therefore the reliability of results when applied to a different problem cannot be gaurunteed.
> - Management and budgetary support for testing may not be provided.
> - Software development is treated as a secondary activity resulting in a lack of recognition for the skills and knowledge required for software development.
> - The wide [use] of FORTRAN in the scientific community makes it difficult to utilize many testing tools from the software engineering community.

--

# Physics $\neq$ equations $\neq$ program $\neq$ code

--

## The primary goal of source code is to communicate to other programmers, not the computer.

--

## The tools we use and make help us express our problems.
### Sapir–Whorf hypothesis:  
### - (weak) Thought influences language  
### - (strong) Language influences thought

### Holds very strongly for programming languages:
>Iverson, Kenneth E. "Notation as a tool of thought". 1980. 

> Matsumoto, Yukihiro. "The Power and Philosophy of Ruby (or how to create Babel-17)". 2003

--

# Design questions

1. What is our end goal?
1. Who benefits from our work?
2. What does it mean for our software to be correct?
3. How do we ourselves use and program our software?
4. What kinds of scientists develop our software?
5. Who else wants to use our software? How will they use it?

# Design process

1. Identify what we need to do
1. Identify who is impacted
1. Identify how those people interact with the product
1. Identify what is success
1. Identify what we need to do
1. *Start engineering and architecting the product.*
1. GOTO 1.

--

# What's our product?

![blackbox](cartoons/blackbox.png)

People ask questions, and we provide answers.

# What's our product?

![us](cartoons/black_box_with_us.png)

We're inside of the black box. 

# Everything can be automated.

![robot](cartoons/robot.png)

# At least some questions can be automated.

![](cartoons/fully_automated_question.png)

# Hard questions require us

![us_in_computer](cartoons/us_in_the_computer.png)

# It's easy to end up with kludges and spaghetti code.

![bad_code](cartoons/bad_code.png)

# Making the process is part of the process

![](cartoons/onboarding.png)

# Design questions

1. How do we effectively add new features? As scientists we don't even know what they have to be when we start.
1. How do we streamline adding new data from the field, experiments, and simulations into the assets?
1. How do we quickly onboard new developers?
1. How do we streamline collaboration with external scientists?
1. How do we effeciently scale to new resources?
1. How do we do all of this while mainting cost effective **throughput**?

# Agile Software Development

Core values:

- **Individuals and Interactions** over processes and tools
- **Working Software** over comprehensive documentation
- **Customer Collaboration** over contract negotiation
- **Responding to Change** over following a plan

Adapt to scientific workflow:

- Shifting goals and shifting projects are inherent: we need to lean into the "code fast" mentality
- **Continuous Integration** instead of *perpetual prototyping*
- Include ourselves in the list of users
- We have distinct developers; can't do the fully open **scrum** board
- **Test-driven development**: assert correctness metrics first

# Stakeholders

- **Grant program managers:** Want the end scientific result  
- **In-house domain scientists:** Developing physics to meet problem-focused projects
- **Architecture team:** numerical simulation experts, high-level domain experts
- **Software engineers:** no domain knowledge but know solutions we don't  
- **External research collaborators:** Domain researchers at universities, numerical method collaborators
- **Academic end users:** Know what they're doing but don't care about the code
- **Industry end users:** Never see the code, maybe never even run the full stack themselves.

# The system needs to be designed around the people.

![seuss](cartoons/seussian.png)

# User Stories

- Design should be driven by how humans will use our product.
- To external stakeholders, we are part of the computer.
- Inside of our organization, the product needs to help us create the product.
- Some users are computer programs (automation)

# Basic Use Case

![human_running_code](cartoons/person_running_code.png)

# Typical Use Case

![batching](cartoons/batching.png)

### User stories: New developer.

The developer arrives at their desk. They are directed to the documentation webpage. They type one command in their terminal and the entire software stack and source code for EESA is checked out onto their machine. The source code is self-documented. 

Their project leader directs them to the package they will be working on and assigns them their first task on management software. The task-entry written for the new developer contains links to the source file, relevant documentation, and a link to the journal paper as guidance.

The developer types in a new equation in the module and fills in documentation. The developer launches the tests.
The linter rejects their style; they correct the code to adhere to style guidelines. 

The build framework performs tests. The tests pass and the commits are submitted into the review system. The other developers examine the changes and leave minor comments, but accept the new code. The branch is merged in to the feature branch on the team's repository.

Full tests are exectued overnight (when commodity costs are low.) The tests consisting of thousands of simulations pass. The new feature is automatically merged into the "bleeding-edge" branch in the main repository. End users on `egd/bleeding-edge` automatically pull the new feature.

# Testing must be automated


https://arstechnica.com/gadgets/2018/10/microsofts-problem-isnt-shipping-windows-updates-its-developing-them/

Windows failure is due to **waterfall engineering cycle**: Program, then integrate, then test, then push on deadline.

> Take, for example, the process Google uses for its ad server. This is a critical piece of infrastructure for the company, but new developers at the company describe that they've made code changes to fix a minor bug and seen those changes go into production within a day. When the changed code was committed to the source repository, it was automatically rebuilt and subjected to the battery of tests. The developer who owned the area of code then reviewed the change, accepted it, and it was merged into the main codebase, retested, and deployed to production.

# User Stories

- Design should be driven by how humans will use our product.

- To external stakeholders, we are part of the computer.

- Inside of our organization, the product needs to help us create the product.

- Some users are computer programs (automation)
# Basic Use Case

![human_running_code](cartoons/person_running_code.png)
# Typical Use Case

![batching](cartoons/batching.png)
### User stories: New developer.

The developer arrives at their desk. They are directed to the documentation webpage. They type one command in their terminal and the entire software stack and source code for EESA is checked out onto their machine. The source code is self-documented. 

Their project leader directs them to the package they will be working on and assigns them their first task on management software. The task-entry written for the new developer contains links to the source file, relevant documentation, and a link to the journal paper as guidance.

The developer types in a new equation in the module and fills in documentation. The developer launches the tests.
The linter rejects their style; they correct the code to adhere to style guidelines. 

The build framework performs tests. The tests pass and the commits are submitted into the review system. The other developers examine the changes and leave minor comments, but accept the new code. The branch is merged in to the feature branch on the team's repository.

Full tests are exectued overnight (when commodity costs are low.) The tests consisting of thousands of simulations pass. The new feature is automatically merged into the "bleeding-edge" branch in the main repository. End users on `egd/bleeding-edge` automatically pull the new feature.
# Testing must be automated


https://arstechnica.com/gadgets/2018/10/microsofts-problem-isnt-shipping-windows-updates-its-developing-them/

Windows failure is due to **waterfall engineering cycle**: Program, then integrate, then test, then push on deadline.

> Take, for example, the process Google uses for its ad server. This is a critical piece of infrastructure for the company, but new developers at the company describe that they've made code changes to fix a minor bug and seen those changes go into production within a day. When the changed code was committed to the source repository, it was automatically rebuilt and subjected to the battery of tests. The developer who owned the area of code then reviewed the change, accepted it, and it was merged into the main codebase, retested, and deployed to production.


# Code Review (from Google's Gerrit, a git server with more steps)

![review](figures/gerrit_code_review.png)
### User Stories: Domain Scientist

The scientist derives a new equation and opens a new module template file. The scientist describes the equation in the Domain Specific Language.

The scientist types `test`. The DSL compiler warns of a discrepency in physical units. The user corrects the exposed typo.

The scientist types `test` again. The DSL takes their expressed equation and generates numerical approximations, tangents, directional derivatives, etc. It compiles into highly optimized versions tailored to CPUs and GPUs.

The testing framework executes the test suite for changes applicable to physics modules: thousands of simulations with matching analytical solutions and benchmark comparisons.

One test-case does not pass. The user's new equation does reduce to a linear theory in a limiting-case and the new module is rejected by the test framework.

The scientist rethinks the equation.
### User Stories: Industry end user

The end user logs into the LBNL web application. The user uploads their seimic data obtained from company assets. The model inversion software processes the data on cloud resources. The user is emailed when the process is done and views the result in the web application.

The resultant geologic model is presented to the user. The user sets up a production simulation using the GUI and specifications for a parameter study. The forward simulations are scheduled, and the user is notified via email with a link to results.

The web server invoices the end user for compute resource expenses and licensing fees.

The user identifies an open problem with the reservoir and emails a contact at LBNL for guidance.
### User Stores: The AI
    
As described in the terms-of-service contract, the web server is logging all requested simulations and outputs into a database with detailed performance metrics. 

The low-cost dataset is used to continuously automatically reprogram the simulation.

Reduced-order models are continuously being trained to obtain initial condition GANs, surrogate models, performance heuristics for numerical algorithms, etc.

End users are transparently given results obtained from a reduced order model instead of the complete forward simulator at a lower cost.
# How is a simulation used?

1. **Automated Testing**
1. Write an input file, run a simulation on a laptop, look at the results.
2. Peform a parameter study in batch-mode.
1. Run a large-scale simulation on HPC. (Parallelization)
2. Use a GUI to run a simulation on cloud resources. (Fits in a modern stack)
3. Invert seismic and field data as simulation input. (Adjoints w.r.t. input data)
4. Optimize well placement. (Derivatives w.r.t. input variables)
6. Train a Reduced Ordered Model. (Database of results)
5. Have the simulation program itself. (Automatic differentiation w.r.t. *code*)

*(We start with a few user stories and work our way up through sprints and redesign.)*
# How is a simulation programmed?

- More than just the core forward simulator.
- Includes support software and libraries: meshers, linear algebra libraries, etc.
  - We shouldn't program everything: find off-the-shelf components
- Identify workflows between software components, different users, **and developers**
- Design the source code architecture to communicate to developers:
  - Scientists should be given restricted modules with a Domain Specific Language
  - Mathematicians only need to know rough properties of the equations to solve
  - Computer Scientists only need to see data flow and computation schedules
  - Software engineers only need to see commands and API specifications
- Design for interchangeable components to enable rapid prototyping, continuous integration, and longetivity:
  - Swap out equations
  - Swap out preprocessing and meshing software
  - Swap out numerical methods, matrix solvers etc.
  - Swap out different compute infrastructures
# Design Conclusions

Our product is a process that produces scientific results

1. Design based on our stakeholders' needs
1. Design based on user interaction to achieve a task
1. Design based on continuous development
1. Design based on different types of us
1. **Design based on our interaction with our product**

What qualities do we want?

1. Continuous development cycle
1. Maintain verifiability
1. Maximize throughput
1. Efficiently add labor and resources
1. Scale with number of users
1. Expresses scientific goals
# Engineering

1. **Testing**
1. Programming by Shackles
1. Agile Development
1. Fundamental Tools and Structure
1. Code Review
1. Pair programming
1. Automated builds and deployment
# Detest: an in-house automated testing framework

[https://github.com/afqueiruga/detest](https://github.com/afqueiruga/detest)

When we see something wrong with out codes, we don't know if it's a problem with:

- a bug in the code?
- a failure of the numerical model?
- a fundamental problem with the underlying theory?
- or incorrect expectations?

How do we describe the goals of our program? How do we organize tests?

1. **Unit Tests** - make sure the code works
2. **Known Analytical Oracles** - check for exact correctness, or an expected convergence rate.
3. **Self-Similarity Convergence** - Expected approximation consistence with itself.
4. **Reference Tests** - over-discretized trusted code, or experimental data.

`Detest` provides a unified framework for testing codes that solve differential equations, with a library of analytical solutions. Reuse tests with different codes to help you **write tests first** (and verify testing software.)

# Testing framework for TOUGH+ and Millstone

```bash
MacBook-Pro-14:toughstone_examples afq$ ls Testing/*
Testing/Readme.md	Testing/testframework.py

Testing/DeLeeuw_Convergence:
INPUT			__init__.py		runtest.py
INPUT_continue.format
MM_1D_gen.py		stone_input.py

Testing/PoroelasticWell:
afqsvtkutil.py	stone_input.py
INPUT.format	__init__.py	script.py
MM_1D_gen.py	parameters.py

Testing/Poroelastic_Static:
INCON		__init__.py	afqsvtkutil.py	make_plots.py
INPUT		runtest.py	stone_input.py

Testing/Preconditioner:
INCON		script.py	stone_input.py
INPUT.format	test.py

...

Testing/detest_report:
conv_exact_DeLeeuw_1.5__errors.db
conv_exact_DeLeeuw_errors.db
...
conv_exact_Terzaghi_errors.db
exact_DeLeeuw_1.2__P_contours.pdf
exact_DeLeeuw_1.2__error.pdf
exact_DeLeeuw_1.5__P_contours.pdf
exact_DeLeeuw_1.5__error.pdf
exact_DeLeeuw_P_contours.pdf
...
```
# Detest

```python
import detest
import numpy as np

import SinglePhaseWell_Radial, PoroelasticWell, Terzaghi_Convergence, ...
...

TestingFramework = detest.make_suite([
    detest.ConvergenceTest(detest.oracles.SinglePhaseWell,
              SinglePhaseWell_Radial.RUN,
              1, h_path = [40.0,30,20,10,7.5,5,2.5,1],
              params=SinglePhaseWell_Radial.default_parameters,
              report_cfg = {'idx':0}
    ),
    detest.ConvergenceTest(detest.oracles.PoroelasticWell,
              PoroelasticWell.RUN,
              1, h_path = [30,10,5,2,1.5,1],
              params=PoroelasticWell.default_parameters,
              extra_name='plane_strain',
              report_cfg = {'idx':0,'x_label':'r (m)','labels':{'U':'u_r (m)','P':'P (Pa)'}}
    ),
    detest.ConvergenceTest(detest.oracles.Terzaghi,
...
More Tests                        
...
],report=True)

if __name__=='__main__':
    import unittest
    unittest.main()
```
# Path foward

- **Design our software engineering framework first.**
  - The design of the components will follow.
- Testing comes first.
- Design around our internal-users
  - Domain scientists adding features and data
  - Numerical specialists improving algorithms and performance
  - Fully automated workflows should be typical
- Design for end users
  - Distribute our solutions quickly and cost-effectively to others
- Design for quickly shifting goals of scientific problems
print "By the way, I wrote these slides in Jupyter."
for _ in range(10): print "thanks!"