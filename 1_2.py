from PIL import Image, ImageFilter
from pathlib import Path

current_dir = ''
filenames = Path(current_dir).glob('*')
Path('new_images').mkdir(parents=True, exist_ok=True)

for file in filenames:
    if file.suffix in ['.jpg', '.png']:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.save(Path("new_images", file))