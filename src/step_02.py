from taipy.gui import Gui

if __name__ == "__main__":
    text = "input the json or setup here ---->"

    page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
    """

    Gui(page).run(debug=True)
