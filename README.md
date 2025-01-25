# AI-Storyboard-for-cinematography

## 🎬 Project Overview

The **AI Storyboarding Tool** is a Python-based application that automates the process of transforming textual scripts into visual storyboards. By combining natural language processing and AI-generated images, this project helps creators visualize their ideas seamlessly.

---

## 🚀 Features

1. **Script Parsing**:
   - Automatically breaks scripts into six detailed scenes.
   - Includes camera angles, mood, and background settings.

2. **AI-Generated Images**:
   - Uses **Google Gemini AI** for scene descriptions.
   - Integrates **Stable Diffusion** to create sketch-style visuals for each scene.

3. **User-Friendly GUI**:
   - Built with **Tkinter** to display scene images in a clean, grid-based layout.
   - Features options to refresh images dynamically.

---

## 📂 Directory Structure
```
.
├── ai_storyboarding_tool
│   ├── creativity.txt  # Input script file
│   ├── generated       # Directory for generated images
│   └── main.py         # Main script
├── README.md           # Project documentation
```

---

## 🛠️ Libraries Used

- **Google Gemini AI**: For generating scene details.
- **Stable Diffusion**: For creating visual imagery.
- **Tkinter**: For the graphical user interface.
- **Pillow (PIL)**: For image resizing and processing.
- **re**: For script parsing with regex.
- **os & shutil**: For file and directory management.
- **collections**: For organizing images by section.

---

## 🔧 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Tanmay0766/AI-Storyboard-for-cinematography.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AI-Storyboard-for-cinematography
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API keys for **Google Gemini AI** and **Stable Diffusion** in the script.

5. Run the application:
   ```bash
   python main.py
   ```

---

## 🖼️ How It Works

1. Load a script (`creativity.txt`).
2. Parse the script into six scenes using AI.
3. Generate scene descriptions and prompts for **Stable Diffusion**.
4. Create and save visuals for each scene.
5. Display all visuals in the GUI, organized by sections.

---

## 💡 Learnings

- Implementing AI-powered workflows.
- Seamless integration of APIs like **Google Gemini** and **Stable Diffusion**.
- Designing intuitive GUIs with **Tkinter**.
- Advanced file organization for scalability.

---

## 🤝 Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## 🌟 Acknowledgments

- The amazing teams behind **Google Gemini AI** and **Stable Diffusion**.
- Open-source libraries and the Python community for their support.
