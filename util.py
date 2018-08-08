from stl import mesh as stlmesh
from mpl_toolkits import  mplot3d
from matplotlib import pyplot
import numpy as np

def plotMesh(mesh, points=None):
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    toPlot = stlmesh.Mesh(np.zeros(mesh.faces.shape[0], dtype=stlmesh.Mesh.dtype))
    for i, f in enumerate(mesh.faces):
        for j in range(3):
            toPlot.vectors[i][j] = mesh.vertices[f[j],:]
                            
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(toPlot.vectors))

    if not(points is None) and points.any():
        axes.scatter3D(points[:,0], points[:,1], zs=points[:,2], c='r', s=20)
    # Auto scale to the mesh size
    scale = toPlot.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()
