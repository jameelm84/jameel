import flet as ft


def main(page: ft.Page):
    ft.ElevatedButton(text="Click Me")cut
    ft.Row(controls=[10])
    text_element = ft.Text(value="Hi all", color="red", size=20)
    page.add(text_element)


ft.app(target=main)