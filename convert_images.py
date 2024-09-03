"""
 * Traox Studios Image Format Converter
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

import os
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

def convert_images(source_folder, source_format, target_format, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    valid_formats = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'}
    source_format = source_format.lower().strip('.')
    target_format = target_format.lower().strip('.')

    if source_format not in valid_formats or target_format not in valid_formats:
        raise ValueError(f"Invalid format(s). Valid formats are: {', '.join(valid_formats)}")

    print(f"{Fore.GREEN}Converting images from {source_format} to {target_format}...")

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(f".{source_format}"):
            file_path = os.path.join(source_folder, filename)
            try:
                with Image.open(file_path) as img:
                    base_filename = os.path.splitext(filename)[0]
                    target_filename = f"{base_filename}.{target_format}"
                    target_file_path = os.path.join(target_folder, target_filename)
                    
                    img.convert('RGB').save(target_file_path, target_format.upper())
                    
                    print(f"{Fore.GREEN}Converted: {filename} to {target_filename}")
            
            except Exception as e:
                print(f"{Fore.RED}Error converting {filename}: {e}")

def main():
    print(f"{Fore.CYAN}Welcome to the Image Format Converter!")
    print(f"{Fore.CYAN}This utility is a part of the image-batch processing suite. It will help you convert all images within a folder to the new formats!")

    source_folder = input(f"{Fore.CYAN}Enter the folder containing source images: ").strip()
    source_format = input(f"{Fore.CYAN}Enter the source image format (e.g., 'jpg', 'jpeg', 'png', 'bmp', 'webp', 'gif'): ").strip()
    target_format = input(f"{Fore.CYAN}Enter the target image format (e.g., 'jpg', 'jpeg', 'png', 'bmp', 'webp', 'gif'): ").strip()
    target_folder = input(f"{Fore.CYAN}Enter the folder to save converted images: ").strip()

    try:
        convert_images(
            source_folder=source_folder,
            source_format=source_format,
            target_format=target_format,
            target_folder=target_folder
        )
    except ValueError as e:
        print(f"{Fore.RED}{e}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    main()
