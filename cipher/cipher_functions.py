# Importing libraries for random integer generation and punctuation management.
from random import randint
import re

# Function to perform encryption by converting text to ASCII values and 
# changing the ASCII value by the random integer generated. Random int is
# printed so the user can decrypt the encrypted output.
def encryption(number_list, encrypted_list):
	active = True
	while(active):

		encrypt = input("\nPlease enter the message you would like to encrypt:" 
			+ "\n")
		encrypt_list = list(encrypt)
		
		if encrypt == '':
			active = False
			# this 'flag' allows user to exit

		else:
			rotation = input("Please enter the rotation value (1-25).\n"
				+ "(Press enter for random rotation)\n" + ">>>")
			# storing the rotation value and giving option for random rotation
			if rotation == '':
				rotation = randint(1,25)
				print("Random rotation is: " + str(rotation))
			else:
				rotation = int(rotation)

			# Performing the encryption using ASCII values:	
			for letter in encrypt_list:
				# for capital letters between ASCII value 65-90
				if ord(letter) >= 65 and ord(letter) <= 90:
					if ord(letter) + rotation > 90:
						changed = ord(letter) - 26 + rotation
						number_list.append(changed)
					else:
						changed = ord(letter) + rotation
						number_list.append(changed)

				elif ord(letter) >= 97 and ord(letter) <= 122:
					# converting lowercase (97-122) to UPPER case
					if ord(letter) + rotation > 122:
						changed = ord(letter) - 26 + rotation - 32
						number_list.append(changed)
					else:
						changed = ord(letter) + rotation - 32
						number_list.append(changed)

				# Ensure non-letters (i.e., punctuation) is unchanged
				else:
					number_list.append(ord(letter))
			
			# converting ASCII values back from numbers to letters	
			for number in number_list:
				encrypted_list.append(chr(number))

			# compiling encrypted_list back into a string for output
			encrypted = ''.join(encrypted_list)
			print("\n" + encrypted + "\n")

			# Perform analysis on original unencrypted text
			analysis(encrypt)

			active = False


# Function to perform decryption by converting encrypted text to ASCII values 
# changing the ASCII value by the input integer. If the input integer matches
# the integer used in the encryption, the text will be decrypted.
def decryption(number_list, decrypted_list):
	# Inverse functional logic compared to 'encryption' function
	active = True
	while(active):

		decrypt = input("\nPlease enter the message you would like to decrypt:"
			+ "\n")
		decrypt_list = list(decrypt)

		if decrypt == '':
			active = False

		else:
			rotation = input("Please enter the rotation value.\n"
				+ "(Press Enter for random rotation)\n" + "->")
			if rotation == '':
				rotation = randint(1,25)
				print("Random rotation is: " + str(rotation))
			else:
				rotation = int(rotation)
			for letter in decrypt_list:
				if ord(letter) >= 65 and ord(letter) <= 90:
					if ord(letter) - rotation < 65:
						changed = ord(letter) - rotation + 26
						number_list.append(changed)
					else:
						changed = ord(letter) - rotation
						number_list.append(changed)
				elif ord(letter) >= 97 and ord(letter) <= 122:
					if ord(letter) - rotation < 97:
						changed = ord(letter) - rotation - 32 + 26
						number_list.append(changed)
					else:
						changed = ord(letter) - rotation - 32
						number_list.append(changed)
				else:
					changed = ord(letter)
					number_list.append(changed)

			for number in number_list:
				changed_back = chr(number)
				decrypted_list.append(changed_back)

			decrypted = ''.join(decrypted_list)
			print("\n" + decrypted + "\n")

			# Perform analysis on the decrypted output text
			analysis(decrypted)

			active = False


# Using the 're' library to extract punction in text
def remove_punc(text):
	return re.compile('\w+').findall(text)


# analysis function to output: number of words, number of unique words, 
# shortest word length, longest word length
def analysis(result):
	result_list = remove_punc(result)

	text_length = len(result_list)
	unique_words = len(set(result_list))
	short_word = min_length(result_list)
	long_word = max_length(result_list)
	one_word = common_word(result_list)
	one_letter = common_letter(result_list)

	print("Number of words: " + str(text_length) + 
		"\nNumber of unique words: " + str(unique_words) +
		"\nShortest word has " + str(short_word) + " letters." +
		"\nLongest word has " + str(long_word) + " letters." +
		"\nMost common word: \n" + str(one_word) +
		"\nMost common letter: \n" + str(one_letter))
	

	write_to_file(text_length, unique_words, short_word, long_word, one_word,
		one_letter)


# Function to determine the length of the shortest word
def min_length(list1):

	min = sorted(list1, key=len)
	shortest = min[0]
	shortest_value = len(shortest)
	return shortest_value


# Function to determine length of the longest word
def max_length(list2):

	max = sorted(list2, key=len, reverse=True)
	longest = max[0]
	longest_value = len(longest)
	return longest_value


# Function to print the 10 most common words
def common_word(list3):

	counts = dict()
	for word in list3:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1

	store = list()
	for key, value in list(counts.items()):
	    store.append((value, key))

	store.sort(reverse=True)

	for key, value in store[:1]:
	    return(str(value) + " (" + str(key) + ")")


# Function for finding most common letter
def common_letter(text1):

	text2 = ''.join(text1)
	counts = dict()

	for letter in text2:
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1

	store = list()
	for key, value in list(counts.items()):
		store.append((value, key))

	store.sort(reverse=True)

	for key, value in store[:1]:
		return(str(value) + " (" + str(key) + ")")

# Function to output analysis to file metrics.txt
def write_to_file(length, unique, min_, max_, com_word, com_letter):

	with open('metrics.txt', 'w') as m:
		m.write("Words in text: " + str(length) +
    	"\nNumber of unique words in text: " + str(unique) +
    	"\nLength of shortest word: " + str(min_) + "\nLength of longest word: " 
    	+ str(max_) + "\nMost common word: \n" + str(com_word) + 
		"\nMost common letter: \n" + str(com_letter))
