import tkinter as tk
from tkinter import ttk
import datetime
import threading
import time
import random
import ctypes

class TimeProgressWidget:
    ##FROM HERE 
    def start_move(self, event):
        self.offset_x = event.x_root - self.root.winfo_x()
        self.offset_y = event.y_root - self.root.winfo_y()

    def do_move(self, event):
        x = event.x_root - self.offset_x
        y = event.y_root - self.offset_y
        self.root.geometry(f"+{x}+{y}")


    #TO HERE
    def __init__(self, root):
        self.root = root
        self.root.title("Time Flow")
        self.root.geometry("380x240")
        #this mext line is added ny me
        root.overrideredirect(True)
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)
        
        # Set the window to be semi-transparent with a gradient background
        self.root.attributes("-alpha", 0.95)
        
        
                
        # Modern color scheme
        self.colors = {
            "bg_gradient_top": "#2E3B4E",
            "bg_gradient_bottom": "#1A1E2B",
            "text_light": "#FFFFFF",
            "text_highlight": "#64FFDA",
            "progress_day": "#4FC3F7",
            "progress_year": "#B39DDB",
            "accent": "#FF4081"
        }
        
        # Create a canvas for gradient background
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Draw gradient background
        self.draw_gradient()
        
        # Create a frame for the widget content
        self.frame = tk.Frame(self.canvas, bg=self.colors["bg_gradient_bottom"])
        self.frame_window = self.canvas.create_window(0, 0, anchor="nw", window=self.frame)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Bind resize event
        self.root.bind("<Configure>", self.on_resize)
        
        # Title with dynamic color animation
        self.title_frame = tk.Frame(self.frame, bg=self.colors["bg_gradient_bottom"])
        self.title_frame.pack(fill=tk.X, pady=(5, 15))
        
        self.title_label = tk.Label(
            self.title_frame, 
            text="TIME FLOW", 
            font=("Verdana", 16, "bold"),
            fg=self.colors["text_highlight"],
            bg=self.colors["bg_gradient_bottom"]
        )
        self.title_label.pack(side=tk.TOP)
        
        ##THIS TOO
        # Bind mouse events to make window draggable
        for widget in [self.title_frame, self.frame, self.canvas]:
            widget.bind("<Button-1>", self.start_move)
            widget.bind("<B1-Motion>", self.do_move)
        
        # Day progress section with stylish design
        self.day_frame = tk.Frame(self.frame, bg=self.colors["bg_gradient_bottom"])
        self.day_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.day_label_frame = tk.Frame(self.day_frame, bg=self.colors["bg_gradient_bottom"])
        self.day_label_frame.pack(fill=tk.X)
        
        tk.Label(
            self.day_label_frame, 
            text="DAY PROGRESS", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["text_light"],
            font=("Verdana", 9, "bold")
        ).pack(side=tk.LEFT)
        
        self.day_percentage = tk.Label(
            self.day_label_frame, 
            text="0%", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["progress_day"],
            font=("Verdana", 9, "bold")
        )
        self.day_percentage.pack(side=tk.RIGHT)
        
        # Create custom style for progress bars
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Day.Horizontal.TProgressbar", 
                        troughcolor=self.colors["bg_gradient_top"],
                        background=self.colors["progress_day"],
                        thickness=8,
                        borderwidth=0)
        
        style.configure("Year.Horizontal.TProgressbar", 
                        troughcolor=self.colors["bg_gradient_top"],
                        background=self.colors["progress_year"],
                        thickness=8,
                        borderwidth=0)
        
        self.day_progress = ttk.Progressbar(
            self.day_frame, 
            orient="horizontal", 
            length=360, 
            mode="determinate",
            style="Day.Horizontal.TProgressbar"
        )
        self.day_progress.pack(fill=tk.X, pady=(5, 0))
        
        # Year progress section with matching style
        self.year_frame = tk.Frame(self.frame, bg=self.colors["bg_gradient_bottom"])
        self.year_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.year_label_frame = tk.Frame(self.year_frame, bg=self.colors["bg_gradient_bottom"])
        self.year_label_frame.pack(fill=tk.X)
        
        tk.Label(
            self.year_label_frame, 
            text="YEAR PROGRESS", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["text_light"],
            font=("Verdana", 9, "bold")
        ).pack(side=tk.LEFT)
        
        self.year_percentage = tk.Label(
            self.year_label_frame, 
            text="0%", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["progress_year"],
            font=("Verdana", 9, "bold")
        )
        self.year_percentage.pack(side=tk.RIGHT)
        
        self.year_progress = ttk.Progressbar(
            self.year_frame, 
            orient="horizontal", 
            length=360, 
            mode="determinate",
            style="Year.Horizontal.TProgressbar"
        )
        self.year_progress.pack(fill=tk.X, pady=(5, 0))
        
        self.year_info_frame = tk.Frame(self.year_frame, bg=self.colors["bg_gradient_bottom"])
        self.year_info_frame.pack(fill=tk.X, pady=(3, 0))
        
        self.year_date_label = tk.Label(
            self.year_info_frame, 
            text="", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["text_light"],
            font=("Verdana", 8)
        )
        self.year_date_label.pack(side=tk.LEFT)
        
        # Current date display with elegant styling
        self.date_frame = tk.Frame(self.frame, bg=self.colors["bg_gradient_bottom"])
        self.date_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Creator label
        self.creator_label = tk.Label(
            self.frame,
            text="Created by lazyflash99",  # <-- change to your actual name
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["text_light"],
            font=("Verdana", 8, "italic")
        )
        self.creator_label.pack(side=tk.BOTTOM, pady=(5, 0))

        
        self.current_date_label = tk.Label(
            self.date_frame, 
            text="", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["accent"],
            font=("Verdana", 10, "bold")
        )
        self.current_date_label.pack(side=tk.LEFT)
        
        self.current_time_label = tk.Label(
            self.date_frame, 
            text="", 
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["accent"],
            font=("Verdana", 10, "bold")
        )
        self.current_time_label.pack(side=tk.RIGHT)
        
        # Start animation for title
        self.animate_title()
        
        # Start the update thread
        self.update_thread = threading.Thread(target=self.update_progress_loop, daemon=True)
        self.update_thread.start()
        
        # Update progress bars immediately
        self.update_progress()
        
        # Add toggle pin button
        self.pin_state = "desktop"  # or "top"
        self.toggle_button = tk.Button(
            self.frame,
            text="📌",
            font=("Verdana", 14, "bold"),
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["accent"],
            bd=0,
            command=self.toggle_pin
        )
        self.toggle_button.place(x=330, y=4)
        
        # Add close button
        self.close_button = tk.Button(
            self.frame,
            text="❌",
            font=("Verdana", 12, "bold"),
            bg=self.colors["bg_gradient_bottom"],
            fg=self.colors["accent"],
            bd=0,
            command=self.root.destroy
        )
        self.close_button.place(x=300, y=10)


    def toggle_pin(self):
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
        if self.pin_state == "desktop":
            # Bring to front
            self.root.attributes("-topmost", True)
            self.pin_state = "top"
            self.toggle_button.config(text="📍")
        else:
            # Send to bottom
            self.root.attributes("-topmost", False)
            ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0,
                0x0001 | 0x0002 | 0x0010)
            self.pin_state = "desktop"
            self.toggle_button.config(text="📌")
    
    
    def draw_gradient(self):
        """Draw gradient background on canvas"""
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        
        # Clear canvas
        self.canvas.delete("gradient")
        
        # Create gradient
        for i in range(height):
            # Calculate color ratio
            ratio = i / height
            r1, g1, b1 = self.hex_to_rgb(self.colors["bg_gradient_top"])
            r2, g2, b2 = self.hex_to_rgb(self.colors["bg_gradient_bottom"])
            
            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, width, i, fill=color, tags="gradient")
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def on_resize(self, event):
        """Handle window resize events"""
        # Redraw gradient and adjust frame
        self.draw_gradient()
        self.canvas.itemconfig(self.frame_window, width=event.width, height=event.height)
    
    def animate_title(self):
        """Animate the title with color changes"""
        # Cycle through colors
        r = int(random.uniform(100, 255))
        g = int(random.uniform(200, 255))
        b = int(random.uniform(200, 255))
        
        next_color = f'#{r:02x}{g:02x}{b:02x}'
        self.title_label.config(fg=next_color)
        
        # Schedule next animation
        self.root.after(2000, self.animate_title)
    
    def update_progress_loop(self):
        """Update progress bars every second"""
        while True:
            self.update_progress()
            time.sleep(1)  # Update every second for more accurate progress
    
    def update_progress(self):
        """Calculate and update day and year progress"""
        now = datetime.datetime.now()
        
        # Calculate day progress
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + datetime.timedelta(days=1)
        day_elapsed = now - start_of_day
        day_total = end_of_day - start_of_day
        day_progress = day_elapsed.total_seconds() / day_total.total_seconds() * 100
        
        # Calculate year progress
        start_of_year = datetime.datetime(now.year, 1, 1)
        end_of_year = datetime.datetime(now.year + 1, 1, 1)
        year_elapsed = now - start_of_year
        year_total = end_of_year - start_of_year
        year_progress = year_elapsed.total_seconds() / year_total.total_seconds() * 100
        
        # Format date information
        days_elapsed = (now - start_of_year).days
        days_total = (end_of_year - start_of_year).days
        days_remaining = days_total - days_elapsed
        
        date_info = f"Day {days_elapsed} of {days_total}, {days_remaining} days remaining"
        
        # Current date and time display
        current_date = now.strftime("%A, %B %d")
        current_time = now.strftime("%H:%M:%S")
        
        # Update UI on the main thread
        self.root.after(0, lambda: self.update_ui(
            day_progress, 
            year_progress, 
            date_info, 
            current_date, 
            current_time
        ))
    
    def update_ui(self, day_progress, year_progress, date_info, current_date, current_time):
        """Update the UI with calculated progress values"""
        # Update day progress
        self.day_progress["value"] = day_progress
        self.day_percentage["text"] = f"{day_progress:.1f}%"
        
        # Update year progress
        self.year_progress["value"] = year_progress
        self.year_percentage["text"] = f"{year_progress:.1f}%"
        self.year_date_label["text"] = date_info
        
        # Update current date and time
        self.current_date_label["text"] = current_date
        self.current_time_label["text"] = current_time

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeProgressWidget(root)
    root.mainloop()