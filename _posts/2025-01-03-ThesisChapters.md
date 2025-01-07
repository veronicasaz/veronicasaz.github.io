---
title: "Thesis Chapters"
layout: post
---

Ph.D. Thesis Chapters:
- [Full thesis](Thesis.pdf) *(Not yet available)*
- [Chapter 1: Introduction](Introduction_v1.pdf)
- [Chapter 2: A hybrid approach for solving the gravitational *N*-body problem with Artificial Neural Networks](Chapter2.pdf)
- [Chapter 3: A Generalized Framework of Neural Networks for Hamiltonian Systems](Chapter3.pdf)
- [Chapter 4: Reinforcement Learning for Adaptive Time-Stepping in the Chaotic Gravitational Three-Body Problem](Chapter4.pdf)
- [Chapter 5: Reinforcement Learning for the time-step size estimation in bridged cluster dynamics simulations](Chapter5.pdf) *(Not yet available)*



### Chapter 2: A hybrid approach for solving the gravitational *N*-body problem with Artificial Neural Networks
**Abstract**

Simulating the evolution of the gravitational $N$-body problem becomes extremely computationally expensive as $N$ increases since the problem complexity scales quadratically with the number of bodies. 
In order to alleviate this problem, we study the use of Artificial Neural Networks (ANNs) to replace expensive parts of the integration of planetary systems.
Neural networks that include physical knowledge have rapidly grown in popularity in the last few years, although few attempts have been made to use them to speed up the simulation of the motion of celestial bodies. For this purpose, we study the advantages and limitations of using Hamiltonian Neural Networks to replace computationally expensive parts of the numerical simulation of planetary systems, focusing on realistic configurations found in astrophysics. We compare the results of the numerical integration of a planetary system with asteroids with those obtained by a Hamiltonian Neural Network and a conventional Deep Neural Network, with special attention to understanding the challenges of this specific problem. Due to the non-linear nature of the gravitational equations of motion, errors in the integration propagate, which may lead to divergence from the reference solution. To increase the robustness of a method that uses neural networks, we propose a hybrid integrator that evaluates the prediction of the network and replaces it with the numerical solution if considered inaccurate.

Hamiltonian Neural Networks can make predictions that resemble the behavior of symplectic integrators but are challenging to train and in our case fail when the inputs differ $\sim$7 orders of magnitude. In contrast, Deep Neural Networks are easy to train but fail to conserve energy, leading to fast divergence from the reference solution. The hybrid integrator designed to include the neural networks increases the reliability of the method and prevents large energy errors without increasing the computing cost significantly. For the problem at hand, the use of neural networks results in faster simulations when the number of asteroids is ~70.

### Chapter 3: A Generalized Framework of Neural Networks for Hamiltonian Systems
**Abstract**

When solving Hamiltonian systems using numerical integrators, preserving the symplectic structure may be crucial for many problems. At the same time, solving chaotic or stiff problems requires integrators to approximate the trajectories with extreme precision. Integrating Hamilton's equations to a level of scientific reliability such that the answer can be used for scientific interpretation, may lead to computationally expensive simulations. In some cases, a neural network can be a viable alternative to numerical integrators, offering high-fidelity solutions orders of magnitudes faster.
	
To understand the role of preservation of symplecticity in problems where neural networks are used, we analyze three well-known neural network architectures that include the symplectic structure inside the neural network's topology. Between these neural network architectures, many similarities can be found. This allows us to formulate a new, generalized framework for these architectures. In the generalized framework Symplectic Recurrent Neural Networks, SympNets, and HénonNets are special cases. Additionally, this new framework enables us to find novel neural network topologies by transitioning between the established ones. 
	
We compare new Generalized Hamiltonian Neural Networks (GHNNs) against the already established SympNets, HénonNets, and physics-unaware multilayer perceptrons. This comparison is performed for the gravitational three-body problem. In order to perform a fair comparison, the hyperparameters of the different neural networks are chosen such that the prediction speeds of all four architectures are the same during inference. A special focus lies on the capability of the neural networks to generalize outside the training data. The GHNNs outperform all other neural network architectures for the problem considered.

### Chapter 4: Reinforcement Learning for Adaptive Time-Stepping in the Chaotic Gravitational Three-Body Problem
**Abstract**

Many problems in astrophysics cover multiple orders of magnitude in spatial and temporal scales. While simulating systems that experience rapid changes in these conditions, it is essential to adapt the (time-) step size to capture the behavior of the system during those rapid changes and use a less accurate time step at other, less demanding, moments. We encounter three problems with traditional methods. Firstly, making such changes requires expert knowledge of the astrophysics as well as of the details of the numerical implementation. Secondly, some parameters that determine the time-step size are fixed throughout the simulation, which means that they do not adapt to the rapidly changing conditions of the problem. Lastly, we would like the choice of time-step size to balance accuracy and computation effort. 
We address these challenges with Reinforcement Learning by training it to select the time-step size dynamically. We use the integration of a system of three equal-mass bodies that move due to their mutual gravity as an example of its application. With our method, the selected integration parameter adapts to the specific requirements of the problem, both in terms of computation time and accuracy while eliminating the expert knowledge needed to set up these simulations.
Our method produces results competitive to existing methods and improve the results found with the most commonly-used values of time-step parameter. This method can be applied to other integrators without further retraining. We show that this extrapolation works for variable time-step integrators but does not perform to the desired accuracy for fixed time-step integrators.  

### Chapter 5: Reinforcement Learning for the time-step size estimation in bridged cluster dynamics simulations
**Abstract**



