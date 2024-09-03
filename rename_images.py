"""
 * Traox Studios File Renaming Tool
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
from colorama import Fore, init

init(autoreset=True)

def rename_files_sequentially(folder_path):
    if not os.path.exists(folder_path):
        print(f"{Fore.RED}The folder does not exist.")
        return
    
    files = sorted(os.listdir(folder_path))
    
    if not files:
        print(f"{Fore.YELLOW}No files found in the folder.")
        return
    
    print(f"{Fore.GREEN}Renaming files in {folder_path}...")

    for index, filename in enumerate(files):
        old_file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(old_file_path):
            new_filename = f"{index + 1}{os.path.splitext(filename)[1]}"
            new_file_path = os.path.join(folder_path, new_filename)
            
            os.rename(old_file_path, new_file_path)
            print(f"{Fore.GREEN}Renamed {filename} to {new_filename}")
        else:
            print(f"{Fore.YELLOW}Skipping directory {filename}")
    
    print(f"{Fore.CYAN}Renaming process completed.")

def main():
    print(f"{Fore.CYAN}Welcome to the File Renaming Tool!")
    print(f"{Fore.CYAN}This utility is a part of the image-batch processing suite. It will help you automatically rename all files in a directory to numbers!")
    
    folder_path = input(f"{Fore.CYAN}Enter the folder containing the files to rename: ").strip()

    try:
        rename_files_sequentially(folder_path)
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    main()
