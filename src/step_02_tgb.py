import taipy.gui.builder as tgb
from taipy.gui import Gui

if __name__ == "__main__":
    text = "type here"
    gathering = "Welcome to Warehouse Doc."

    with tgb.Page() as page:
        tgb.text("{gathering} ", mode="md")
        tgb.text("My text: {text}")

        tgb.input("{text}")

    Gui(page).run(debug=True)
