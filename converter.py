import re

class Converter:

	def jessConverter(self, histoireLine):

		matchObj = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M|re.I)

		if matchObj:
		   who =  matchObj.group(2)
		   is_what = matchObj.group(1)


		print (histoireLine)