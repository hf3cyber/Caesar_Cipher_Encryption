

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Perform Caesar Cipher encryption or decryption on the given text with the specified shift value.
    :param text: The text to be encrypted or decrypted.
    :param shift: The shift value to be used for encryption or decryption.
    :param mode: The mode of operation, either 'encrypt' or 'decrypt'.
    :return: The resulting text after encryption or decryption.
    """
    # Initialize the result variable
    result = ""

    # Normalize shift to be within 0-25 range
    shift = shift % 26

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result  # Return the final result 


def main():
    print("Welcome to the Caesar Cipher Program!")  # Display welcome message
    text = input("Enter the text: ") # Prompt user for text input

     # Ensure text input is not empty
    while not text:
        print("Text cannot be empty!")
        text = input("Enter the text: ").strip()


    # Ensure shift input is valid
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric shift value.")

    # Validate encryption mode with numeric input
    while True:
        mode_input = input("Enter 1 to encrypt or 2 to decrypt: ").strip()
        if mode_input == '1':
            mode = 'encrypt'
            break
        elif mode_input == '2':
            mode = 'decrypt'
            break
        print("Invalid choice! Please enter 1 for encrypt or 2 for decrypt.")

    # Perform Caesar Cipher
    result = caesar_cipher(text, shift, mode)

    # Print the result
    print(f"Result: {result}")
    
# Call the main function 
if __name__ == "__main__":   # Call the main function
    main()
