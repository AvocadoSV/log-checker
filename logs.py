import subprocess
import tkinter as tk
from tkinter import ttk


def clear_text():
    text.delete("1.0", "end")


def system_logs():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    text.insert(tk.END, result.stdout.decode())


def audit_logs():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    text.insert(tk.END, result.stdout.decode())


def security_timestamps():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "security"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $1}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def security_threads():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "security"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $2}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def security_PID():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "security"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $5}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def security_activity():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "security"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $4}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def security_type():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "security"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $3}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def audit_timestamps():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $1}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def audit_threads():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $2}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def audit_PID():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $5}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def audit_activity():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $4}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def audit_type():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $3}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def system_timestamps():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $1}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def system_threads():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $2}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def system_PID():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $5}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def system_activity():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $4}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def system_type():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "system"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    result2 = subprocess.run(
        ["awk", "{print $3}"], input=result.stdout, capture_output=True
    )
    ttl_column = result2.stdout.decode()
    text.insert(tk.END, ttl_column)


def security_logs():
    result = subprocess.run(
        [
            "sudo",
            "log",
            "show",
            "--predicate",
            'eventMessage contains "audit"',
            "--info",
            "-last",
            "50",
        ],
        capture_output=True,
    )
    text.insert(tk.END, result.stdout.decode())


def search():
    search_str = search_entry.get()
    text.tag_remove("search", "1.0", tk.END)
    if search_str:
        idx = "1.0"
        while True:
            idx = text.search(search_str, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            last_idx = f"{idx}+{len(search_str)}c"
            text.tag_add("search", idx, last_idx)
            idx = last_idx
        text.tag_config("search", background="yellow")
        text.mark_set("insert", "1.0")
        text.see("insert")


root = tk.Tk()

search_entry = tk.Entry(root, width=30)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

frame1 = tk.Frame(root)
frame1.pack()
label = ttk.Label(frame1, text="Security options:")
label.pack(side=tk.LEFT)
options = ["time", "type", "threads", "PID", "Activity"]
combobox = ttk.Combobox(frame1, values=options)
combobox.pack(side=tk.LEFT)

combobox.bind("<<ComboboxSelected>>", lambda event: globals()[combobox.get()]())
globals().update(
    {
        "time": security_timestamps,
        "type": security_type,
        "threads": security_threads,
        "PID": security_PID,
        "Activity": security_activity,
    }
)
frame2 = tk.Frame(root)
frame2.pack()
label = ttk.Label(frame2, text="Audit options:")
label.pack(side=tk.LEFT)
options = ["time", "type", "threads", "PID", "Activity"]
combobox = ttk.Combobox(frame2, values=options)
combobox.pack(side=tk.LEFT)

combobox.bind("<<ComboboxSelected>>", lambda event: globals()[combobox.get()]())
globals().update(
    {
        "time": audit_timestamps,
        "type": audit_type,
        "threads": audit_threads,
        "PID": audit_PID,
        "Activity": audit_activity,
    }
)
frame3 = tk.Frame(root)
frame3.pack()
label = ttk.Label(frame3, text="System options:")
label.pack(side=tk.LEFT)
options = ["time", "type", "threads", "PID", "Activity"]
combobox = ttk.Combobox(frame3, values=options)
combobox.pack(side=tk.LEFT)

combobox.bind("<<ComboboxSelected>>", lambda event: globals()[combobox.get()]())
globals().update(
    {
        "time": system_timestamps,
        "type": system_type,
        "threads": system_threads,
        "PID": system_PID,
        "Activity": system_activity,
    }
)

text = tk.Text(root)
text.pack()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="System Logs", command=system_logs)
button.pack(side=tk.LEFT)
button = tk.Button(frame, text="Audit Logs", command=audit_logs)
button.pack(side=tk.LEFT)
button = tk.Button(frame, text="Security Logs", command=security_logs)
button.pack(side=tk.LEFT)
button = tk.Button(frame, text="Clear", command=clear_text)
button.pack(side=tk.LEFT)

search_button.config(command=search)

root.mainloop()
