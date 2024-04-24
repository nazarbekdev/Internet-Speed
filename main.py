import tkinter as tk
import speedtest


def internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    return download_speed, upload_speed, ping


def get_speed():
    download_speed, upload_speed, ping = internet_speed()
    result_text = f"\nDownload Speed: {download_speed:.2f} Mbps\n\nUpload Speed: {upload_speed:.2f} Mbps\n\nPing: {ping} ms\n"
    result_label.config(text=result_text)


def on_enter(event):
    test_button.config(bg="grey")


def on_leave(event):
    test_button.config(bg="SystemButtonFace")


root = tk.Tk()
root.title("Internet Speed")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.attributes("-fullscreen", True)

result_label = tk.Label(root, text="")
result_label.pack()

test_button = tk.Button(root, text="Internet Speed Test", command=get_speed)
test_button.pack()

test_button.bind("<Enter>", on_enter)
test_button.bind("<Leave>", on_leave)

if __name__ == "__main__":
    root.mainloop()
