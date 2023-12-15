# Save this code in a file, e.g., my_script.py


import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    return file_path

def run_accelerate_command(target_directory='/Images', new_file_name='custom.png'):
    os.makedirs(target_directory, exist_ok=True)
    original_file_path = select_image_file()
    original_file_name = os.path.basename(original_file_path)
    target_file_name = new_file_name or original_file_name
    target_path = os.path.join(target_directory, target_file_name)
    
    shutil.copy(original_file_path, target_path)
    print(f"Image copied and saved to {target_path}")

    file_path = f'{target_directory}/output.png'
    if os.path.exists(file_path):
        os.remove(file_path)
    
    subprocess.run(['rembg', 'i', target_path, f'{target_directory}/output.png'])
    os.remove(target_path)
    print('Done 1')

def run_accelerate(config_file_path):
    run_accelerate_command(config_file_path)
    file_path = '/outputs'
    if os.path.exists(file_path):
       shutil.rmtree(file_path)
       print(f'Removed existing {file_path}')
    command = "accelerate launch --config_file 1gpu.yaml test_mvdiffusion_seq.py --config configs/mvdiffusion-joint-ortho-6views.yaml"
    command_list = command.split()
    subprocess.run(command_list)
    print('Done 2')


run_accelerate('./Images')