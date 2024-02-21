import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
from ttkbootstrap import ttk
from ttkbootstrap import Style



def upload_reader_data():
    filepath = filedialog.askopenfilename()
    if filepath:
        entry_reader_data_path.config(state=tk.NORMAL)
        entry_reader_data_path.delete(0, tk.END)
        entry_reader_data_path.insert(0, filepath)
        entry_reader_data_path.config(state=tk.DISABLED)
        # 在这里添加处理上传文件的逻辑


def upload_matching_data():
    filepath = filedialog.askopenfilename()
    if filepath:
        entry_matching_data_path.config(state=tk.NORMAL)
        entry_matching_data_path.delete(0, tk.END)
        entry_matching_data_path.insert(0, filepath)
        entry_matching_data_path.config(state=tk.DISABLED)
        # 在这里添加处理上传文件的逻辑


def generate_files():
    folderpath = filedialog.askdirectory()
    if folderpath:
        # 在这里添加生成文件的逻辑
        for i in range(100):
            progress_var.set(i + 1)
            app.update_idletasks()
            time.sleep(0.05)
        messagebox.showinfo("信息", "文件已成功生成于: " + folderpath)
        progress_var.set(0)
        app.update_idletasks()


app = tk.Tk()
app.withdraw()
style = Style(theme='sandstone')
TOP6 = style.master
app.title("自动匹配脚本")
app.update_idletasks()
window_width = app.winfo_width()
window_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2) - 170
y = (screen_height / 2) - (window_height / 2) - 100
app.geometry('+%d+%d' % (x, y))
app.resizable(width=False, height=False)
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)
btn_upload_reader_data = tk.Button(frame, text="上传读卡器数据", command=upload_reader_data, width=15)
btn_upload_reader_data.grid(row=0, column=0, padx=10)
entry_reader_data_path = tk.Entry(frame, state=tk.DISABLED, width=60)
entry_reader_data_path.grid(row=0, column=1, pady=10, padx=10)
btn_upload_matching_data = tk.Button(frame, text="上传匹配数据", command=upload_matching_data, width=15)
btn_upload_matching_data.grid(row=1, column=0, pady=10)
entry_matching_data_path = tk.Entry(frame, state=tk.DISABLED, width=60)
entry_matching_data_path.grid(row=1, column=1, pady=10, padx=10)
btn_generate = tk.Button(frame, text="生成结果数据", command=generate_files, width=15)
btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.grid(row=3, column=0, columnspan=2, pady=(0, 10), sticky='ew')

app.deiconify()
app.mainloop()
