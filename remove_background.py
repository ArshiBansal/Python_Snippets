from rembg import remove
from PIL import Image
import io

input_path = 'pic.jpg'
output_path = 'pic.png'

# Load image
inp = Image.open(input_path)

# Remove background
output_bytes = remove(inp)

# Convert bytes to image
output_image = Image.open(io.BytesIO(output_bytes))

# Save and show
output_image.save(output_path)
output_image.show()
