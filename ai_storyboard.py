import os
import re
import random
import shutil
from gradio_client import Client
import google.generativeai as genai
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from collections import defaultdict

def load_script(script):
    try:
        with open(script, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading the script file: {e}")
        return None
script_content = load_script('D:/codes/ai_storyboard/creativity.txt')

#generating the missing data in the script using the Gemini generative model
genai.configure(api_key="AIzaSyCYdLd1b819Lr-r6Oh6O8TL-jR5lIYtLKA")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("analysze and break the given script into 6 scenes, givea camera angles, mood and backgroung setting and each scene must be created as an promt for stable diffusion with art style as sketch and manga or anime to understand better. give extreme details to make the images realistic (do not use any '*' and empty spaces, do not use any age factors and no fiction and dont specify age of any character):" +script_content)
#print(response.text)
res = response.text

#parsing the response to get the scenes
def parse_text(text, keyword):
    pattern = rf"(?i)(?={re.escape(keyword)}\s*\d+[:\-]?)"
    sections = re.split(pattern, text)
    return [section.strip() for section in sections if section.strip()]

parsed_sections = parse_text(res, "Scene")

# Append each parsed section to the scenes dictionary
scenes = {}
for i, section in enumerate(parsed_sections, start=1):
    scenes[f"Section {i}"] = section
    #print(f"Section {i}:\n{section}\n")

def generate_image(prompt, output_dir, image_name):
    client = Client("stabilityai/stable-diffusion")
    results = client.predict(
            prompt= prompt,
            negative= "high definition, realistic, detailed, 4k",
            scale=9,
            api_name="/infer"
    )
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, result in enumerate(results):
        image_path = result['image']
        new_image_path = os.path.join(output_dir, f"{image_name}_{idx + 1}.jpg")
        shutil.copy(image_path, new_image_path)
        os.remove(image_path)
        #print(f"Image saved to {new_image_path}")
        #print(results)
    
output_dir = "D:/codes/ai_storyboard/generated"

for i, (scene, content) in enumerate(scenes.items(), start=1):
    image_name = f"Section_{i}"
    generate_image(content, output_dir, image_name)
    print(f"Generated image for {scene}")
    

#creating a GUI to display the generated images

def load_images_by_section(directory):
    try:
        files = os.listdir(directory)
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        sections = defaultdict(list)
        for file in image_files:
            section_name = '_'.join(file.split('_')[:2])
            sections[section_name].append(file)
        
        # Add the full path for each image
        for section in sections:
            sections[section] = [os.path.join(directory, img) for img in sections[section]]
        
        return dict(sections)
    except Exception as e:
        print(f"Error loading images: {e}")
        return {}

def display_random_images(images):
    for section, label in image_labels.items():
        if section in images and images[section]:
            image_path = random.choice(images[section])
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
            print(f"Displayed image: {image_path}")
        else:
            label.config(text="No images available", image="")

images = load_images_by_section(output_dir)

# the tkinter GUI:
root = tk.Tk()
root.title("Scene Image Viewer - All Sections")

frm = tk.Frame(root)
frm.grid(padx=10, pady=20)

# Add labels for each section
image_labels = {}
row = 0
col = 0
for section in images.keys():
    tk.Label(frm, text=section).grid(column=col, row=row*2, padx=5, pady=5)
    label = Label(frm)
    label.grid(column=col, row=row*2 + 1, padx=5, pady=5)
    image_labels[section] = label
    col += 1
    if col > 2:
        col = 0
        row += 1

# Button to display images for all sections
tk.Button(frm, text="Show All Images", command=lambda: display_random_images(images)).grid(column=0, row=4, columnspan=4, pady=20)

# Start the GUI event loop
root.mainloop()