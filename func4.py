import math
import matplotlib.pyplot as plt


def f3(filePath, height = -1, interval = 0.01):
	longitudeList = []
	latitudeList = [0]
	elevationList = []
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			if latitudeList[len(latitudeList)-1] != float(tokens[0]):
				latitudeList.append(float(tokens[0]))
			if len(latitudeList) == 2:
				longitudeList.append(float(tokens[1]))
			elevationList.append(float(tokens[2]))
	latitudeList = latitudeList[1:]
	# print(len(longitudeList))
	# print(len(latitudeList))



	i = 1
	longitudeDifferenceList = []
	latitudeDifferenceList = []

	for i in range(1,len(latitudeList)):
		latitudeDifferenceList.append(abs(latitudeList[i]-latitudeList[i-1]))
	averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)
	
	
	for i in range(1,len(longitudeList)):
		longitudeDifferenceList.append(abs(longitudeList[i]-longitudeList[i-1]))
	averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)


	# while i < len(longitudeList):
	# 	if abs(longitudeList[i] - longitudeList[i-1]) > 0 and abs(latitudeList[i] - latitudeList[i-1]) == 0.0:
	# 		longitudeDifferenceList.append(abs(longitudeList[i] - longitudeList[i-1]))
	# 	else:
	# 		latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))
	# 	# the the difference of the latitude
	# 	# if abs(latitudeList[i] - latitudeList[i-1]) > 0:
	# 	# 	latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))

	# 	i += 1
	# averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)
	# averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)

	verticalSpacing = averageLatitude * 40007/360
	horizontalSpacingList = []
	for lat in latitudeList:
		horizontalSpacingList.append(40075/360 * abs(math.cos(math.radians(lat))) * averageLongitude)
	averageHorizontalSpacing = sum(horizontalSpacingList) / len(horizontalSpacingList)

	if height >= 0:
		aboveSea1 = 0
		totalLand1 = 0
		aboveSea2 = 0
		totalLand2 = 0
		SetList = []
		for i in range(0,len(latitudeList)):
			for j in range(0,len(longitudeList)):
				if elevationList[i*len(longitudeList)+j] > 0.0:
					# print '.',
					totalLand1 += verticalSpacing*averageHorizontalSpacing
					totalLand2 += verticalSpacing*horizontalSpacingList[i]
					if elevationList[i*len(longitudeList)+j] > height:
						aboveSea1 += verticalSpacing*averageHorizontalSpacing
						aboveSea2 += verticalSpacing*horizontalSpacingList[i]
						
						#Counting Island Stuff
						
						FoundSets = []
						if i != 0 and j != 0:
							for l in range(0,len(SetList)):
								if ( (i,j-1) in SetList[l] ) or ( (i-1,j-1) in SetList[l] ) or ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
									FoundSets.append(l)
							if len(FoundSets) == 0:
								s = {(i,j)}
								SetList.append(s)
							elif len(FoundSets) == 1:
								SetList[FoundSets[0]].add((i,j))
							elif len(FoundSets) == 2:
								s = SetList[FoundSets[0]].union(SetList[FoundSets[1]])
								if FoundSets[0] < FoundSets[1]:
									del SetList[FoundSets[1]]
									del SetList[FoundSets[0]]
								elif FoundSets[0] > FoundSets[1]:
									del SetList[FoundSets[0]]
									del SetList[FoundSets[1]]
								s.add((i,j))
								SetList.append(s)
							elif len(FoundSets) > 2:
								print("IMPOSSIBLE, YOU JUST BROKE LOGIC")
						elif i == 0 and j != 0:
							for l in range(0,len(SetList)):
								if ( (i,j-1) in SetList[l] ):
									FoundSets.append(l)
							if len(FoundSets) == 0:
								s = {(i,j)}
								SetList.append(s)
							elif len(FoundSets) == 1:
								SetList[FoundSets[0]].add((i,j))
						elif i != 0 and j == 0:
							for l in range(0,len(SetList)):
								if ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
									FoundSets.append(l)
							if len(FoundSets) == 0:
								s = {(i,j)}
								SetList.append(s)
							elif len(FoundSets) == 1:
								SetList[FoundSets[0]].add((i,j))
						elif i == 0 and j == 0:
							SetList.append({(i,j)})
						#END SET COUNTING		
						
						
				# else:
				# 	print ' ',
			# print(' ')
			
		print("First functionality")
		print("===================")
		print("First Approximation:")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(aboveSea1))
		print("Percent area above sea level: {:.2f}%".format(aboveSea1/totalLand1*100))
		print("\nSecond Approximation")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(aboveSea2))
		print("Percent area above sea level: {:.2f}%".format(aboveSea2/totalLand2*100))
		print(len(SetList))
		print(len(SetList[0]), len(SetList[1]), len(SetList[2]))
	elif height == -1:
		maxSeaLevel = 0	
		for el in elevationList:
			maxSeaLevel = max(el, maxSeaLevel)
				
		# print (maxSeaLevel)
		total_area1 = []
		total_area2 = []
		intervalList = []
		spacing = maxSeaLevel * interval
		for k in range(0, int(1 / interval) + 1):
			#(area, percent) = f1(filePath, meanArea, i * spacing)
			# --- ABSTRACT ---
			heightm = k * spacing
			aboveSea1 = 0
			totalLand1 = 0
			aboveSea2 = 0
			totalLand2 = 0
			SetList = [] # For Counting Island Stuff
			for i in range(0,len(latitudeList)):
				for j in range(0,len(longitudeList)):
					if elevationList[i*len(longitudeList)+j] > 0.0:
						# print '.',
						totalLand1 += verticalSpacing*averageHorizontalSpacing
						totalLand2 += verticalSpacing*horizontalSpacingList[i]
						if elevationList[i*len(longitudeList)+j] > heightm:
							aboveSea1 += verticalSpacing*averageHorizontalSpacing
							aboveSea2 += verticalSpacing*horizontalSpacingList[i]
					
							#Counting Island Stuff
							
							FoundSets = []
							if i != 0 and j != 0:
								for l in range(0,len(SetList)):
									if ( (i,j-1) in SetList[l] ) or ( (i-1,j-1) in SetList[l] ) or ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
										FoundSets.append(l)
								if len(FoundSets) == 0:
									s = {(i,j)}
									SetList.append(s)
								elif len(FoundSets) == 1:
									SetList[FoundSets[0]].add((i,j))
								elif len(FoundSets) == 2:
									s = SetList[FoundSets[0]].union(SetList[FoundSets[1]])
									del SetList[FoundSets[0]]
									del SetList[FoundSets[1]]
									s.add((i,j))
									SetList.append(s)
								elif len(FoundSets) > 2:
									print("IMPOSSIBLE, YOU JUST BROKE LOGIC")
							elif i == 0 and j != 0:
								for l in range(0,len(SetList)):
									if ( (i,j-1) in SetList[l] ):
										FoundSets.append(l)
								if len(FoundSets) == 0:
									s = {(i,j)}
									SetList.append(s)
								elif len(FoundSets) == 1:
									SetList[FoundSets[0]].add((i,j))
							elif i != 0 and j == 0:
								for l in range(0,len(SetList)):
									if ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
										FoundSets.append(l)
								if len(FoundSets) == 0:
									s = {(i,j)}
									SetList.append(s)
								elif len(FoundSets) == 1:
									SetList[FoundSets[0]].add((i,j))
							elif i == 0 and j == 0:
								SetList.append({(i,j)})
							#END SET COUNTING
							
									
					# else:
					# 	print ' ',
				# print(' ')
			# --- END ABSTRACT ---

			print("Approximation 1: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, aboveSea1, aboveSea1/totalLand1*100))
			print("Approximation 2: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, aboveSea2, aboveSea2/totalLand2*100))
			
			total_area1.append(aboveSea1)
			total_area2.append(aboveSea2)
			
			intervalList.append(k * spacing)
	
		# plotting the graph
		# plt.figure(1)
		plt.subplot(121)
		plt.plot(intervalList, total_area1)
		plt.title('Approximation 1')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		# plt.figure(2)
		plt.subplot(122)
		plt.plot(intervalList, total_area2)
		plt.title('Approximation 2')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		plt.show()


f3('sydney250m.txt',2)
