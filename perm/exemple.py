from nicegui import ui
import pandas as pd
import numpy as np

with ui.card(align_items="center"):
    with ui.row().classes("items-center"):
        ui.label("Style:")
        ui.separator().props("vertical")
        ui.select(["Fusion", "Other"], value="Fusion")
        ui.checkbox("Use standard palette")
        ui.checkbox("Disable widgets")
    ui.separator()
    with ui.grid(columns=2):
        with ui.column():
            ui.label("Box 1")
            ui.radio(["Radio button 1"])
            ui.radio(["Radio button 2"])
            ui.radio(["Radio button 3"])
            ui.checkbox("Tri-state check box")
        with ui.column():
            ui.label("Box 2")
            my_button = ui.button("Default button")
            ui.button("Flat button").props("flat")
            ui.button("Disabled button").disable()
        with ui.column():
            with ui.tabs().classes("w-full") as tabs:
                one = ui.tab("One")
                two = ui.tab("Two")
            with ui.tab_panels(tabs, value=two).classes("w-full"):
                with ui.tab_panel(one):
                    ui.label("Table")
                    ui.table.from_pandas(pd.DataFrame(np.random.randint(0, 5, (4, 4))))
                with ui.tab_panel(two):
                    ui.label("Text edit")
                    ui.textarea()
        with ui.row():
            ui.slider(min=0, max=50, value=25).props("vertical")
            with ui.column():
                ui.checkbox("Group 3")
                ui.input("password", password=True)
                ui.slider(min=0, max=50, value=0)
                with ui.input("Date") as date:
                    with ui.menu().props("no-parent-event") as menu:
                        with ui.date().bind_value(date):
                            with ui.row().classes("justify-end"):
                                ui.button("Close", on_click=menu.close).props("flat")
                    with date.add_slot("append"):
                        ui.icon("edit_calendar").on("click", menu.open).classes(
                            "cursor-pointer"
                        )
                ui.knob(0.5, min=0.1, max=0.9, show_value=True)
    ui.linear_progress(0.5)


ui.run(title="Styles")
