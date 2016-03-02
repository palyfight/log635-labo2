import re

class Converter:

	def jessConverter(self, histoireLine):

		matchObj = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M|re.I)
		if matchObj:
		   who =  matchObj.group(1)
		   is_what = matchObj.group(2)
		fact = "(" + who + " est un " + is_what + ")"

		print (fact)