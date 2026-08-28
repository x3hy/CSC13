import webview
from lib.types import exitcodes as e

# Run UI code
def init_frontend(PORT:int) -> int:
    window = webview.create_window(title="", url=f"http://localhost:{PORT}")
    webview.start()

    return e.EXIT_SUCCESS.value
