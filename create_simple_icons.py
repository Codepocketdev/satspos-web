from PIL import Image, ImageDraw
# Purple color (#667eea)
purple = (102, 126, 234)
white = (255, 255, 255)

# Create 192x192 icon
img192 = Image.new('RGB', (192, 192), color=purple)
d = ImageDraw.Draw(img192)
# Draw a lightning bolt shape (simplified)
d.polygon([(96, 30), (70, 96), (110, 96), (86, 162), (120, 96), (80, 96), (96, 30)], fill=white)
img192.save('icon-192.png')
print("✓ Created icon-192.png")

# Create 512x512 icon
img512 = Image.new('RGB', (512, 512), color=purple)
d = ImageDraw.Draw(img512)
# Draw a lightning bolt shape (scaled up)
d.polygon([(256, 80), (186, 256), (293, 256), (229, 432), (320, 256), (213, 256), (256, 80)], fill=white)
img512.save('icon-512.png')
print("✓ Created icon-512.png")

print("\nIcons created successfully! ⚡")
