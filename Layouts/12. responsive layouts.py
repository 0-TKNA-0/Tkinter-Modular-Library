import tkinter as tk
from tkinter import ttk

# Create window
class App(tk.Tk):
    def __init__(self, startSize):
        super().__init__()
        self.title("Responsive Layout")
        self.geometry(f"{startSize[0]}x{startSize[1]}")

        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = "both")


        size_Notifier = SizeNotifier(self, {300: self.createSmallLayout, 600: self.createMediumLayout, 1200: self.createLargeLayout})
        self.mainloop()
        
    def createSmallLayout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text = "Label #1", background = "red").pack(expand = True, fill = "both", padx = 10, pady = 5)
        ttk.Label(self.frame, text = "Label #2", background = "green").pack(expand = True, fill = "both", padx = 10, pady = 5)
        ttk.Label(self.frame, text = "Label #3", background = "blue").pack(expand = True, fill = "both", padx = 10, pady = 5)
        ttk.Label(self.frame, text = "Label #3", background = "yellow").pack(expand = True, fill = "both", padx = 10, pady = 5)
        self.frame.pack(expand = True, fill = "both")

    def createMediumLayout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight = 1, uniform = "a")
        self.frame.rowconfigure((0,1), weight = 1, uniform = "a")
        self.frame.pack(expand = True, fill = "both")

        ttk.Label(self.frame, text = "Label #1", background = "red").grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #2", background = "green").grid(column = 1, row = 0, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #3", background = "blue").grid(column = 0, row = 1, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #3", background = "yellow").grid(column = 1, row = 1, sticky = "nsew", padx = 10, pady = 10)

    def createLargeLayout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight = 1, uniform = "a")
        self.frame.rowconfigure(0, weight = 1, uniform = "a")
        self.frame.pack(expand = True, fill = "both")

        ttk.Label(self.frame, text = "Label #1", background = "red").grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #2", background = "green").grid(column = 1, row = 0, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #3", background = "blue").grid(column = 2, row = 0, sticky = "nsew", padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label #3", background = "yellow").grid(column = 3, row = 0, sticky = "nsew", padx = 10, pady = 10)


class SizeNotifier:
    def __init__(self, window, sizeDict):
        self.window = window
        self.sizeDict = {key: value for key, value in sorted(sizeDict.items())}
        self.currentMinSize = None
        self.window.bind("<Configure>", self.check)

        self.window.update()

        minHeight = self.window.winfo_height()
        minWidth = list(self.sizeDict)[0]
        self.window.minsize(minWidth, minHeight)

    def check(self, event):
        if event.widget == self.window:
            windowWidth = event.width
            checkedSize = None

            for minSize in self.sizeDict:
                delta = windowWidth - minSize
                if delta >= 0:
                    checkedSize = minSize

            if checkedSize != self.currentMinSize:
                self.currentMinSize = checkedSize
                self.sizeDict[self.currentMinSize]()
        

# Run window
app = App((400,300))