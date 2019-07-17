import numpy as np
data=np.array([[2.0,4.0],[1.0,3.0],[0.0,1.0],[-1,0.5]])
print(data)
#plot.scatter(data[:,0:1],data[:,1:2])
#plot.plot(data[:,0:1],data[:,1:2])
c=np.cov(data.T)
evalue,evecs=np.linalg.eig(c)
T=np.dot(data,evecs)
print(T)
#plot.scatter(T[:0:1],T[:1:2])
#plot.plot(T[:,0:1],T[:,1:2])
O=np.dot(T,np.linalg.inv(evecs))
print(O)