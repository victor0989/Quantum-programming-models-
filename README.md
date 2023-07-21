# Quantum-programming-models-
In this project I want to create quantum programming models to build predictive data in  AI applications

Description:
With this small project I would like to start developing predictive models within the field of robotics and machine learning with quantum mechanical models built on a functional programming base.

The key difference between classical and quantum mechanics is the use of operators instead of numbers as variables. Moreover, we need to specify state vectors and their properties. Therefore, in computing the dynamics of quantum systems, we need a data structure that encapsulates the properties of a quantum operator and ket/bra vectors. The quantum object class, qutip.Qobj, accomplishes this using matrix representation. We need to build high dimensional data representations across quantum programming
in a static manner to reflect pretty well a model built upon programming functions.

Scipy example:
#!/usr/bin/python3
Program-defined function my_print() is implemented as:
def my_print(arr, cols, dec):
 n = len(arr)
 fmt = "%." + str(dec) + "f" # like %.4f
 for i in xrange(n):
 if i > 0 and i % cols == 0:
 print ""
 print fmt % arr[i],
 print "\n"

The function first finds the number of cells in the array using the Python len() function. An 
alternative is to use the more efficient NumPy size property:

#!/usr/bin/python3
n = arr.size
Note that size has no parentheses after it because it's a property, not a function. The 
my_print() function iterates through the array using traditional array indexing:
for i in xrange(n):

Using this technique, a cell value in array arr is accessed as arr[i]. An alternative is to iterate 
over the array like so:

#!/usr/bin/python3
for x in arr
Here, x is a cell value. This technique is similar to using a "for-each" loop in other languages 
such as C#. In most situations, I prefer using array indexing to "for-eaching" but most of my 
colleagues prefer the "for x in arr" syntax.
Next, the demo program creates an array using the NumPy zeros() function:
arr = np.zeros(5)
print "Printing array arr using built-in print() 
