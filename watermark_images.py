"""
 * Traox Studios Image Watermarking Tool
 * Copyright (c) 2024 Traox Studios Limited™ and contributors
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the MIT License as published by
 * Traox Studios Limited™.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * MIT License for more details.
 *
 * You should have received a copy of the MIT License
 * along with this program. If not, see <https://opensource.org/licenses/MIT>.
"""

from PIL import Image
import os
from colorama import Fore, Style, init

init(autoreset=True)

def add_watermark(image_path, watermark_path, position, padding_x, padding_y, output_folder, watermark_size):
    with Image.open(image_path) as img:
        with Image.open(watermark_path) as watermark:
            if watermark_size:
                watermark = watermark.resize(watermark_size, Image.LANCZOS)
            
            if watermark.mode != 'RGBA':
                watermark = watermark.convert('RGBA')
            
            img_width, img_height = img.size
            watermark_width, watermark_height = watermark.size
            
            if position == 'top-left':
                position = (padding_x, padding_y)
            elif position == 'top-right':
                position = (img_width - watermark_width - padding_x, padding_y)
            elif position == 'bottom-left':
                position = (padding_x, img_height - watermark_height - padding_y)
            elif position == 'bottom-right':
                position = (img_width - watermark_width - padding_x, img_height - watermark_height - padding_y)
            else:
                raise ValueError("Invalid position. Choose from 'top-left', 'top-right', 'bottom-left', 'bottom-right'")
            
            watermark_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
            watermark_layer.paste(watermark, position, watermark)
            
            watermarked_img = Image.alpha_composite(img.convert('RGBA'), watermark_layer)
            
            if img.mode != 'RGBA':
                watermarked_img = watermarked_img.convert(img.mode)
            
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            watermarked_img.save(output_path)
            print(f"{Fore.GREEN}Watermarked {os.path.basename(image_path)}")

def main():
    print(f"{Fore.CYAN}Welcome to the Image Watermarking Tool!")
    print(f"{Fore.CYAN}This utility is a part of the image-batch processing suite. It will help you automatically apply a watermark to all of your photos!")

    folder_path = input(f"{Fore.CYAN}Enter the folder containing the images: ").strip()
    watermark_path = input(f"{Fore.CYAN}Enter the watermark image file path: ").strip()
    position = input(f"{Fore.CYAN}Enter the position of the watermark (top-left, top-right, bottom-left, bottom-right): ").strip().lower()
    padding_x = int(input(f"{Fore.CYAN}Enter horizontal padding (in pixels): ").strip())
    padding_y = int(input(f"{Fore.CYAN}Enter vertical padding (in pixels): ").strip())
    output_folder = input(f"{Fore.CYAN}Enter the folder to save watermarked images: ").strip()
    
    resize_choice = input(f"{Fore.CYAN}Do you want to resize the watermark? (yes/no): ").strip().lower()
    watermark_size = None
    if resize_choice == 'yes':
        try:
            width = int(input(f"{Fore.CYAN}Enter the watermark width (in pixels): ").strip())
            height = int(input(f"{Fore.CYAN}Enter the watermark height (in pixels): ").strip())
            watermark_size = (width, height)
        except ValueError:
            print(f"{Fore.RED}Invalid size values. Using default watermark size.")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
                image_path = os.path.join(folder_path, filename)
                add_watermark(image_path, watermark_path, position, padding_x, padding_y, output_folder, watermark_size)
        print(f"{Fore.CYAN}Watermarking process completed.")
    except ValueError as e:
        print(f"{Fore.RED}{e}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    main()
