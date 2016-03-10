def lightBulbs(lights, n):
	temp_lights = [e for e in lights]
	for i in range(n):
		j = 0
		while j < len(lights):
			if lights[j] == 1:
				#print j, (j + 1 < len(lights))
				if j + 1 < len(lights):
					if temp_lights[j + 1] == 1:
						temp_lights[j + 1] = 0
					else:
						temp_lights[j + 1] = 1
				else:
					if j == len(lights) - 1:
						if temp_lights[0] == 1:
							temp_lights[0] = 0
						else:
							temp_lights[0] = 1
			j += 1
		lights = [e for e in temp_lights]

	return temp_lights

#lights: [0, 0, 1, 1, 1]
#n: 5
print lightBulbs([0,0,1,1,1],5)
#[0, 0, 1, 1, 1]
#[1, 0, 1, 0, 0]
#[1, 1, 1, 1, 0]
#[1, 0, 0, 0, 1]
#[0, 1, 0, 0, 1]
#[1, 1, 1, 0, 1]