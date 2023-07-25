
from qutip import *
#This will load all of the user available functions. Often, we also need to import the NumPy and Matplotlib libraries with:
import numpy as np
import matplotlib.pyplot as plt
from qutip import *
settings.colorblind_safe = True

#2nd SECTION
import matplotlib.pyplot as plt
plt.rcParams['savefig.transparent'] = True

X = sigmax() # DOES NOT WORK
S = spre(X) * spost(X.dag())

hinton(S)

# For qubits, a particularly useful way to visualize superoperators is to plot them in the Pauli basis, such that Sμ,ν=⟨⟨σμ|S[σν]⟩⟩
# . Because the Pauli basis is Hermitian, Sμ,ν
#  is a real number for all Hermitian-preserving superoperators (S) allowing us to plot the elements of S
# In such diagrams, positive elements are indicated by white squares, and negative elements by black squares. The size of each element is indicated by the size of the corresponding square. For instance, let S[ρ]=σxρσ†x
# Then S[σμ]=σμ⋅{+1−1μ=0,xμ=y,z

# Choi matrix J(Λ) of a quantum map Λ
# is useful for working with ancilla-assisted process tomography (AAPT), and for reasoning about properties of a map or channel. Up to normalization, the Choi matrix is defined by acting Λ
# on half of an entangled pair. In the column-stacking convention,

# FORMULA TO REPRESENT MATRIX STATES: J(Λ)=(1⊗Λ)[|1⟩⟩⟨⟨1|].

I, X, Y, Z = qeye(2), sigmax(), sigmay(), sigmaz()
#POSSIBLE OUTPUTS
Quantum object: dims = [[[2], [2]], [[2], [2]]], shape = (4, 4), type = super, isherm = True
Qobj data =
[[0.5 0.  0.  0.5]
 [0.  0.  0.  0. ]
 [0.  0.  0.  0. ]
 [0.5 0.  0.  0.5]]

# In particular, let {Ai} be a set of operators such that J(Λ)=∑i|Ai⟩⟩⟨⟨Ai|
# We can write J(Λ) In this way for any hermicity-preserving map; that is, for any map Λ
# such that J(Λ)=J†(Λ) and these operators then form the Kraus representation of Λ. In particular, for any input ρ
# The Stinespring representation is closely related to the Kraus representation, and consists of a pair of operators A and B such that for all operators X
# acting on H
# FORMULA: Λ(X)=Tr2(AXB†), where the partial trace is over a new index that corresponds to the index in the Kraus summation.
# Conversion to Stinespring is handled by the to_stinespring function.
