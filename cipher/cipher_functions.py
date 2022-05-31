from random import randint
import re
# Importing external libraries to be used for random integer and to remove punct
# -uation


# This function performs the encryption. It uses other functions defined in
# this module to perform the other specific requirements. It takes the encryptio
# -n input and converts to ASCII values, performs sum to encrypt and then return
# -s encrypted value.
def encryption(number_list, encrypted_list):
	active = True
	while(active):

		encrypt = input("\nPlease enter the message you would like to encrypt:" 
			+ "\n")
		encrypt_list = list(encrypt)
		
		if encrypt == '-':
			active = False
			# this 'flag' allows user to exit

		else:
			rotation = input("Please enter the rotation value.\n"
				+ "(enter ' ' for random rotation)\n" + "->")
			# storing the rotation value and giving option for random rotation
			if rotation == ' ':
				rotation = randint(1,25)
				print("Random rotation is: " + str(rotation))
			else:
				rotation = int(rotation)

			# calculating the encryption using ASCII values:	
			for letter in encrypt_list:
				# for capital letters between 65-90
				if ord(letter) >= 65 and ord(letter) <= 90:
					if ord(letter) + rotation > 90:
						changed = ord(letter) - 26 + rotation
						number_list.append(changed)
					else:
						changed = ord(letter) + rotation
						number_list.append(changed)

				elif ord(letter) >= 97 and ord(letter) <= 122:
					# converting lowercase (97-122) to UPPER case as required 
					# in spec.
					if ord(letter) + rotation > 122:
						changed = ord(letter) - 26 + rotation - 32
						number_list.append(changed)
					else:
						changed = ord(letter) + rotation - 32
						number_list.append(changed)

				# following conditional maintains that punctuation are unchanged
				else:
					changed = ord(letter)
					number_list.append(changed)
			
			# converting ASCII values back to letters	
			for number in number_list:
				changed_back = chr(number)
				encrypted_list.append(changed_back)

			# compiling encrypted_list back into a string for output
			encrypted = ''.join(encrypted_list)
			print("\n" + encrypted + "\n")

			# result argument initialised as original (english) input so it 
			# can perform analysis on original text
			analysis(result=encrypt)

			active = False


# This function performs the decryption. It takes the decryption input and conv
# -erts to ASCII values, performs sum to decrypt and then returns encrypted valu
# -e.
def decryption(number_list, decrypted_list):
	active = True
	while(active):

		decrypt = input("\nPlease enter the message you would like to decrypt:"
			+ "\n")
		decrypt_list = list(decrypt)

		if decrypt == '-':
			active = False

		else:
			rotation = input("Please enter the rotation value.\n"
				+ "(enter ' ' for random rotation)\n" + "->")
			if rotation == ' ':
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

			# this time result is initialised as the decrypted output (english 
			# text)
			analysis(result=decrypted)

			active = False


# this function uses the 're' imported library to extract punctuation, idea to
# use this function was found on stackexchange
def remove_punc(text):
	return re.compile('\w+').findall(text)


# analysis function performs the analytic tasks required and is called to
# encryption and decryption functions. 
def analysis(result):
	result_list = remove_punc(text=result)

	text_length = len(result_list)
	print("Number of words: " + str(text_length))

	unique_words = len(set(result_list))
	print("Number of unique words: " + str(unique_words))

	short_word = min_length(list1=result_list)
	print("Shortest word has " + str(short_word) + " letters.")

	long_word = max_length(list2=result_list)
	print("Longest word has " + str(long_word) + " letters.")

	write_to_file(length=text_length, unique=unique_words, min_=short_word,
		max_=long_word)

	ten_common(list3=result_list)

	common_letter(text1=result_list)




	

# this function returns the length of the shortest word and is called in analysi
# -s
def min_length(list1):

	min = sorted(list1, key=len)
	shortest = min[0]
	shortest_value = len(shortest)
	return shortest_value


# this function returns the length of the longest word
def max_length(list2):

	max = sorted(list2, key=len, reverse=True)
	longest = max[0]
	longest_value = len(longest)
	return longest_value


# this function writes the stats to file metrics.txt
def write_to_file(length, unique, min_, max_):

	with open('metrics.txt', 'w') as m:
		m.write("Words in text: " + str(length) +
    	"\nNumber of unique words in text: " + str(unique) +
    	"\nLength of shortest word: " + str(min_) + "\nLength of longest word: " 
    	+ str(max_))


# function to print the 10 most common words, making value-key tuples and then
# printing in order using sort
def ten_common(list3):

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

	for key, value in store[:10]:
	    print(str(value) + ": " + str(key))


# function for finding most common letter, using same logic as ten_common

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
		print(str(value) + ": " + str(key))


	











	
	























