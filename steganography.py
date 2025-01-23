import numpy as np

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    message += "###"  # End-of-message marker
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_index = 0

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                if message_index < len(binary_message):
                    pixels[i, j, k] = pixels[i, j, k] & ~1 | int(binary_message[message_index])
                    message_index += 1
                else:
                    break

    encoded_img = Image.fromarray(pixels)
    encoded_img.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    binary_message = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                binary_message += str(pixels[i, j, k] & 1)
                if len(binary_message) % 8 == 0:
                    char = chr(int(binary_message[-8:], 2))
                    if binary_message[-24:] == "".join(format(ord(c), '08b') for c in "###"):
                        return binary_message[:-24]

    return ""