# Steps:
# 1) insert the functionality [1-4], keep asking if users
#	 enter the wrong number
# 2) if 1: enter 4 parameters: filepath, mean vertical spacing,
#		   mean horizontal spacing, and sea height
#    if 2: enter 4 parameters: filepath, mean vertical spacing,
#		   mean horizontal spacing, and interval
#    if 3: enter 2 parameters: filepath, and sea height (for first functionality)

from func1 import f1
from func2 import f2
from func3 import f3
from func4 import f4
from func4image import f4i
import sys
import argparse
	
if len(sys.argv) > 1: #User provided args
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--file", help="Input data file.")
	parser.add_argument("-l","--height", help="New sea level height.", type=float)
	parser.add_argument("-i","--interval", help="Interval of sea levels.", type=int)
	parser.add_argument("-m","--image", help="Display an image.", action="store_true")
	args = parser.parse_args()

	file_name = args.file
	filevalid = True
	try:		
		f = open(file_name, 'r')
	except FileNotFoundError:
		print("[Error] Cannot open", file_name)
		filevalid = False
	
	if filevalid:
		if args.image:
			if args.height != None:
				f4i(args.file, height=args.height)
			elif args.interval != None:
				f4i(args.file, interval=(1/args.interval))
			else:
				f4i(args.file)
		else:
			if args.height != None:
				f4(args.file, height=args.height)
			elif args.interval != None:
				f4(args.file, interval=(1/args.interval))
			else:
				f4(args.file)
