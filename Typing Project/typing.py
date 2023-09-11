import tkinter as tk
import time
import threading
import random



# create typing class 
class Typing_Speed_Checking:

    # create a simple constructor
    def __init__(self):
        self.interface = tk.Tk()
        self.interface.title("TESTING SPEED OF TYPER")
        self.interface.geometry("800x600")
        
        #added image to title bar
        self.interface.iconphoto(False,tk.PhotoImage(file = "typing.png"))
        self.interface.configure(bg = "cyan")


        #text file to read the data for typing
        self.text_file = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.interface)

        # creating a data as label to do work or typing
        self.sample_content = tk.Label(self.frame, text=random.choice(self.text_file), font=("Arial", 18))
        self.sample_content.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # creating a display to enter the data and check
        self.dp_interface = tk.Entry(self.frame, width=40, font=("Arial", 24),bd= "8px",bg= "yellow",highlightcolor="green")
        self.dp_interface.grid(row=1, column=0, columnspan=2, padx=5, pady=20)
        
        
        # adding the function to start automatically if the key is pressed
        self.dp_interface.bind("<KeyPress>", self.start_typing)

        # creating a label to help us showing time of speed
        self.speed_testing = tk.Label(self.frame, text="Speed: \n0.00 WPS\n0.00 WPM", font=("Arial", 18))
        self.speed_testing.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        # creating a reset button
        self.reseting_button = tk.Button(self.frame, text="Reset", command=self.reseting, font=("Arial", 24),bg="red",bd="8px")
        self.reseting_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)


        # adding the stating values.
        self.counter = 0
        self.running = False

        self.interface.mainloop()
        
    
    #function of typing to start typing data
    def start_typing(self ,event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.timer_threading)
                t.start()
        if not self.sample_content.cget('text').startswith(self.dp_interface.get()):
            self.dp_interface.config(fg="black")
            self.running = False
        else:
            self.dp_interface.config(fg="red")
            self.running = False
        if self.dp_interface.get() == self.sample_content.cget('text')[:-1]:
            self.running = False
            self.dp_interface.config(fg="blue")
            
            
      #function to maintain the time of speed      
    def timer_threading(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            wps = len(self.dp_interface.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_testing.config(text=f"Speed: \n{wps:.2f} WPS\n{wpm:.2f} WPM")
            
     #function for reseting the data given in text file        
    def reseting(self):
        self.running = False
        self.counter = 0
        self.speed_testing.config(text="Speed: \n0.00 WPS\n0.00 WPM")
        self.sample_content.config(text=random.choice(self.text_file))
        self.dp_interface.delete(0, tk.END)
        
 

#function call to typing class
Typing_Speed_Checking()

