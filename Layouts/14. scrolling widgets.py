import tkinter as tk
from tkinter import ttk
from random import randint, choice

class ListFrame(ttk.Frame):
    def __init__(self, parent, textData, itemHeight):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")

        # Widget data
        self.textData = textData
        self.itemNumber = len(textData)
        self.listHeight = self.itemNumber * itemHeight

        # Create canvas
        self.canvasWidget = tk.Canvas(self, background = "white", scrollregion = (0,0,self.winfo_width(),self.listHeight))
        self.canvasWidget.pack(expand = True, fill = "both")

        # Widget display frame
        self.frameWidget = ttk.Frame(self)
        
        # Create scrollbar
        self.scrollBarWidget = ttk.Scrollbar(self, orient = "vertical", command = self.canvasWidget.yview)
        self.canvasWidget.config(yscrollcommand = self.scrollBarWidget.set) # Updates the scrollbar UI
        self.scrollBarWidget.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")


        for index, item in enumerate(self.textData):
            self.createItem(index, item).pack(expand = True, fill = "both", pady = 4, padx = 10)

        # Place canvas
        # self.canvasWidget.create_window((0,0), window = self.frameWidget, anchor = "nw", width = self.winfo_width(), height = self.listHeight)

        # Mousewheel scrolling event Binding
        self.canvasWidget.bind_all("<MouseWheel>", lambda event: self.canvasWidget.yview_scroll(-int(event.delta / 60), "units"))
        self.bind("<Configure>", self.updateSize)

    def updateSize(self, event):
        if  self.listHeight >= self.winfo_height():
            height = self.listHeight
            self.canvasWidget.bind_all("<MouseWheel>", lambda event: self.canvasWidget.yview_scroll(-int(event.delta / 60), "units"))
            self.scrollBarWidget.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

        else:
            height = self.winfo_height()
            self.canvasWidget.unbind_all("<MouseWheel>")
            self.scrollBarWidget.place_forget()
            
        # Place canvas
        self.canvasWidget.create_window((0,0), window = self.frameWidget, anchor = "nw", width = self.winfo_width(), height = height)

    def createItem(self, index, item):
        frameWidget = ttk.Frame(self.frameWidget)

        # Gridded layout
        frameWidget.rowconfigure(0, weight = 1)
        frameWidget.columnconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # Create widgets
        ttk.Label(frameWidget, text = f"#{index}").grid(row = 0, column = 0)
        ttk.Label(frameWidget, text = f"{item[0]}").grid(row = 0, column = 1)
        ttk.Button(frameWidget, text = f"{item[1]}").grid(row = 0, column = 2, columnspan = 3, sticky = "nswe")

        return frameWidget


# Create window
window = tk.Tk()
window.title("Scrolling Widgets")
window.geometry("500x400")

textList = [('label', 'button'),('thing', 'click'),('third', 'something'),('label1', 'button'),('label2', 'button'),('label3', 'button'),('label4', 'button')]
listFrame = ListFrame(window, textList, 100)




# Run window
window.mainloop()