#USERNAME AND DOMAIN NAME #FETCHER
#EMAIL SLICER
while 1:
	email=input("\nEnter Your Email : ")
	try:
	    if email.isdigit():
	    	 print ("Something went Wrong ")
	    else:
	    	 	usr=email[:email.index('@')]
	    	 	domain=email[email.index('@')+1:]
	    	 	print("UserName =",usr+"\nDomain = ",domain )
	except:
	    print("\nData In Invalid Format")


	


