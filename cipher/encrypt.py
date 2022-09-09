from cipher_functions import encryption, decryption
# imports the encryption and decryption defined in cipher_functions.py 
# file

print("\nThis program will encrypt/decrypt input messages.")
print("Enter 'exit' to exit the program.")

# looping the option to encrypt or decrypt until user chooses to exit
while(True):
	ask = input("\nWould you like to encrypt or decrypt?\n" + 
		"(Enter 'encrypt' or 'decrypt')\n")
	if ask == 'exit':
		break
	elif ask == 'encrypt':
		# arguments number_list, encrypted_list and decrypted_list store the
		# ASCII values for rotation, and the output values respectively.
		encryption(number_list=[], encrypted_list=[])
	elif ask == 'decrypt':
		decryption(number_list=[], decrypted_list=[])
