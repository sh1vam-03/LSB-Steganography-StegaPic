# LSB-Steganography-StegaPic

# StegaPic

StegaPic is a command-line tool for image steganography, using Least Significant Bit (LSB) encoding to hide and extract messages or files in images. It provides a simple and secure way to embed and retrieve hidden data.

## Features

- **Hide Messages/Text**: Embed text messages into an image.
- **Hide Files**: (Not recommended) Embed files into an image.
- **Extract Messages/Text**: Retrieve hidden messages from an image.
- **Password Protection**: Optionally secure your hidden data with a password.

## Requirements

- Python 3.x
- Required Python modules:
  - `colorama`
  - `random`
  - `os`
  - `time`
  - `PIL` (Pillow)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sh1vam-03/LSB-Steganography-StegaPic.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LSB-Steganography-StegaPic
    ```

3. Install the required Python modules:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Tool**

    ```bash
    python StegaPic.py
    ```

2. **Options Menu**

   - **HIDE DATA**: Embed a message or file in an image.
     - **HIDE MESSAGE/TEXT**: Embed a text message.
     - **HIDE FILE**: Embed a file (not recommended).
   - **EXTRACT DATA**: Retrieve a hidden message from an image.
   - **QUIT & EXIT**: Exit the tool.

3. **Hiding Data**

   - Provide the path to the image.
   - Optionally enter a password.
   - Enter the message you want to hide.
   - Specify the name for the output image.

4. **Extracting Data**

   - Provide the path to the image containing the hidden message.
   - Optionally enter a password if the file was secured.
   - The hidden message will be displayed.


## Example Usage

### Hiding a Message in an Image

1. **Start the Tool**

   Launch the StegaPic tool from your terminal by navigating to the project directory and running:

    ```bash
    python stegapic.py
    ```

2. **Select the Option to Hide Data**

   When prompted, choose the option to hide data:

    ```bash
    Choose an option from the following:
        [1] HIDE DATA
        [2] EXTRACT DATA
        [0] QUIT & EXIT
    [+] Choose an Option -> 1
    ```

3. **Choose to Hide a Message/Text**

   You’ll be given further options to hide a message or a file. For this example, select to hide a text message:

    ```bash
    [*] HIDE DATA <Selected>

    Choose an option from the following:
        [1] HIDE MESSAGE/TEXT
        [2] HIDE FILE (Not Recommended)
        [0] QUIT & EXIT
    [+] Choose an Option -> 1
    ```

4. **Provide Image Path**

   Enter the path to the image where you want to hide the message. For example:

    ```bash
    [+] Image Path -> image.png
    ```

   The tool will then confirm that the image has been selected and will provide information about the image:

    ```bash
        [ALERT] Image Information
        Image Size: 512x512
        Total Pixels: 262144
        Based on the image size, you can hide up to 96.0KB data.
        Approximately 98304.0 characters.
    ```

5. **Enter a Password (Optional)**

   If you want to secure your hidden message with a password, you can enter it here. If not, simply press Enter:

    ```bash
    [+] Password (Optional) ->
    ```

6. **Type the Message to Hide**

   Enter the message you want to hide in the image. For example:

    ```bash
    [+] Message Box -> Hi, This is a hidden message.
    ```

   The tool will confirm that the message has been successfully hidden:

    ```bash
    Message Inserted...
    ```

7. **Specify Output Image Name**

   Enter a name for the output image. This is the image that will contain the hidden message. For example:

    ```bash
    [+] Output Image Name (Optional) -> StegaPic_image.png
    ```

   The tool will save the image with the hidden message and confirm the success:

    ```bash
    Message hidden successfully in the image!
    Output Image Location: StegaPic_image.png
    ```


### Extracting a Hidden Message from an Image

1. **Start the Tool**

   Again, start the StegaPic tool from your terminal.

2. **Select the Option to Extract Data**

   Choose the option to extract hidden data:

    ```bash
    Choose an option from the following:
        [1] HIDE DATA
        [2] EXTRACT DATA
        [0] QUIT & EXIT
    [+] Choose an Option -> 2
   ```

3. **Provide Image Path**

   Enter the path to the image from which you want to extract the hidden message:

    ```bash
    [+] Image Path -> StegaPic_image.png
    ```

4. **Enter Password (If Applicable)**

   If the image was secured with a password, enter it here. Otherwise, just press Enter:

    ```bash
    [+] Password (Optional) ->
    ```

5. **Retrieve the Hidden Message**

   The tool will process the image and display the hidden message:

    ```bash
    [\] Please wait! Depending on Image size it takes some time.

    Your hidden message:
    Hi, This is a hidden message.
    ```

By following these steps, you can easily hide and extract messages in images using StegaPic.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [sh1vam.03](https://github.com/sh1vam-03).
