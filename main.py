# -*- coding: utf-8 -*-
import os
from PIL import Image

def collect_images_from_folder(folder_path):
    images = []
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, file_name)
            img = Image.open(file_path)
            images.append(img)
    return images

def create_image_grid(images, rows, cols, margin=50):
    if not images:
        raise Exception("No images to create a grid")

    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    max_height = max(heights)

    grid_width = cols * max_width + (cols + 1) * margin
    grid_height = rows * max_height + (rows + 1) * margin

    grid_image = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))

    for idx, image in enumerate(images):
        row = idx // cols
        col = idx % cols
        x = col * max_width + (col + 1) * margin
        y = row * max_height + (row + 1) * margin
        grid_image.paste(image, (x, y))

    return grid_image

def main(folders):
    all_images = []
    base_path = os.path.join(os.getcwd(), 'Для тестового')
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        images = collect_images_from_folder(folder_path)
        all_images.extend(images)

    rows, cols = 3, 3
    output_image = create_image_grid(all_images, rows, cols)
    output_image.save("Result.tif", compression="tiff_deflate")
    print("Images saved to Result.tif")

if __name__ == "__main__":
    folders = ['1369_12_Наклейки 3-D_3', '1388_12_Наклейки 3-D_3']
    main(folders)
