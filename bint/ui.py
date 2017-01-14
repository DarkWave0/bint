import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets(master)

    def create_widgets(self, master):
        top_frame = ttk.Frame(self)
        top_frame.pack(side="top")

        btn = ttk.Button(self)
        btn['text'] = 'Browse'
        btn['command'] = self.select_dir
        btn.pack()

        self.quit = ttk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack(side="bottom")

    def select_dir(self):
        dir_entry = tix.DirSelectDialog(self)
        dir_entry['command'] = self.dir_selected
        dir_entry.popup()

    def dir_selected(self, directory):
        print('Directory: ', directory)

root = tix.Tk()
app = Application(master=root)
app.mainloop()
