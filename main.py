import tkinter as tk
from gemini_app import GeminiLiveApp
from config import GEMINI_API_KEY

if __name__ == "__main__":
    root = tk.Tk()
    app = GeminiLiveApp(root)
    root.mainloop()
