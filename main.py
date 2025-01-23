from steganography import encode_message, decode_message

def main():
    print("Welcome to the Steganography Tool!")
    action = input("Do you want to (e)ncode or (d)ecode? ").lower()

    if action == 'e':
        image_path = input("Enter the path to the image: ")
        message = input("Enter the message to hide: ")
        output_path = input("Enter the output image path: ")
        encode_message(image_path, message, output_path)
    elif action == 'd':
        image_path = input("Enter the path to the encoded image: ")
        message = decode_message(image_path)
        print(f"Decoded Message: {message}")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()