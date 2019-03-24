import sys

def main():
    partial = sys.argv[1]	# 2nd argument is ISBN
    
    for x in range(11):
    	total = (int(partial[0]) * 5) + \
    			(int(partial[1]) * 4) + \
    			(int(partial[2]) * 3) + \
    			(int(partial[3]) * 2) + x
    	if total % 11 == 0:
    		if x == 10:
    			print("X")
    		else:
    			print x
    		break 
    
    
if __name__ == "__main__":
    main()
