def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

	#start with all points on cluster 0, don't care, they will be reassigned on first iteration
	labels = [0]*len(points) # 1 label for each point
	final_centroids = initial_centroids.copy()
	dimensions = len(points[0])

	for _ in range(max_iterations):
		centroids_old = final_centroids.copy()
		# Assign each point to closest centroid
		for i, p in enumerate(points):
			curr_cluster = labels[i]
			curr_dist = distance(p, final_centroids[curr_cluster])
			for j, centroid in enumerate(final_centroids):
				dist = distance(p, centroid)
				if dist < curr_dist or (dist==curr_dist and j<labels[i]):
					curr_dist = dist
					labels[i] = j # assign new centroid

		# Compute new centroids
		for i in range(k):
			assigned_points = []
			for idx, l in enumerate(labels):
				if l == i:
					assigned_points.append(points[idx])
			if not assigned_points:
				continue

			new_centroid = []
			for d in range(dimensions):
				val = 0
				for assp in assigned_points:
					val += assp[d]
				new_centroid.append(val/len(assigned_points))
			
			final_centroids[i] = tuple(new_centroid)
		
		# convergence condition
		if final_centroids == centroids_old:
			break

	rounded_centroids = []
	for c in final_centroids:
		rounded = []
		for val in c:
			rounded.append(round(val,4))
		rounded_centroids.append(tuple(rounded))
	return rounded_centroids

def distance(p1, p2):
	# assuming points have same dimension, won't check
	dimensions = len(p1)
	dist_squared=0
	for i in range(dimensions):
		dist_squared += (p1[i]-p2[i])**2
	return dist_squared**0.5