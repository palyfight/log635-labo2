class JessWriter:

	def writeFile(self, fileContent):

		file = open('facts.clp', 'w')

		file.write("(clear) \n")

		file.write("(deffacts history-facts \n")

		file.write(fileContent)

		file.write(") \n")

		file.write("(run)")

		file.close()
		
		return ("done")