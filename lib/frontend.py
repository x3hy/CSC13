import webview
import threading
import time

def background_task(window):
    time.sleep(5)
    window.evaluate_js('alert("Hello from Python after 5 seconds!");')

if __name__ == '__main__':
    window = webview.create_window('PyWebview Example', html='<h1>Waiting for Python…</h1>')
    thread = threading.Thread(target=background_task, args=(window,))
    thread.start()
    webview.start()
