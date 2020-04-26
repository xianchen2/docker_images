
from sys import argv
from src.api import get_data


if __name__ == '__main__':
	page_size = int(argv[1])
	num_pages = None
	output = None

	if len(argv) == 4:
		num_pages = int(argv[2])
		output = argv[3]

	elif len(argv) == 3:
		try:
			num_pages = int(argv[2])
		except:
			output = argv[2]

	
	get_data(page_size,num_pages,output)
	

