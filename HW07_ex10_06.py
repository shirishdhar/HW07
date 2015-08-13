# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def sort(item,list_):
	while list_.index(item)<(len(list_)-1):
		if list_[list_.index(item)+1]>=list_[list_.index(item)]:   #Ignores last element to preserve range
			return True
		else:
			return False

def is_sorted(list_):
	return [sort(item,list_) for item in list_]

def main():
	a=is_sorted([1,3,5,7,20])
	if False in a[:-1]:				
		print False
	else:
		print True

main()

