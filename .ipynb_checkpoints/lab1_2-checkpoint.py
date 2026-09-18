import numpy as np
from scipy import constants,sparse,spatial,interpolate
import matplotlib.pyplot as plt

def main():
    #constants
    print("speed of light in vaccum:",constants.c)
    print("planck constant (reduced):",constants.hbar)
    print("boltzmann constant:",constants.k)

    #sparse data
    #sparse matrix
    data = np.array([1,2,3])
    row=np.array([0,1,2])
    col=np.array([0,1,2])
    sparse_matrix=sparse.coo_matrix((data,(row,col)),shape=(3,3))
    print("\nSparse Matrix:")
    print(sparse_matrix.toarray())

    # Graphs (Networks) 
    # Creating a simple graph using dok_matrix

    G=sparse.dok_matrix((5,5),dtype=bool)
    G[0,1]=G[1,0]=1
    G[1,2]=G[2,1]=1
    G[2,3]=G[3,2]=1
    G[3,4]=G[4,3]=1
    print("\nGraph (Adjacency matrix representation):") 
    print(G.toarray())

    #spatialdata
    points=np.array([[0,0],[0,1.1],[1,0],[1,1]])
    tri=spatial.Delaunay(points)
    plt.figure(figsize=(6,4))
    plt.triplot(points[:,0],points[:,1],tri.simplices)
    plt.plot(points[:, 0], points[:, 1], 'o')
    plt.title('Delaunay Triangulation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

    #Matlab Arrays
    mat_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
    matlab_matrix=np.asmatrix(mat_array)
    print("\nmatlab array:")
    print(matlab_matrix)

    #interpolation
    x=np.linspace(0,10,10)
    y=np.sin(x)
    f=interpolate.interp1d(x,y)
    x_new=np.linspace(0,10,100)
    y_new=f(x_new)
    plt.figure(figsize=(8,4))
    plt.plot(x,y,'o',label='original data')
    plt.plot(x_new,y_new,'-',label='Interpolated data')
    plt.title('Interpolation Example')
    plt.xlabel('X-axis') 
    plt.ylabel('Y-axis') 
    plt.legend() 
    plt.show()

main()