from lib.types import exitcodes as e

# Run UI code
def init_frontend(PORT:int) -> int:
    import webview

    # All frontend files held in the "con" folder out of root
    window = webview.create_window(title="Test",
        url=f"http://localhost:{PORT}")

    webview.start()
    return e.EXIT_SUCCESS.value
