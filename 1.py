from PIL import Image

# Open the image
img = Image.open('image.jpg')

# Resize to new dimensions (e.g., 50% smaller)
new_size = (int(img.width * 0.25), int(img.height * 0.25))
resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

# Save the resized image
resized_img.save("resized_image.jpg")
