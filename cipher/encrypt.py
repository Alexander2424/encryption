from cipher_functions import encryption, decryption
# imports the encryption and decryption defined in encrypt_decrypt_func.py 
# module

print("\nThis program will encrypt/decrypt your messages.")
print("Enter '-' once you no longer want to encrypt/decrypt.")

# looping the option to encrypt or decrypt until user chooses to exit

while(True):
	ask = input("\nWould you like to encrypt or decrypt?\n" + 
		"(Enter 'encrypt' or 'decrypt')\n")
	if ask == '-':
		break
	elif ask == 'encrypt':
		# arguments number_list, encrypted_list[] and decrypted_list are initial
		# -ised as empty lists to store the ASCII numbers and to store the 
		# output values in a list
		encryption(number_list=[], encrypted_list=[])
	elif ask == 'decrypt':
		decryption(number_list=[], decrypted_list=[])



