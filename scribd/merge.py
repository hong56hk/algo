from PIL import Image
import os

folder_path = "downloads"


# Get all file names in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
sorted_image_files = []

for i in range(1, len(image_files)+1, 1):
  found_page = False
  for full_path in image_files:
    file_name = os.path.splitext(os.path.basename(full_path))[0]
    if file_name.startswith(f"{i}-"):
      sorted_image_files.append(full_path)
      found_page = True
  if not found_page:
    print(f"missing page {i}")

# Open the images and convert them to RGB (PDF does not support RGBA)
images = [Image.open(img).convert("RGB") for img in sorted_image_files]

# Save all images as a single PDF
output_path = "output.pdf"
if images:
    images[0].save(output_path, save_all=True, append_images=images[1:])

print(f"PDF saved as {output_path}")