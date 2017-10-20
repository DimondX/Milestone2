import cntk
import numpy as np

cntk.device.try_set_default_device(cntk.device.cpu())

# Define the network
input_dim = 1
num_output_classes = 2
num_training_samples = 1
# Ensure we always get the same amount of randomness
np.random.seed(0)

# array X has a set of inputs
X = np.random.randn(num_training_samples, input_dim)
X = X.astype(np.float32)   
X[0,0]=2
h = np.random.randn(num_training_samples, input_dim)
h = h.astype(np.float32)   #numpy default is float64, wrong type
c = np.random.randn(num_training_samples, input_dim)
c = c.astype(np.float32)   

# this is what each input is like
feature = cntk.input(input_dim, np.float32)
dc = cntk.input(input_dim, np.float32)
dh = cntk.input(input_dim, np.float32)

# make LSTM layer
# for LSTM the weights will be dim X 4, so input_dim=2 gives 2 X 8 weights matrix
z = cntk.layers.LSTM(input_dim,init=0)
model = z(dh,dc,feature)

print('before')
print('h=',h)
print('c=',c)

h,c = model(h,c,X)
print('after')
print('h=',h)
print('c=',c)
print('Weights=',z.W.value)
print('X=',X)
