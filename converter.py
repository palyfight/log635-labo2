import re

class Converter:

	def jessConverter(self, histoireLine):

		matchObj = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(1) + " est un " + matchObj.group(2) + ")")

		matchObj = re.match( r'etre\(([NOT,]*),([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if matchObj:
			print ("")

		matchObj = re.match(r'temps\((.*?)\) & loc\((.*?)\) & voir\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(4) + " vu " +   matchObj.group(3) + " au " +  matchObj.group(2) + " a " +  matchObj.group(1) + ")")


		matchObj = re.match(r'but\(devenir\((.*?)\)\) & prendre\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(3) + " prend " + matchObj.group(2) + " de " + matchObj.group(1) + ")")


		matchObj = re.match(r'avant_temps\((.*?)\) & loc\((.*?)\) & doit\(etre\((.*?)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(3) + " doit etre a " + matchObj.group(2) + " avant " + matchObj.group(1) + ")")
