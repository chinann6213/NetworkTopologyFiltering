"""
TSN2201 - Computer Networks Assignment: Network Topology Filtering
Tutorial Section: TT03 (Monday Group)
Name: NG CHIN ANN
Student ID: 1142701684
Email: chinann6213@gmail.com
Question 5.1: Write a program that will list all network configurations
              which has a max degree of 2. 
              (Where the max number of links connected to one node is 2)
"""
def getFulfilledTopology(files): 

	try:
		#Open input file
		with open(files, "r") as file:
			nodes = int(file.read(1)) + 1
			next(file)
			input = [line.split() for line in file]
	except:
		print "File name '" + files + "' does not exist."
		return 
	
	#Open output file
	outputFile = open(files + "_output.txt", "w")
	
	counter = 0
	fulfilled_counter = 0
	
	#Get the degree of each node
	for line in input:
		Nodearray = [0 for x in range(nodes)]
		for integer in line:
			Nodearray[int(integer) / 10] += 1
			Nodearray[int(integer) % 10] += 1
		#Get the topology with max degree of 2
		if all(element <= 2 for element in Nodearray):
			#Write the topology with max degree of 2 into the output file
			outputFile.write(' '.join(input[counter]) + "\n")
			fulfilled_counter += 1
		counter += 1

	print "Input file: " + files + "\nNumber of network topologies with max degree of 2:",
	print str(fulfilled_counter) + "\n" 
			
	outputFile.close()	

print "Running input file...\n"
getFulfilledTopology("5node6link.txt")
getFulfilledTopology("6node7link.txt")
getFulfilledTopology("6node8link.txt")
getFulfilledTopology("7node6link.txt")
print "**The output files are available in the project folder."

