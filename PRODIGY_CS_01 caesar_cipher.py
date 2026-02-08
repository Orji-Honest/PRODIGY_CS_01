"""
Task-01: Caesar Cipher Encryption/Decryption Tool
A Python program that encrypts and decrypts text using the Caesar Cipher algorithm.
"""

def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar cipher with given shift value.
    
    Args:
        text (str): The message to encrypt
        shift (int): Number of positions to shift (0-25)
    
    Returns:
        str: Encrypted message
    """
    result = ""
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypts text using Caesar cipher with given shift value.
    
    Args:
        text (str): The message to decrypt
        shift (int): Number of positions to shift (0-25)
    
    Returns:
        str: Decrypted message
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def main():
    """Main function to run the Caesar Cipher program."""
    print("="*50)
    print("CAESAR CIPHER ENCRYPTION/DECRYPTION TOOL")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            shift = int(input("Enter shift value (0-25): "))
            
            # Normalize shift to 0-25 range
            shift = shift % 26
            
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal Message: {message}")
            print(f"Shift Value: {shift}")
            print(f"Encrypted Message: {encrypted}")
            
        elif choice == '2':
            message = input("\nEnter the message to decrypt: ")
            shift = int(input("Enter shift value (0-25): "))
            
            # Normalize shift to 0-25 range
            shift = shift % 26
            
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted Message: {message}")
            print(f"Shift Value: {shift}")
            print(f"Decrypted Message: {decrypted}")
            
        elif choice == '3':
            print("\nThank you for using Caesar Cipher Tool!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
