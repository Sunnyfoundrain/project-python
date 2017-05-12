

#index
print "\t\t\t+++  APP EDIT FILE :D  +++\n"
print "\t\t\t   +++  by Crack  +++\n\n"
print "\t\t------------------------------------------\n\n"

#set name file
setnamefile = raw_input("Your file name :\n > ")
print "\n\n"

# # # # # # # # # xac nhan tao file hoac exit file
# # # # # # # # # writepath = 'C:\Users\crack\Desktop\Project Py\learnpython/%s' %setnamefile


#open file
textfile = open(setnamefile, 'w')

#import data from keyboard
text = raw_input(">> ")


input01 = input("\n\n+++\tI. Read text ( 1 ) or close and save txt (2) \n\t> ")
if ( input01 == 1 ):
	print text
else:
	textfile.write(text)
	textfile.close
	
input02 = input("\n\n+++\tII. Do you want read file ? ( 1) \n\t> ")
if (input02 == 1):
	textfile = open(setnamefile, 'r')
	print "\n+++\tRead again file : \n"
	print textfile.read()
	while True:
		for i in ["/","-","|","\\","|"] :
			print "%s\r" %i,
else: 
	while True:
		for i in ["/","-","|","\\","|"] :
			print "%s\r" %i,

