import customtkinter as ctk
# Also works with normal tkinter

try: # ONLY WORKS ON WINDOWS SO EXCEPTION HANDLING FOR OTHER OS SYSTEMS
    from ctypes import windll, byref, sizeof, c_int # required to change title bar colour
except:
    pass

# Create window
window = ctk.CTk(fg_color = "#888888")
window.geometry("300x200")

try: # ONLY WORKS ON WINDOWS SO EXCEPTION HANDLING FOR OTHER OS SYSTEMS
    # Change title bar colour
    HWND = windll.user32.GetParent(window.winfo_id())
    titleBarColour = 0x00888888 #BB GG RR - opposite of RGB
    windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(titleBarColour)), sizeof(c_int)) # 35 = title bar colour attribute

    # Change title bar text colour
    HWND = windll.user32.GetParent(window.winfo_id())
    titleBarTextColour = 0x00FFFFFF #BB GG RR - opposite of RGB
    windll.dwmapi.DwmSetWindowAttribute(HWND, 36, byref(c_int(titleBarTextColour)), sizeof(c_int)) # 36 = title bar text colour attribute
except:
    pass

# Run window
window.mainloop()