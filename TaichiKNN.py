"""
Find the KNN nearest points by using Taichi
"""

N = point_np.shape[0]
point = ti.Vector.field(2, dtype=ti.f64, shape=N)
point.from_numpy(marker_point_np)
nearest = ti.ndarray(dtype=ti.i32, shape=N)

sorts = ti.field(dtype=ti.i32, shape=NV)
dists = ti.field(dtype=ti.f64, shape=NV)

@ti.kernel
def points_knn(point:ti.types.vector(2, dtype=ti.f64)):
    """
    Find the K-th nearest nodes No. and the weights.
    :param point: ti.Vector
    :return:
    """
    sorts.fill(0)
    dists.fill(0.)
    for i in range(NV):
        sorts[i] = i
        dists[i] = (pos_init[i] - point).norm()

for i in range(N):
    points_knn(point[i])
    ti.algorithms.parallel_sort(dists, sorts)
    sorts_host = sorts.to_numpy()
    nearest_idx = sorts_host[0]
    nearest[i] = nearest_idx
