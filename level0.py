# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:50:29 2017

@author: Chris
"""

import cntk
import numpy as np
import operator

cntk.device.try_set_default_device(cntk.device.cpu())

# Define the network
input_dim = 2
num_output_classes = 2
num_training_samples = 2
# Ensure we always get the same amount of randomness
np.random.seed(0)

# array X has a set of inputs
X = np.random.randn(num_training_samples, input_dim)
X = X.astype(np.float32)   

# this is what each input is like
feature = cntk.input(input_dim, np.float32)

#z = cntk.layers.Dense(input_dim, init=1, activation=cntk.ops.relu)
# give one feature as input to get z.W defined as 10x10
z = cntk.layers.Dense(input_dim, activation=cntk.ops.sigmoid)
model = z(feature)
# echo out the values
print(z.W.value)
print(z.b.value)
print(X)

# assign first input to new variable features
#features = X[0]
#print(z(x=feature))
print(model.eval({feature:X[0]}))

# map the output to the Blender ontology
p =cntk.softmax(model.eval({feature:X})).eval()
print(p)
# find winner of just first set
index, value = max(enumerate(p[0]), key=operator.itemgetter(1))
print(index,value)
blenderTokens = ['circle','square','triangle']
print(blenderTokens[index])

#send tokens to blender to see what it thinks!
#
# --> go to blender ??
#