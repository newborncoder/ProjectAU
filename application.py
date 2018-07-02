import sys


f = open(sys.argv[1],'r')
while True:
	line1 = f.readline()
	line2 = f.readline()
	line3 = f.readline()
	line4 = f.readline()

	print("")
	lenx = len(line1)

	if not line1: break

	for x in range(lenx):
		if(line1[x] == " " and line1[x+1] == "_"):
			if(line2[x]=="|" and line2[x+1]==" " and line3[x+2]=="|"):
				if(line3[x]=="|" and line3[x+1]=="_" and line3[x+2]=="|"):
					print("0"),

		if(line1[x] == " " and line1[x] == " " and line1[x] == " "):
			if(line2[x]==" " and line2[x+1]=="|" and line2[x+2]==" "):
				if(line3[x]==" " and line3[x+1]=="|" and line3[x+2]==" "):
					print("1"),

        	if(line1[x] == " " and line1[x+1] == "_"):
            		if(line2[x]==" " and line2[x+1]=="_" and line2[x+2]=="|"):
                		if(line3[x]=="|" and line3[x+1]=="_"):
                    			print("2"),

		if(line1[x] == " " and line1[x+1] == "_" and line1[x+2] == " "):
                        if(line2[x]==" " and line2[x+1]=="_" and line2[x+2]=="|"):
                                if(line3[x]==" " and line3[x+1]=="_" and line3[x+2]=="|"):
                                        print("3"),

		if(line1[x] == " " and line1[x] == " " and line1[x] == " "):
                        if(line2[x]=="|" and line2[x+1]=="_" and line2[x+2]=="|"):
                                if(line3[x]==" " and line3[x+1]=="|"):
                                        print("4"),

		if(line1[x] == " " and line1[x+1] == "_"):
                        if(line2[x]=="|" and line2[x+1]=="_" and line2[x+2] != "|"):
                                if(line3[x]==" " and line3[x+1]=="_" and line3[x+2]=="|"):
                                        print("5"),

		if(line1[x] == " " and line1[x+1] == "_"):
                        if(line2[x]=="|" and line2[x+1]=="_" and line2[x+2] != "|"):
                                if(line3[x]=="|" and line3[x+1]=="_" and line3[x+2]=="|"):
                                        print("6"),

		if(line1[x] == " " and line1[x+1] == "_"):
                        if(line2[x]==" " and line2[x+1]==" " and line2[x+2]=="|"):
                                if(line3[x]==" " and line3[x+1]==" " and line3[x+2]=="|"):
                                        print("7"),

		if(line1[x] == " " and line1[x+1] == "_"):
                        if(line2[x]=="|" and line2[x+1]=="_" and line2[x+2]=="|"):
                                if(line3[x]=="|" and line3[x+1]=="_" and line3[x+2]=="|"):
                                        print("8"),

		if(line1[x] == " " and line1[x+1] == "_"):
                        if(line2[x]=="|" and line2[x+1]=="_" and line2[x+2]=="|"):
                                if(line3[x]==" " and line3[x+1]=="_" and line3[x+2]=="|"):
                                        print("9"),