else:

	print("Welcome to AUSTRALIA LAND CALCULATOR")
	print("====================================\n")
	print("Choose 1 from 4 available funcitonality levels")
	print("Level 1. Calculate area above sea level")
	print("Level 2. Calculate area every sea level increase")
	print("Level 3. Level 1 & 2 functionalities")

	func_choice = -1
	while func_choice < 1 or func_choice > 4:
		try:
			func_choice = int(input("Enter the desired functionality level [1-4]: "))
		except ValueError:
			print("[Error] The entered value must be an integer between 1 to 4")
		if (func_choice < 1 or func_choice > 4):
			print("[Error] The integer must be between 1 to 4")

	f = None
	file_name = ''

	while f == None:
		file_name = input("Enter the complete name file with its correct extension: ")
		try:		
			f = open(file_name, 'r')
		except FileNotFoundError:
			print("[Error] Cannot open", file_name)

	## !! TO-DO: VALIDATE THE FILE FORMAT IN YXZ FORMAT
	# Y is negative
	# X is positive
	# f = open(file_name,'r')
	is_file_valid = True
	for line in f:
		tokens = line.split()
		if len(tokens) != 3:
			print('[Error] The file content format is not valid. Should be in YXZ format')
			is_file_valid = False
			break
		else:
			try:
				y = float(tokens[0])
				x = float(tokens[1])
				h = float(tokens[2])
			except ValueError:
				print('[Error] The file is in the wrong format')
				is_file_valid = False
				break


	f.close()

	if is_file_valid:
		if func_choice == 1:
			print("\nFunctionality Level 1")
			print("=====================")
			
			mean_vertical_spacing = -1.0
			while mean_vertical_spacing <= 0.0:
				try:
					mean_vertical_spacing = float(input('Enter the correct mean VERTICAL spacing value for ' + file_name + ':\n'))
				except ValueError:
					print('[Error] The entered value must be of type float')

				
			# print(mean_vertical_spacing)
			mean_horizontal_spacing = -1.0
			while mean_horizontal_spacing <= 0.0:
				try:
					mean_horizontal_spacing = float(input('Enter the correct mean HORIZONTAL spacing value: '))
				except ValueError:
					print('[Error] The entered value must be of type float')

			sea_height = -1.0
			while sea_height < 0.0:
				try:
					sea_height = float(input('Enter the desired sea height level: '))
				except ValueError:
					print('[Error] The entered value must be of type float')
			
			(area,percent) = f1(file_name,mean_vertical_spacing * mean_horizontal_spacing,sea_height)
			print("\nAnswer:\nat sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(sea_height, area, percent))
		        
		elif func_choice == 2:
			print("\nFunctionality Level 2")
			print("=====================")

			mean_vertical_spacing = -1.0
			while mean_vertical_spacing <= 0.0:
				try:
					mean_vertical_spacing = float(input('Enter the correct mean VERTICAL spacing value for ' + file_name + ':\n'))
				except ValueError:
					print('[Error] The entered value must be of type float')

				
			# print(mean_vertical_spacing)
			mean_horizontal_spacing = -1.0
			while mean_horizontal_spacing <= 0.0:
				try:
					mean_horizontal_spacing = float(input('Enter the correct mean HORIZONTAL spacing value: '))
				except ValueError:
					print('[Error] The entered value must be of type float')

			interval = -1
			while interval < 0:
				try:
					interval = int(input('Enter the desired interval (e.g. 10. For default, enter 0):\n'))		
				except ValueError:
					print('[Error] The entered value must be of type int')
			if interval == 0:
				interval = 100


			print('\nAnswer')
			f2(file_name, mean_vertical_spacing*mean_horizontal_spacing, float(1/interval))

		# functionality 3
		elif func_choice == 3:
			print("\nFunctionality Level 3")
			print("=====================")

			parameter_choice = ''
			while parameter_choice == '':
				parameter_choice = input('Choose the desired parameter to set (h = to set sea height; i = to set interval; d = default): ')

				parameter_choice = parameter_choice.lower()
				if parameter_choice == 'd':
					print('\nAnswer')
					f3(file_name)
				elif parameter_choice == 'h':
					sea_height = -1.0
					while sea_height < 0.0:
						try:
							sea_height = float(input('Enter the desired sea height level: '))
						except ValueError:
							print('[Error] The entered value must be of type float')

					print('\nAnswer:')
					f3(file_name,sea_height)
				elif parameter_choice == 'i':
					inter = -1
					while inter < 0:
						try:
							inter = int(input('Enter the desired interval (e.g. 10. For default, enter 0):\n'))		
						except ValueError:
							print('[Error] The entered value must be of type int')
					
					if inter == 0:
						inter = 100
					print(inter)
					print('\nAnswer:')
					f3(file_name, height=-1, interval=float(1/inter))
				else:
					print('[Error] Input invalid')
					parameter_choice = ''

		elif func_choice == 4:
			print("\nFunctionality Level 4")
			print("=====================")

			parameter_choice = ''
			while parameter_choice == '':
				parameter_choice = input('Choose the desired parameter to set (h = to set sea height; i = to set interval; d = default): ')
				
				parameter_choice = parameter_choice.lower()
				display_image = False			

				if parameter_choice == 'h' or parameter_choice == 'i' or parameter_choice == 'd':
					image_choice = input('Do you want the image to be displayed [y/n]: ')
					if image_choice.lower() == 'y':
						display_image = True


				
				if parameter_choice == 'd':
					print('\nAnswer')
					if display_image:
						f4i(file_name)
					else:
						f4(file_name)
				elif parameter_choice == 'h':
					sea_height = -1.0
					while sea_height < 0.0:
						try:
							sea_height = float(input('Enter the desired sea height level: '))
						except ValueError:
							print('[Error] The entered value must be of type float')

					print('\nAnswer:')
					if display_image:
						f4i(file_name,sea_height)
					else:
						f4(file_name,sea_height)
				elif parameter_choice == 'i':
					inter = -1
					while inter < 0:
						try:
							inter = int(input('Enter the desired interval (e.g. 10. For default, enter 0):\n'))		
						except ValueError:
							print('[Error] The entered value must be of type int')
					
					if inter == 0:
						inter = 100
					print(inter)
					print('\nAnswer:')
					if display_image:
						f4i(file_name, height=-1, interval=float(1/inter))
					else:
						f4(file_name, height=-1, interval=float(1/inter))

				else:
					print('[Error] Input invalid')
					parameter_choice = ''


	else:
		print('[FileError] File is invalid. Program terminated.')

