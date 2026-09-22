from lib.types import exitcodes as e
import threading
import time


class Frontend:
    def __init__ (self, port:int):
        self._window = None;
        self.port = port;

    def set_window(self, window):
        self._window = window;

    def change_page(self, page_name):
        # Run the navigation in a separate thread so this function returns immediately
        threading.Thread(target=self._navigate, args=(page_name,)).start()

    def _navigate(self, page_name):
        time.sleep(0.1)  # Gives the frontend bridge time to close cleanly
        print("Changing window URL to " + page_name);
        self._window.load_url(f'http://127.0.0.1:{self.port}/{page_name}')


# Run UI code
def init_frontend(PORT:int) -> int:
    import webview

    api = Frontend(PORT);

    # All frontend files held in the "templates" folder out of root
    window = webview.create_window(title="Test",
        url=f"http://localhost:{PORT}", js_api=api)

    api.set_window(window);
    webview.start()
    return e.EXIT_SUCCESS.value
