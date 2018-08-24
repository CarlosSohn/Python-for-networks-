name = raw_input("Name: ")
print "Hello, " + name + ", and welcome to Pyg Translator"
original = raw_input("In order to see how it works, please, enter a word: ")
pyg = "py"

if original > 0 and original.isalpha():

	first = original[0]
	new_word = original + first + pyg
	new_word = new_word[1:len(new_word)]
	print new_word
	print "As you see, this little program puts the first letter of your word to the end and, aditionally, it is added the word 'py'"

else:
	print "You just needed to enter a word, please, try it later"
