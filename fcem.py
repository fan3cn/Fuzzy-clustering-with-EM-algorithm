import numpy as np

# Load data
X = np.loadtxt(open("Q2Q3_input.csv", "rb"), delimiter=",", skiprows=1, usecols= range(1,7))

# Initialize Clustering Centers
C1 = np.matrix("1,1,1,1,1,1")
C2 = np.matrix("0,0,0,0,0,0")

# Iteration
for i in range(50):
	# Calaulate square distance to C1 & C2
	dist_1 = np.sum(np.square(X - C1),axis=1)
	dist_2 = np.sum(np.square(X - C2),axis=1)
	# Calculate W_C1 & W_C2
	W_C1 = dist_2/(dist_1 + dist_2)
	W_C2 = 1 - W_C1
	# Calculate SSE(sum of squared error)
	SSE = np.sum(np.multiply(dist_1, W_C1)) + np.sum(np.multiply(dist_2, W_C2))
	# Save as old value
	C1_old = C1
	C2_old = C2
	# Calculate new Clustering Centers
	C1 = np.matmul(np.transpose(np.square(W_C1)), X)/np.sum(np.square(W_C1))
	C2 = np.matmul(np.transpose(np.square(W_C2)), X)/np.sum(np.square(W_C2))
	# Print
	if i<=1:
		print("After iteration "+ str(i+1) + ":")
		print("the updated SSE(sum of squared error) is:")
		print(SSE)		
		print("the updated C1 is:")
		print(C1)
		print("the updated C2 is:")
		print(C2)
	# Calculate the sum of L1 distance of two clustering centers
	L1_sum = np.sum(np.absolute(C1_old - C1)) + np.sum(np.absolute(C2_old - C2))
	# Terminate
	if L1_sum <= 0.001:
		print("After "+ str(i+1) + " iterations, with L1_sum="+str(L1_sum)+",the clusters converge.")
		break
# Print result
print("Converged C1:")
print(C1)
print("Converged C2:")
print(C2)


