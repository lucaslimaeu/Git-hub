import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from math import pi, exp, sqrt
from scipy import integrate

#um vendedor tem a probabilidade de 5% para fechar uma venda e tem uma meta
# de 5 vendas por dia. Quantas ligações ele precisa fazer para fechar 5 vendas?
# P=0,05
# r=5
# 
import numpy as np

# Define the probability of success (p)
p = 0.05 # Change this to your desired probability

# Generate random samples from a Bernoulli distribution
num_samples = 5 # Change this to the number of samples you want
samples = np.random.binomial(1, p, num_samples)

# Print the generated samples
print(samples) 