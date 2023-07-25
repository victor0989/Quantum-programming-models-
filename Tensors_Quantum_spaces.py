# HERE in this examples I am investigating how to manipulate high order dimenssional data with tensor products upon the basics of quentum objects visualization


>>> basis(5,2)
Quantum object: dims = [[5], [1]], shape = (5, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [1.]
 [0.]
 [0.]]
>>> tensor([sigmax(), sigmax()])
Quantum object: dims = [[2, 2], [2, 2]], shape = (4, 4), type = oper, isherm = True
Qobj data =
[[0. 0. 0. 1.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]
 [1. 0. 0. 0.]]
# Entropy Functions
# concurrence(rho)[source]
# Calculate the concurrence entanglement measure for a two-qubit state.
# Parameters
# stateqobj
# Ket, bra, or density matrix for a two-qubit state.Returns concurfloat

# Calculates the conditional entropy S(A|B)=S(A,B)−S(B) of a selected density matrix component.
# Linear entropy of a density matrix (Parameters, rhoqobj,density matrix or ket/bra vector.

#ENTROPY CALCULATION FOR QUANTUM SPACES
Qobj data =
[[0. 0. 0. 1.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]
 [1. 0. 0. 0.]]
>>> rho=0.5*fock_dm(2,0)+0.5*fock_dm(2,1)
>>> entropy_linear(rho)
0.5
