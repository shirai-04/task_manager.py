import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

TASK_FILE = "tasks.txt"

# タスクをファイルに保存
def save_tasks():
    with open(TASK_FILE, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# タスクを読み込む
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

# タスクを追加
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("警告", "タスクを入力してください")

# タスクを削除（複数選択対応）
def delete_task():
    try:
        selected_indices = task_listbox.curselection()  # 選択されたすべてのインデックスを取得
        if not selected_indices:
            raise IndexError
        
        for index in reversed(selected_indices):  # 後ろから削除しないとインデックスがずれる
            task_listbox.delete(index)
        
        save_tasks()
    except IndexError:
        messagebox.showwarning("警告", "削除するタスクを選択してください")

# GUI作成
root = tk.Tk()
root.title("タスク管理アプリ")
root.geometry("400x400")

# 今日の日付を表示するラベル
today_date = datetime.now().strftime("%Y年%m月%d日")  # 今日の日付を取得
task_label = tk.Label(root, text=f"{today_date} のタスク", font=("Arial", 14, "bold"))
task_label.pack(pady=5)

# 入力フィールドと追加ボタン
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="タスクを追加", command=add_task)
add_button.pack()

# タスクリスト表示（複数選択可能に変更）
task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.MULTIPLE)
task_listbox.pack(pady=10)

# 削除ボタン
delete_button = tk.Button(root, text="選択したタスクを削除", command=delete_task)
delete_button.pack()

# タスクをロード
load_tasks()

# アプリ起動
root.mainloop()
