import tkinter as tk
import subprocess
from PIL import Image, ImageTk

# Define the dictionary of apps with their names and paths
apps = {
    "Chatty": "/Users/kingziaire/Desktop/FinalProject/Chatty/chatty.py",
    "GenerateApp": "/Users/kingziaire/Desktop/FinalProject/GenerateApp/main.py",
    "Snake": "/Users/kingziaire/Desktop/FinalProject/snakegame/snakegame.py",
    "WeatherApp": "/Users/kingziaire/Desktop/FinalProject/Weather App/weatherApp_GUI.py",
    "VisionApp": "/Users/kingziaire/Desktop/FinalProject/vision-app/hgp-vision/vision.py"
}

# Function to open the selected application
def open_app(app_path):
    try:
        if app_path.endswith(".py"):
            subprocess.Popen(["python3", app_path])
        else:
            subprocess.Popen(["open", "-a", app_path])
    except FileNotFoundError:
        print(f"Error: {app_path} not found.")
    except Exception as e:
        print(f"Error: Failed to open {app_path}. {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("App Launcher")

# Set the window to full-screen mode
root.attributes("-fullscreen", True)

# Load and display an image at the top
image_path = "/Users/kingziaire/Desktop/FinalProject/images (3).jpeg"
image = Image.open(image_path)
image = image.resize((275, 300))
image = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=image, bg="Purple")
image_label.pack(pady=10)

# Add a text box at the top of the menu to introduce the menu
intro_label = tk.Label(root, text="Ziaire's Menu", font=("Times New Roman", 24), bg="white", fg="sky blue", relief='solid', padx=10, pady=10)
intro_label.pack(pady=10)

# Create a frame to hold the introduction and the buttons
content_frame = tk.Frame(root, bg='sky blue',)
content_frame.pack(expand=True, fill='both', padx=10, pady=10)

# Create a frame to hold the title label at the top of the menu to introduce the menu
title_frame = tk.Frame(content_frame, bg='white')
title_frame.pack(anchor='w', padx=10, pady=10) # Position it at the top left with padding

# Create a frame to hold the buttons
button_frame = tk.Frame(content_frame, bg='sky blue')
button_frame.pack(side='left', expand=True, fill='both', padx=10, pady=10, anchor='w')

# Create a frame to contain the text widget
frame = tk.Frame(content_frame, bg="sky blue", relief="solid", padx=10, pady=20)
frame.pack(pady=(0, 0), side=tk.RIGHT, fill=tk.BOTH)

# Allow the frame to resize based on its content
frame.pack_propagate(True)

# Create a text widget
text_label = tk.Label(frame, text="Welcome to my menu app. Here you can check and explore each application shown. Enjoy!!", font=("Times New Roman", 17),  height=10, width=85, relief='solid')
text_label.pack(pady=30) # Set the pady value (top and bottom)

# Create buttons for each app
for app_name, app_path in apps.items():
    button = tk.Button(button_frame, text=app_name, width=60,
                       command=lambda path=app_path: open_app(path),
                       borderwidth=0, highlightthickness=0, relief='solid')
    button.pack(pady=20, anchor='w')

# Create a frame to hold the text box
intro_frame = tk.Frame(content_frame, bg='sky blue')
intro_frame.pack(anchor='e', padx=30) # Position the text box to the right

# Set the background color to sky blue
root.configure(bg='sky blue') # Hex code for sky blue

# Run the tkinter main loop
root.mainloop()
