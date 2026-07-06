from cryptography.fernet import Fernet
from PIL import Image
import numpy as np
import random
import base64
from pathlib import Path


def extract():
    inputimage = input("Image file path name here----->").strip('"')
    filepath = Path(inputimage)

    if filepath.exists():
        image = Image.open(inputimage).convert("RGB")
        matrix_image = np.array(image)
        flat_image = matrix_image.flatten()
        generatedkey = Fernet.generate_key()

        cipher = Fernet(generatedkey)
        messege_byUser = str(input("Type your messege here---->")).encode()
        encrypted_messege = cipher.encrypt(messege_byUser)
        binary_bytes = base64.urlsafe_b64decode(encrypted_messege)
        binary_string = "".join(f"{b:08b}" for b in binary_bytes)

        a = []  # {
        count = ""
        for i in str(len(binary_string)):  # combined key generation
            a.append(int(i))
        for i in a:
            count += chr(i)
        combinedkey = str(generatedkey) + count  # }

        Seed = int.from_bytes(combinedkey.encode("utf-8"), "big")
        random.seed(Seed)
        spots_generated = random.sample(range(len(flat_image)), len(binary_string))

        for spot, bit_in_string in zip(spots_generated, binary_string):
            spot_in_image = spot
            bit = int(bit_in_string)
            pixel_value = int(flat_image[spot_in_image])

            if bit == 0:
                modified_number = pixel_value & ~1

            if bit == 1:
                modified_number = pixel_value | 1

            flat_image[spot_in_image] = np.uint8(modified_number)

        copy_flat = flat_image.copy()

        reshaped_image = copy_flat.reshape(matrix_image.shape)
        filename = input("Enter the filename (with .png extension): ")
        img = Image.fromarray(reshaped_image, "RGB")
        img.save(filename)
        print(
            """ 
		SAVE THIS KEY FOR FURTHER EXTRACTING PROCESS
		""",
            base64.urlsafe_b64encode(combinedkey.encode("utf-8")).decode("utf-8"),
        )
    else:
        print("SUCH FILE PATH DOES NOT EXISTS ")


def decrypt():
    inputimage = input("Image file path name here----->").strip('"')
    filepath = Path(inputimage)
    if filepath.exists():
        key = input("ENTER KEY -->")
        image = Image.open(inputimage).convert("RGB")
        matrix_image = np.array(image)
        flat_image = matrix_image.flatten()
        decode_bytes = base64.urlsafe_b64decode(key)
        a = decode_bytes[:47]
        b = decode_bytes[47:]
        generatedkey = a.decode("utf-8")
        lenght = ""
        for i in b:
            lenght += str(i)
        lenght = int(lenght)
        Seed = int.from_bytes(decode_bytes)
        random.seed(Seed)
        spots_generated = []
        spots_generated = random.sample(range(len(flat_image)), lenght)
        binary_string = ""
        values = []
        for i in spots_generated:
            lsb = flat_image[i] & 1
            binary_string += str(lsb)
            values.append(flat_image[i])

        integer_binaryString = int(binary_string, 2)
        binary_string_bytes = integer_binaryString.to_bytes(
            (len(binary_string) + 7) // 8, "big"
        )
        encrypted_messege = base64.urlsafe_b64encode(binary_string_bytes)
        cipher = Fernet(generatedkey.strip("b'").encode())
        print("````````````````````````````````````````````````")
        print(cipher.decrypt(encrypted_messege).decode("utf-8"))
    else:
        print("SUCH FILE NOT EXISTS ")


match int(
    input("""
TYPE:
      
0:FOR HIDE
1:FOR RETRIVE
      
""")
):
    case 0:
        extract()
    case 1:
        decrypt()
    case _:
        print("Invalid choice")
