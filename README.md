# The Ising Model
 
The Ising model is a mathematical model of ferromagnetism in statistical mechanics. 

## Theory

Electrons have a quantum mechanical property of spin, which when measured along any axis take the value of either $-\hbar/2$ or $\hbar/2$. The spin of an electron is closely related to its magnetic moment, as if the electron is a tiny bar magnet with both a north and a south pole. In this sense, the north pole can either point up or down. The magnetic moment between two nearby electrons creates a force between them, so that they prefer to line up anti-parallel, or anti-aligned. But there are two important points to consider:

- Electrons repel each other electrostatically since they have the same charge, and
- the Pauli exclusion principle, which states that no two electron can be in the same quantum mechanical state in the same location.

Considering electrons situated on a regular grid, focus on the nearest-neighbour pair. When the pair is anti-aligned, they can be close together as the electrons are not in the same quantum state and there will be no electrostatic repulsion. When aligned, the electrons cannot get too close together or else break the exclusion principle, and there is little electrostatic repulsion. Interestingly, it is energetically favourable for the electrons to be in the parallel spin state. The difference in energy between parallel and anti-parallel states is mainly electrostatic in origin, with little from the magnetic interaction. As such, the electrons in a regular lattice tend to be aligned in the same direction, with the indiviidual magnetic moments of each adding up to create a large net magnetic moment. This is Ising's model for ferromagnetism. 

Consider a 2D lattice with spins at each lattice site. The ith spin can take one of two values: $s_i = \pm 1$. We will consider only the nearest neighbours, that being above, below, to the left and to the right. We will not consider diagonal interactions. This is a good approximation because Pauli's exclusion principle is only relevant if the spins are in the immediate proximity to each other.

The energy of the system is given by:

$$ \tag{1} E = \sum_{i=1}^{N} E_i \text{  and  } E_i = - \frac{J}{2} \sum_{j = i \pm 1} s_i s_j$$

where $E$ is the total energy, $E_i$ is the energy of the ith index, $s_i$ is the ith spin, and $J$ is the exchange constant ($J > 0$ for ferromagnets). $J$ has dimensions of energy. To clarify, the sum over $j = i \pm 1$ for the $E_i$ equation means summing over nearest neighbours.

The energy of the lattice depends on whether the majority of spins are aligned or anti-aligned:

- If all spins are aligned $E = -2JN$. This is the lowest energy state of the system.
- If the spins are random, $E \approx 0$.

Now let the system have a temperature $T$, such that the electrons have some kinetic energy and move about a mean position. If $T$ is sufficiently high, the spins can spontaneously flip! The probability of a spin flipping from state 1 to state 2, $P_{12}$, is given by the Boltzmann factor:

$$ P_{12} \propto \exp \left( - \frac{E_{12}}{k_B T} \right) $$

where $E_{12} = E_2 - E_1$ is the difference in the energies of the two states, and $k_B$ is  Boltzmann's constant.

- If $E_1 > E_2$, $E_{12} < 0$, and so $P_{12} > P_{21} \implies$ more likely to flip to a lower energy state.
- If $\left| E_{12} \right| \ll k_B T$, $P_{12} \approx P_{21} \implies$ at high $T$ flips in either direction are equally likely.