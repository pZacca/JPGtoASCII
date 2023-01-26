from PIL import Image

# Open image file
image = Image.open("image3.jpg")

# Resize image to desired size
image = image.resize((80, 60), Image.ANTIALIAS)

# Convert image to grayscale
image = image.convert("L")

# Define more ASCII characters for grayscale values
ASCII_CHARS = ["@", "#", "S", "&", "%", "?", "*", "+", ";", ":", ",","."," ","-","_","^","`","'","~","(",")","[","]","{","}", "|", "\\","/"]

# Create a list of ASCII characters from grayscale values
ascii_image = list(map(lambda x: ASCII_CHARS[x//(256//len(ASCII_CHARS))], list(image.getdata())))


# Print the ASCII image
for i in range(0, len(ascii_image), 80):
    print("".join(ascii_image[i:i+80]))