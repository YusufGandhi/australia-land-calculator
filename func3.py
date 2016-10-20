import math
import matplotlib.pyplot as plt


def f3(filePath, height = -1, interval = 0.01):
	longitudeList = []
	latitudeList = [0]
	elevationList = []
	f = open(filePath,'r')

	# iterate through lines of data file
	for line in f:
		tokens = line.split()
		if latitudeList[len(latitudeList)-1] != float(tokens[0]):
			latitudeList.append(float(tokens[0]))
		if len(latitudeList) == 2:
			longitudeList.append(float(tokens[1]))
		elevationList.append(float(tokens[2]))
	f.close()

	latitudeList = latitudeList[1:]
	
	i = 1
	longitudeDifferenceList = []
	latitudeDifferenceList = []

	# calculating the average latitude
	for i in range(1,len(latitudeList)):
		latitudeDifferenceList.append(abs(latitudeList[i]-latitudeList[i-1]))
	averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)
	
	# calculating the average longitude
	for i in range(1,len(longitudeList)):
		longitudeDifferenceList.append(abs(longitudeList[i]-longitudeList[i-1]))
	averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)

	# calculating the vertical spacing value using the average latitude
	verticalSpacing = round(averageLatitude * 40007/360,3)
	
	# calculating the horizontal spacing value using the average longitude
	# saved each spacing list in a list for caclculating the individual area
	# for the second approximation purpose
	horizontalSpacingList = []
	for lat in latitudeList:
		horizontalSpacingList.append(40075/360 * abs(math.cos(math.radians(lat))) * averageLongitude)
	averageHorizontalSpacing = round(sum(horizontalSpacingList) / len(horizontalSpacingList),3)

	# the users set the heights which means the 1st level functionality is chosen
	if height >= 0:
		aboveSea1 = 0
		totalLand1 = 0
		aboveSea2 = 0
		totalLand2 = 0

		# the main logic of calculating the total land above the set sea height parameter
		# and the total land above 0.0 sea level
		for i in range(0,len(latitudeList)):
			for j in range(0,len(longitudeList)):
				if elevationList[i*len(longitudeList)+j] > 0.0:
					totalLand1 += verticalSpacing*averageHorizontalSpacing # 1st approx
					totalLand2 += verticalSpacing*horizontalSpacingList[i] # 2nd approx
					if elevationList[i*len(longitudeList)+j] > height:
						aboveSea1 += verticalSpacing*averageHorizontalSpacing # 1st approx
						aboveSea2 += verticalSpacing*horizontalSpacingList[i] # 2nd approx
				

		print("Functionality level 1:\n")
		print("First Approximation")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(aboveSea1))
		print("Percent area above sea level: {:.2f}%".format(aboveSea1/totalLand1*100))
		print("\nSecond Approximation")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(aboveSea2))
		print("Percent area above sea level: {:.2f}%".format(aboveSea2/totalLand2*100))
	
	# the users don't provide the height parameter, thus it is the 2nd level functionality that is chosen
	# the interval parameter is optional (default value = 1% of the maximum sea level height)
	elif height == -1:
		maxSeaLevel = max(elevationList)
		total_area1 = []
		total_area2 = []
		intervalList = []
		spacing = maxSeaLevel * interval
		print("Functionality level 2")
		print("---------------------")
		for k in range(0, int(1 / interval) + 1):
			heightm = k * spacing
			aboveSea1 = 0
			totalLand1 = 0
			aboveSea2 = 0
			totalLand2 = 0
			for i in range(0,len(latitudeList)):
				for j in range(0,len(longitudeList)):
					if elevationList[i*len(longitudeList)+j] > 0.0:
						totalLand1 += verticalSpacing*averageHorizontalSpacing # 1st approx
						totalLand2 += verticalSpacing*horizontalSpacingList[i] # 2nd approx
						if elevationList[i*len(longitudeList)+j] > heightm:
							aboveSea1 += verticalSpacing*averageHorizontalSpacing # 1st approx
							aboveSea2 += verticalSpacing*horizontalSpacingList[i] # 2nd approx

			print("Approximation 1: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, aboveSea1, aboveSea1/totalLand1*100))
			print("Approximation 2: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, aboveSea2, aboveSea2/totalLand2*100))

			
			total_area1.append(aboveSea1)
			total_area2.append(aboveSea2)
			
			intervalList.append(k * spacing)
	

		# plotting the graph
		plt.subplot(121)
		plt.plot(intervalList, total_area1)
		plt.title('Approximation 1')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		plt.subplot(122)
		plt.plot(intervalList, total_area2)
		plt.title('Approximation 2')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		plt.show()

