# Variables
terms = {					# Dictionary for manipulating entries
	1: "-AppID: ",
	2: "-SteamName: ",
	3: "-GameFolder: ",
	4: "-SavePath1: ",
	5: "-SaveFolder1: ",
	6: "-ConfigPath1: ",
	7: "-ConfigFolder1: ",
	8: "-SavePath2: ",
	9: "-SaveFolder2: ",
	10: "-ConfigPath2: ",
	11: "-ConfigFolder2: ",
	12: "-SavePath3: ",
	13: "-SaveFolder3: ",
	14: "-ConfigPath3: ",
	15: "-ConfigFolder3: ",
}
term_num = 1				# Counter for terms
incomplete = False			# Boolean for knowing if an entry is incomplete
missingsave = False			# Boolean for knowing if an entry is missing a save
missingconfig = False		# Boolean for knowing if an entry is missing a config

# Open output files
db_output = open("db_output.csv", 'w')
log_output = open("log_output.txt", 'w')
list_output = open("list_output.txt", 'w')

# Start converting
with open("input.txt", 'r') as txt_input:								# Open the input file
	for line in txt_input:												# Iterate through each line
		if line != "\n":												# If current line is not a line break:
			line = line.replace(terms[term_num], "")					# Remove the substring
			line = line.replace("\n", "")								# Remove the line break

			# If term is the game's Steam name, separate the name for later use
			if term_num == 2:
				name = line
			
			# If entry is [UNKNOWN]:
			if line == "[UNKNOWN]":
				incomplete = True										# Mark entry as incomplete
				
				# Mark the related booleans if entry is missing save, config or both
				if term_num == 4 or term_num == 8 or term_num == 12:
					missingsave = True
				elif term_num == 6 or term_num == 10 or term_num == 14:
					missingconfig = True

			# If the last term was NOT reached yet, write to csv with a field separator "|" and go to next term
			if term_num != 15:
				db_output.write(line + "|")
				term_num += 1
			
			# If the last term was reached:
			elif term_num == 15:														
				db_output.write(line + "\n")							# Write to csv with a line break
				
				# Mark entry as incomplete in the changelog output if needed
				if incomplete == True:
					log_output.write("  - (incomplete) " + name + "\n")
				else:
					log_output.write("  - " + name + "\n")
				
				# Mark entry as missing save, config or both in the list output if needed
				if missingsave == True and missingconfig == False:
					list_output.write("* " + name + " (save)\n")
				elif missingsave == False and missingconfig == True:
					list_output.write("* " + name + " (config)\n")
				elif missingsave == True and missingconfig == True:
					list_output.write("* " + name + " (save and config)\n")
				
				# Reset everything for next entry
				term_num = 1
				incomplete = False
				missingsave = False
				missingconfig = False

# Close output files
db_output.close()
log_output.close()
list_output.close()
