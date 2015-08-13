# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_):
	total=0
	try:
		for item in list_:
			if isinstance(item,list):
				total+=nested_sum(item)
			else:
				total+=item
		return total
	except:
		print "Only numerals accepted."

def main():
	#print nested_sum([1,3,[3],[6,8]])
	pass

if __name__=='__main__':
	main()

