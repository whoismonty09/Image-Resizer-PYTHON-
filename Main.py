from PIL import Image

print("Image Resizer developed by Monty")
image_path = input("Enter image path: ")
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

img = Image.open(image_path)
resized_img = img.resize((width, height))

resized_img.save("resized_image.png")

print("Image resized successfully")
