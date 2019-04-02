User documentation:
-------------------
1. The main program is calcmainprogram.py. It is the main interface to call the four
   functionality levels available.

   a. Functionality level 1: calculate the area above a certain sea level height using
                             the given mean vertical spacing & mean horizontal spacing values

   b. Functionality level 2: calculate the area above an interval of sea level heights 
                             and shows the graph related to the produced output using 
                             the given mean vertical spacing & mean horizontal spacing values
                             and the interval (default interval is 1% of the maximum sea level)

   c. Functionality level 3: calculate the area above a certain sea level identical to 1st and
                             2nd level functionalities using 1st and 2nd approximations 
   			                 described in the assignment specifications.

   d. Functionality level 4: identical to functionality level 3 and, additionally, it produces the number of
                             distinct island separated by sea / water.


2. There are a couple of ways to start the program. For a user-friendly command line interface,
   invoke the calmainprogram.py (i.e. python3 calcmainprogram.py) in the terminal. From that
   point, user can choose the functionality levels and test the program.

   a. First, users choose the desired functionality level, betweeen 1-4 (inclusive).

   b. Second, users choose the desired file to read.

   c. Based on the chosen functionality level in step (a), users will be asked to provide
   	  additional parameters (e.g. sea level height, interval, display image, etc).

   d. The program will then produce the output based on these given parameters.


3. For expert users, calcmainprogram.py can receive parameters from the command line and 
   immediately execute functionality level 4. The parameters are as follows:
   -f, --file     : to set the file name           (required data type: string)
   -l, --height   : to set the sea level height    (required data type: float)
   -i, --interval : to set the interval            (required data type: int)
   -m, --image    : to set a flag to display image (no value required)


4. For functionality level 4, if users choose to view the image and the given parameter is
   interval, users can loop through the produced images by clicking the current displayed image.
   (Be advised that the program takes longer to execute if the users choose to display the images.
   Furthermore, the functionality level 4 is the most complex one and, definitely, the nicest one
   we have!)


Required Libraries:
-------------------
- Python 3
- Matplotlib


Contributor:
------------
Edward Kopka
