import tkinter as tk
from tkinter import ttk

# USING A FUNCTION
def createSegment(parent, labelText, buttonText):
    frame = ttk.Frame(master = parent)

    # Gridded layout
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0,1,2), weight = 1, uniform = "a")

    # Create widgets
    ttk.Label(frame, text = labelText).grid(row = 0, column = 0, sticky = "nsew")
    ttk.Button(frame, text = buttonText).grid(row = 0, column = 1, sticky = "nsew")

    return frame

# USING A CLASS
class Segment(ttk.Frame):
    def __init__(self, parent, labelText, buttonText, exerciseText):
        super().__init__(master = parent)

        # Gridded layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")

        # Create widgets
        ttk.Label(self, text = labelText).grid(row = 0, column = 0, sticky = "nsew")
        ttk.Button(self, text = buttonText).grid(row = 0, column = 1, sticky = "nsew")

        self.createExercise(exerciseText).grid(row = 0, column = 2, sticky = "nswe")
        self.pack(expand = True, fill = "both", padx = 10, pady = 10)

    def createExercise(self, text):
        frame = ttk.Frame(master = self)
        ttk.Entry(frame).pack(expand = True, fill = "both")
        ttk.Button(frame, text = text).pack(expand = True, fill = "both")

        return frame

# Create window
window = tk.Tk()
window.title("Widgets and Returning")
window.geometry("400x600")

# Widgets using the class
Segment(window, "Label #1", "Button #1", "test")
Segment(window, "Label #2", "Button #2", "test")
Segment(window, "Label #3", "Button #3", "test")
Segment(window, "Label #4", "Button #4", "test")
Segment(window, "Label #5", "Button #5", "test")

# Widgets using the function
# createSegment(window, "Label #1", "Button #1").pack(expand = True, fill = "both", padx = 10, pady = 10)
# createSegment(window, "Label #2", "Button #2").pack(expand = True, fill = "both", padx = 10, pady = 10)
# createSegment(window, "Label #3", "Button #3").pack(expand = True, fill = "both", padx = 10, pady = 10)
# createSegment(window, "Label #4", "Button #4").pack(expand = True, fill = "both", padx = 10, pady = 10)
# createSegment(window, "Label #5", "Button #5").pack(expand = True, fill = "both", padx = 10, pady = 10)

# Run window
window.mainloop()