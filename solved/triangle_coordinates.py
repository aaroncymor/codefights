def TriangleCoordinates(n):
	"""
	You are given 3 points on the Cartesian plane that form a triangle. Find the area of this triangle.

	Example

		TriangleCoordinates([[2, 7], [12, 7], [6, 17]]) = 50
		TriangleCoordinates([[-182, -152], [-192, -141], [-164, -138]]) = 169
		TriangleCoordinates([[0, 0], [3, 0], [2, 8]]) = 12

	area = |Ax(By-Cy)+Bx(Cy-Ay)+Cx(Ay-By)/2|
	"""
	return abs((n[0][0]*(n[1][1]-n[2][1]) + n[1][0]*(n[2][1]-n[0][1]) + n[2][0]*(n[0][1]-n[1][1]))/2)

print TriangleCoordinates([[2,7],[12,7],[6,17]])
print TriangleCoordinates([[-182,-152],[-192,-141],[-164,-138]])