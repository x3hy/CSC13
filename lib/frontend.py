from lib.types import exitcodes as e

# Run UI code
def init_frontend(PORT:int) -> int:
    import webview

    # All frontend files held in the "con" folder out of root
    window = webview.create_window(title="",
        url=f"http://localhost:{PORT}",
        background_color="#222",
        min_size=(300, 500),
        frameless=True,
        shadow=True,
        confirm_close=True)

    webview.start()
    return e.EXIT_SUCCESS.value
