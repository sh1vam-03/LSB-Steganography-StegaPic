# Import modules for tool designe and style
from colorama import Style, Fore
import random
import os
import time

# Import module for work with image and pixels
from PIL import Image

# Function to convert a message into a binary string
def message_to_binary(message):
  return ''.join(format(ord(char), '08b') for char in message)

# Function to convert a binary into a messsage string
def binary_to_message(binary):
    message = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return message

# Function to convert file data to binary string
def file_to_binary(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    return ''.join(format(byte, '08b') for byte in file_data)

def binary_to_file(binary_data, output_file_path):
    binary_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    file_data = bytes([int(byte, 2) for byte in binary_bytes])
    
    # Write binary data to output file
    with open(output_file_path, 'wb') as file:
        file.write(file_data)

# Function for hide message in image
def hide_message():
  print(line)
  print(Fore.LIGHTMAGENTA_EX + "[*] HIDE MESSAGE/TEXT"+ Style.RESET_ALL + Fore.LIGHTRED_EX + "\t\t<Selected>" + Style.RESET_ALL )

  # Get Image path from user
  print("\nPlease type or paste the image path below.")
  image_path = input(Fore.GREEN + Style.BRIGHT + "[+] Image Path -> " + Style.RESET_ALL)
  if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB format
    print("Image Selected...")
    print(line)
  else:
    print(Fore.RED + Style.BRIGHT + "Sorry... Something went wrong!\nPlease check the image path and try again." + Style.RESET_ALL)
    print(line)
    exit_from_tool()
  
  # Print image information
  print(Fore.RED + Style.BRIGHT + "[ALERT] Image Information\n" + Style.RESET_ALL)
  width, height = img.size
  total_pixels = width * height
  total_bits = total_pixels * 3
  total_bytes = total_bits / 8
  total_kb = total_bytes / 1024
  print(f"Image Size: {width}x{height}\nTotal Pixels: {total_pixels}\nBased on the image size, you can hide up to "+Fore.LIGHTBLUE_EX +  str(total_kb) +"KB" + Style.RESET_ALL + " data.\nApproximately "+Fore.LIGHTBLUE_EX +  str(total_bytes) + Style.RESET_ALL + " characters.")
  print(line)

  # Get password as a delimiter at the end of the message
  print("Please insert a password for security reason.\nIf you don't want to use a password, simply press Enter.")
  password = input(Fore.GREEN + Style.BRIGHT + "[+] Password (Optional) -> " + Style.RESET_ALL)

  # In case user cant insert password we can chose default delimiter at the end of the message
  if password.strip() == '':
    password = '$$' # use Default pass
  else:
    print("Password Inserted...")

  print(line)
  # Get message from user
  print("Please type or paste message/text hare that you want to hide on image.\nExample: (This is a secrect message)")
  message = input(Fore.GREEN + Style.BRIGHT + "[+] Message Box ->" + Style.RESET_ALL)
  if message.strip() == '':
    print(Fore.RED + Style.BRIGHT + "Sorry... Looks like you not inserted message!\nPlease insert a message and try again." + Style.RESET_ALL)
    print(line)
    exit_from_tool()
  else:
    print("Message Inserted...")
    print(line)
  
  identifier = "TEXT"
  # Create binary message
  binary_message = message_to_binary(identifier) + message_to_binary(message) + message_to_binary(password)

  # Ensure the binary message can fit into the image
  max_bits = img.size[0] * img.size[1] * 3  # 3 bits per pixel (R, G, B)
  if len(binary_message) > max_bits:
    raise ValueError(Fore.LIGHTRED_EX + "Message is too long to fit in the image.\nPlease insert high resolution image or short message.",line)

  # Access pixel data
  pixels = img.load()
  binary_message_idx = 0

  # Modify the LSB pixels in the image
  for i in range(img.size[0]):  # Loop through width
    for j in range(img.size[1]):  # Loop through height
      pixel = list(pixels[i, j])  # Get the pixel (tuple of RGB)

      for k in range(3):  # Modify R, G, B channels
        if binary_message_idx < len(binary_message):
          # Modify the least significant bit of the pixel's channel
          pixel[k] = pixel[k] & ~1 | int(binary_message[binary_message_idx])
          binary_message_idx += 1

        # Update the pixel with modified RGB values
        pixels[i, j] = tuple(pixel)

      # Break out if we've embedded the entire message
      if binary_message_idx >= len(binary_message):
        break
    if binary_message_idx >= len(binary_message):
      break
      
  # Save the modified image
  print("Please type the name of the output image.\nExamples: \nWith path: (path/image.jpg)\nWithout path: (image.jpg)")
  # print(Fore.LIGHTRED_EX + "Note: If you are not using Windows, you need to specify the name of the output image." + Style.RESET_ALL)

  output_image_name = input(Fore.GREEN + Style.BRIGHT + "[+] Output Image name (Optional) ->" + Style.RESET_ALL)
  if output_image_name.strip() == '':
    output_image_name = '/'.join(image_path.split('/')[:-1]) + "/Output_of_StegaPic_" + image_path.split('/')[-1]

  else:
    print("Output Image Name Inserted...")
  try:
  # Show message to task ix completed
    img.save(output_image_name)
    print(Fore.LIGHTCYAN_EX + "\nMessage hidden successfully in the image!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Output image Location : " + Style.RESET_ALL + output_image_name)
  except:
    print(Fore.RED + Style.BRIGHT + "\nSorry... Something went wrong!\nPlease Enter output image path and try again." + Style.RESET_ALL)
  print(line,"\n")

# Function for hide file in image
def hide_file():
  print(line)
  print(Fore.LIGHTMAGENTA_EX + "[*] HIDE FILE(Not Recomded)"+ Style.RESET_ALL + Fore.LIGHTRED_EX + "\t<Selected>" + Style.RESET_ALL )
  
  # Get Image path from user
  print("\nPlease type or paste the image path below.")
  image_path = input(Fore.GREEN + Style.BRIGHT + "[+] Image Path -> " + Style.RESET_ALL)
  if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB format
    print("Image Selected...")
    print(line)
  else:
    print(Fore.RED + Style.BRIGHT + "Sorry... Something went wrong!\nPlease check the image path and try again." + Style.RESET_ALL)
    print(line)
    exit_from_tool()
  
  # Print image information
  print(Fore.RED + Style.BRIGHT + "[ALERT] Image Information\n" + Style.RESET_ALL)
  width, height = img.size
  total_pixels = width * height
  total_bits = total_pixels * 3
  total_bytes = total_bits / 8
  total_kb = total_bytes / 1024
  print(f"Image Size: {width}x{height}\nTotal Pixels: {total_pixels}\nBased on the image size, you can hide up to "+Fore.LIGHTBLUE_EX +  str(total_kb) +"KB" + Style.RESET_ALL + " data on the image.\n")
  print(line)

  # Get password as a delimiter at the end of the message
  print("Please insert a password for security reason.\nIf you don't want to use a password, simply press Enter.")
  password = input(Fore.GREEN + Style.BRIGHT + "[+] Password (Optional) -> " + Style.RESET_ALL)

  # In case user cant insert password we can chose default delimiter at the end of the message
  if password.strip() == '':
    password = '$$' # use Default pass
  else:
    print("Password Inserted...")

  print(line)
  # Get message from user
  print("Please type or paste path of file that you want to hide on image.\nExample: (path/msg.txt)")
  file_path = input(Fore.GREEN + Style.BRIGHT + "[+] File path ->" + Style.RESET_ALL)
  if os.path.exists(file_path):
    binary_file = file_to_binary(file_path)
    print("file Selected...")
    print(line)
    print(Fore.RED + Style.BRIGHT + "[ALERT] File Information\n" + Style.RESET_ALL)
    print("File Size: " + str(os.path.getsize(file_path)),"Image able to contains data: "+str(total_kb)+"KB\n")
    identifier = 'FILE' 
    # Create binary message
    binary_message = message_to_binary(identifier) + binary_file + message_to_binary(password)
    # Ensure the binary message can fit into the image
    max_bits = img.size[0] * img.size[1] * 3  # 3 bits per pixel (R, G, B)
    if len(binary_message) > max_bits:
      raise ValueError(Fore.LIGHTRED_EX + "File size is too big to fit in the image.\nPlease insert high resolution image or short message.",line)
  else:
    print(Fore.RED + Style.BRIGHT + "Sorry... Something went wrong!\nPlease check the file path and try again." + Style.RESET_ALL)
    print(line)
    exit_from_tool()

  # Access pixel data
  pixels = img.load()
  binary_message_idx = 0

  # Modify the LSB pixels in the image
  for i in range(img.size[0]):  # Loop through width
    for j in range(img.size[1]):  # Loop through height
      pixel = list(pixels[i, j])  # Get the pixel (tuple of RGB)

      for k in range(3):  # Modify R, G, B channels
        if binary_message_idx < len(binary_message):
          # Modify the least significant bit of the pixel's channel
          pixel[k] = pixel[k] & ~1 | int(binary_message[binary_message_idx])
          binary_message_idx += 1

        # Update the pixel with modified RGB values
        pixels[i, j] = tuple(pixel)

      # Break out if we've embedded the entire message
      if binary_message_idx >= len(binary_message):
        break
    if binary_message_idx >= len(binary_message):
      break
      
  # Save the modified image
  print("Please type the name of the output image.\nExamples: \nWith path: (path/image.jpg)\nWithout path: (image.jpg)")
  # print(Fore.LIGHTRED_EX + "Note: If you are not using Windows, you need to specify the name of the output image." + Style.RESET_ALL)

  output_image_name = input(Fore.GREEN + Style.BRIGHT + "[+] Output Image name (Optional) ->" + Style.RESET_ALL)
  if output_image_name.strip() == '':
    output_image_name = '/'.join(image_path.split('/')[:-1]) + "/Output_of_StegaPic_" + image_path.split('/')[-1]
  else:
    print("Output Image Name Inserted...")
  # Show message to task ix completed
  print(Fore.LIGHTCYAN_EX + "\nFile hidden successfully in the image!" + Style.RESET_ALL)
  print(Fore.LIGHTBLUE_EX + "Output image Location : " + Style.RESET_ALL + output_image_name)
  img.save(output_image_name)
  print(line,"\n")

# Function can Hide data on image
def hide_data():
  print(line)
  print(Fore.LIGHTMAGENTA_EX + "[*] HIDE DATA"+ Style.RESET_ALL + Fore.LIGHTRED_EX + "\t\t\t<Selected>" + Style.RESET_ALL )
  print(Fore.LIGHTYELLOW_EX + "\nChoose an option from the following:" + Style.RESET_ALL)
  print("\t[1] HIDE MESSAGE/TEXT\n\t[2] HIDE FILE(Not Recomded)\n\t[0] QUITE & EXIT")
  try:
    message_or_file = int(input(Fore.GREEN + Style.BRIGHT + "[+] Chose an Option ->" + Style.RESET_ALL))
    if message_or_file == 1:
      hide_message()
    elif message_or_file == 2:
      hide_file()
    elif message_or_file == 0:
      exit_from_tool()
    else:
      print(Fore.RED + Style.BRIGHT + "\nInvalid option. Please choose 1 or 2.\r" + Style.RESET_ALL)
      hide_data()
  except:
    print(Fore.RED + Style.BRIGHT + "\nInvalid option. Please choose 1 or 2.\r" + Style.RESET_ALL)
    hide_data()

# Function can Extract hidden data from image
def extract_data():
  print(line)
  print(Fore.LIGHTMAGENTA_EX + "[*] EXTRACT DATA" + Style.RESET_ALL + Fore.LIGHTRED_EX + "\t\t<Selected>" + Style.RESET_ALL)
    
  # Get Image path from user
  print("\nPlease type or paste the image path that contains the secret message.")
  image_path = input(Fore.GREEN + Style.BRIGHT + "[+] Image Path -> " + Style.RESET_ALL)
    
  # Check if image path exists
  if os.path.exists(image_path):
    try:
      img = Image.open(image_path)
      img = img.convert("RGB")  # Ensure the image is in RGB format
      print("Image Selected...")
      print(line)
    except Exception as e:
      print(Fore.RED + "Failed to load the image. Please check the file format." + Style.RESET_ALL)
      print(f"Error: {e}")
      return
  else:
    print(Fore.RED + Style.BRIGHT + "Sorry... Something went wrong!\nPlease check the image path and try again." + Style.RESET_ALL)
    print(line)
    return
    
  # Get Password or delimiter from user if it is set
  print("Please insert a password if the file is secured with a password.\nIf no password is used, simply press Enter.")
  password = input(Fore.GREEN + Style.BRIGHT + "[+] Password (Optional) -> " + Style.RESET_ALL)
    
  # Use default delimiter if password not provided
  if password.strip() == '':
    password = '$$'  # use Default delimiter
  else:
    print("Password Inserted...")
    
  # Convert password into binary format
  binary_pass = message_to_binary(password)

  # Access pixel data
  pixels = img.load()
    
  # Collect binary message
  binary_message_or_file_more = ''
  start = 0

  for i in range(img.size[0]):
    load_list = ["-", "\\", "|", "/"]
    if start < 4 :
      print(f"\r[{load_list[start]}] Please wait! Depending on Image size it takes some time.", end="")
      start += 1
    else:
      start = 0
    for j in range(img.size[1]):
      pixel = list(pixels[i, j])
      for k in range(3):
        binary_message_or_file_more += str(pixel[k] & 1)

  # Find the delimiter (end of message) and slice it off
  if binary_pass in binary_message_or_file_more:
    binary_message_or_file = binary_message_or_file_more.split(binary_pass)[0]
    identifier_binary = binary_message_or_file[:32]
    identifier = binary_to_message(identifier_binary) 
    if identifier == "TEXT":
      message_binary = binary_message_or_file[32:]  # The rest is the message
      # Convert binary back to message
      hidden_message = binary_to_message(message_binary)
      print(Fore.LIGHTCYAN_EX + "\n\nYour hidden message:" + Style.RESET_ALL)
      print(hidden_message)
    elif identifier == "FILE":
      message_binary = binary_message_or_file[32:]  # The rest is the message
      # Save the File
      print(Fore.LIGHTRED_EX + "\n\nThe image contains a hidden file." + Style.RESET_ALL + "\nPlease type the name of the output file.\nExamples: \nWith path: (path/image.txt)\nWithout path: (image.txt)\nBy default, it will provide a .txt file.")
      output_file_name = input(Fore.GREEN + Style.BRIGHT + "[+] Output File name (Optional) ->" + Style.RESET_ALL)
      if output_file_name.strip() == '':
        img_name = image_path.split('/')[-1]
        output_file_name = '/'.join(image_path.split('/')[:-1]) + "/" + img_name.split('.')[0] + ".txt"
        print(output_file_name)
      else:
        print("Output File Name Inserted...")
      # Convert binary back to message file
      hidden_message = binary_to_file(message_binary, output_file_name)
      print(Fore.LIGHTCYAN_EX+f"\nHidden file extracted and saved as {output_file_name}"+Style.RESET_ALL)
    else:
      print(Fore.RED + "\n\nSorry... something went wrong! \nIt looks like the image can't store any secret data.\nPlease insert a correct image and try again." + Style.RESET_ALL)
  else:
    print(Fore.RED + "\n\nSorry... something went wrong! \nThe correct password is required for the image.\nPlease enter the correct password and try again." + Style.RESET_ALL)
  print(line,"\n")

# Chose Option Hide and Extract data from image
def hide_extract():
    print(line)
    print(Fore.LIGHTYELLOW_EX + "Choose an option from the following:" + Style.RESET_ALL)
    print("\t[1] HIDE DATA\n\t[2] EXTRACT DATA\n\t[0] QUITE & EXIT")
    try:
      hide_and_extract = int(input(Fore.GREEN + Style.BRIGHT + "[+] Chose an Option ->" + Style.RESET_ALL))
      if hide_and_extract == 1:
        hide_data()
      elif hide_and_extract == 2:
        extract_data()
      elif hide_and_extract == 0:
        exit_from_tool()
      else:
        print(Fore.RED + Style.BRIGHT + "\nInvalid option. Please choose 1 or 2.\r" + Style.RESET_ALL)
        hide_extract()
    except:
      print(Fore.RED + Style.BRIGHT + "\nInvalid option. Please choose 1 or 2.\r" + Style.RESET_ALL)
      hide_extract()

# Exit from tool function
def exit_from_tool():
# Simple Exit Loading Bar
    start = 0
    end = 60
    load = (Fore.GREEN + Style.BRIGHT + '='+ Style.RESET_ALL)
    unload = (Fore.RED + '_'+ Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "\nPlease wait while we are exiting the tool" + Style.RESET_ALL)
    while start <= 60:
        print("\r"+load*start+">"+unload*end,end="")
        print("\r\t\t\t"+load*4,start*2-20,"\r",end="")
        time.sleep(0.01)
        start += 1
        end -= 1
    print("\n\n")
    os._exit(0)

# Start
# Colors for designe banner of the tool
colors = [
    Fore.RED,     # Red
    Fore.BLUE,    # Blue
    Fore.MAGENTA, # Magenta
    Fore.CYAN,    # Cyan
]

# Chose a Random color for banner
random_color = random.choice(colors)
# For designe
line = "_"*61
# Tool Name
print(random_color + Style.BRIGHT + """
        ______                         ______ _
       / _____) _                     (_____ (_)
      ( (____ _| |_ _____  ____ _____  _____) )  ____ 
       (____ (_   _) ___ |/ _  (____ ||  ____/ |/ ___)
       _____) )| |_| ____( (_| / ___ || |    | ( (___ 
      (______/ |___)_____)<___ |_____||_|    |_|<____)
                           __| |""" + Style.RESET_ALL + "            -" + Fore.GREEN + Style.BRIGHT + 'sh1vam.03'+ Style.RESET_ALL+ random_color + """
                          (____|
""" + Style.RESET_ALL)
print(line)
print(Fore.CYAN + Style.NORMAL + "Welcome to StegaPic – Your Ultimate Image Steganography Tool!\nEasily hide and extract messages or files in images.\nSecure and simple to use!" + Style.RESET_ALL)

# call Hide_Extract function to chose one option
hide_extract()
