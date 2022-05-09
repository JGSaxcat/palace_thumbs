
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Importing CSV handler
import csv


# Importing textwrap for handling long game / supplier names
import textwrap

# Importing os to handle file paths
import os

# Create dictionary from the game metadata CSV
filename = 'game_metadata.csv'
game_list = []
with open(filename) as file:
	for i in csv.DictReader(file):	
		game_list.append(dict(i))


# get the current directory as a global variable

current_dir = os.getcwd()

# A switch which allows the user to proceed with custom values or with the values as previously discussed

while True:
	customValuesPrompt = input("Do you wish to create thumbnails with custom fonts, locations and sizes? (enter Y/N): ")
	if customValuesPrompt.upper() not in ["Y", "N"]:
		print("Please answer using Y or N")
		continue
	else:
		break


# If user answers that they don't want custom values, these are the hardcoded values

if customValuesPrompt.upper() == 'N':
	
	gameNameCustomFont = 'NotoSans-Bold.ttf'
	gameNameVerticalPercentage = 78
	gameNameHorizontalPercentage = 50
	gameNameFontSize = 20

	supplierNameCustomFont = 'NotoSans-Bold.ttf'
	supplierNameVerticalPercentage = 94 
	supplierNameHorizontalPercentage = 50
	supplierNameFontSize = 12

# Otherwise prompts start here to capture the above variables

else:
	
	print("Enter your preferences for the game name\n")

	while True:
		gameNameCustomFont = input("Enter the name of the font you wish to use for the game name. Ensure it is saved in the 'fonts' folder and include the file extension (e.g. NotoSans-Bold.ttf): ")
		if os.path.exists(current_dir + '/fonts/' + gameNameCustomFont) == False:
			print("Font does not exist in /fonts/ folder. Please add this font to the folder or ensure you have typed its name correctly including file extension")
			continue
		else:
			break

	while True:
		gameNameVerticalPercentage = float(input("Enter a value between 0 and 100 to indicate what % down the page you want the game's name to appear: "))
		if gameNameVerticalPercentage > 100 or gameNameVerticalPercentage < 0:
			print("Your percentage value must be between 0 and 100")
			continue
		else:
			break

	while True:
		gameNameHorizontalPercentage = float(input("Enter a value between 0 and 100 to indicate what % across the page you want the game's name to appear: "))
		if gameNameHorizontalPercentage > 100 or gameNameHorizontalPercentage < 0:
			print("Your percentage value must be between 0 and 100")
			continue
		else:
			break

	while True:
		gameNameFontSize = int(input("Enter a value for the font size of the game name in px: "))
		if gameNameFontSize < 1 or gameNameFontSize > 500:
			print("Font size must be between 1 and 500")
			continue
		else:
			break

	print("\n\nEnter your preferences for the supplier name")

	while True:
		supplierNameCustomFont = input("Enter the name of the font you wish to use for the supplier name. Ensure it is saved in the 'fonts' folder and include the file extension (e.g. NotoSans-Bold.ttf): ")
		if os.path.exists(current_dir + '/fonts/' + supplierNameCustomFont) == False:
			print("Font does not exist in /fonts/ folder. Please add this font to the folder or ensure you have typed its name correctly including file extension")
			continue
		else:
			break

	while True:
		supplierNameVerticalPercentage = float(input("Enter a value between 0 and 100 to indicate what % down the page you want the supplier's name to appear: "))
		if supplierNameVerticalPercentage > 100 or supplierNameVerticalPercentage < 0:
			print("Your percentage value must be between 0 and 100")
			continue
		else:
			break

	while True:
		supplierNameHorizontalPercentage = float(input("Enter a value between 0 and 100 to indicate what % across the page you want the supplier's name to appear: "))
		if supplierNameHorizontalPercentage > 100 or supplierNameHorizontalPercentage < 0:
			print("Your percentage value must be between 0 and 100")
			continue
		else:
			break

	while True:
		supplierNameFontSize = float(input("Enter a value for the font size of the supplier's name in px: "))
		if supplierNameFontSize < 1 or supplierNameFontSize > 500:
			print("Font size must be between 1 and 500")
			continue
		else:
			break

# Taking the variables and using them to iterate over the game & image list

for images in game_list:
	try:
		# Open an Image

		img = Image.open(current_dir + '/game_images/' + images['image_name'])
	
		width, height = img.size

		# Call draw Method to add 2D graphics in an image

		I1 = ImageDraw.Draw(img)
		
		# Custom font style and font size
		
		nameFont = ImageFont.truetype(current_dir + '/fonts/' + gameNameCustomFont, int(gameNameFontSize))
		supplierFont = ImageFont.truetype(current_dir + '/fonts/' + supplierNameCustomFont, int(supplierNameFontSize))
		
		# Add Text to the images
		
		I1.text((width * float(gameNameHorizontalPercentage)/100, height * float(gameNameVerticalPercentage)/100), textwrap.fill(images['game_name'].upper(), 14), font=nameFont, fill =(255, 255, 255), anchor="mm", spacing = 1, align = "center")
		I1.text((width * float(supplierNameHorizontalPercentage)/100, height * float(supplierNameVerticalPercentage)/100), textwrap.fill(images['supplier'], 20), font=supplierFont, fill =(255, 255, 255), anchor="mm", spacing = 1, align = "center")
		
		# Save the edited image
		
		img.save(current_dir + '/game_images/edited/' + images['image_name'], quality = 'keep')
		
		# Print confirmation that the game is complete
		
		print(images['game_name'] + ' completed!')
	except:
		
		print(images['image_name'] + " not completed! An unspecfied error has occurred")