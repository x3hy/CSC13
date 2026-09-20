from lib.types import exitcodes as e

# Run UI code
window = None
def init_frontend(PORT:int) -> int:
    import webview

    global window
    # All frontend files held in the "templates" folder out of root
    window = webview.create_window(title="Test",
        url=f"http://localhost:{PORT}")

    webview.start(http_server=True)
    return e.EXIT_SUCCESS.value
