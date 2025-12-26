from PIL import Image
import pillow_heif

# Load HEIC file
heic_file = "nirav.heic"
image = pillow_heif.read_heif(heic_file)

# Convert to PIL Image
pil_image = Image.frombytes(
    image.mode, image.size, image.data
)

# Save as JPG
pil_image.save("output.jpg", "JPEG")
print("Conversion complete!")
