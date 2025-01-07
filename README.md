Summary:
-------------
A calculator that supports mathematical operations given a single formatted string.

Install:
-------------
Windows:
- mkdir 
- cd 
- git clone [https://github.com/R365-SENG/Challenge_Calculator.git]

Usage:
-------------

The Calculator base class has several type-checking methods available, limiting number of inputs, the type of separators that can be used, and the input format itself. It also contains the addition method. 
The default checks conform to the restrictions of the first requirements, but can be overridden. An child instance of the class will be created in its own file for each requirement, so execution can be checked based on evolving requirements at each stage of the project. Each child class retains the functionality of the previous requirement unless doing so would directly conflict with the new requirement.
Execute each file using:

path/to/python3.exe "Path/to/Challenge/first_requirement.py"

_______________________________________________________________________________________________________________________________________________

To Do:
----------
 - Requirements 7 and 8

Evaluation:
----------
 - Completed challenge steps have a "+" sign to their left. Anything left on the list with a "-" is not yet implemented.

_______________________________________________________________________________________________________________________________________________


Challenge Notes:
-------------
    Provide code via a public distributed version control repository i.e. GitHub. Do NOT fork this repo
    Console application using the language defined by your interviewer
    Include unit tests
    Show each requirement step as a separate commit. Think of each step as a "requirement change"
    Efficient code is always important but for this excercise... readability and separation of concerns are much more critical
    Excluding stretch goals will not affect your overall assessment but implementing them poorly will

_______________________________________________________________________________________________________________________________________________

Requirements:
-------------

+    1.  Support a maximum of 2 numbers using a comma delimiter. Throw an exception when more than 2 numbers are provided
        examples: 20 will return 20; 1,5000 will return 5001; 4,-3 will return 1
        empty input or missing numbers should be converted to 0
        invalid numbers should be converted to 0 e.g. 5,tytyt will return 5

+    2. Remove the maximum constraint for numbers e.g. 1,2,3,4,5,6,7,8,9,10,11,12 will return 78

+    3. Support a newline character as an alternative delimiter e.g. 1\n2,3 will return 6

+    4. Deny negative numbers by throwing an exception that includes all of the negative numbers provided

+    5. Make any value greater than 1000 an invalid number e.g. 2,1001,6 will return 8
    
+    6. Support 1 custom delimiter of a single character using the format: //{delimiter}\n{numbers}
        - examples: //#\n2#5 will return 7; //,\n2,ff,100 will return 102
        - all previous formats should also be supported
-    7. Support 1 custom delimiter of any length using the format: //[{delimiter}]\n{numbers}
        - example: //[***]\n11***22***33 will return 66
        - all previous formats should also be supported
-    8. Support multiple delimiters of any length using the format: //[{delimiter1}][{delimiter2}]...\n{numbers}
        - example: //[*][!!][r9r]\n11r9r22*hh*33!!44 will return 110
        - all previous formats should also be supported

______________________________________________________________________________________________________________________________________________

Stretch Goals:
--------------

+    1. Display the formula used to calculate the result e.g. 2,,4,rrrr,1001,6 will return 2+0+4+0+0+6 = 12
-    2. Allow the application to process entered entries until Ctrl+C is used
-    4. Allow the acceptance of arguments to define...
-        alternate delimiter in step #3
-        toggle whether to deny negative numbers in step #4
-        upper bound in step #5
-    5. Use DI
-    6. Support subtraction, multiplication, and division operations
