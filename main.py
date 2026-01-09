import flet as ft


def main (page:ft.Page):
    text_hello=ft.Text(value="Hello world", color=ft.Colors.RED_900)

    text_hello.value = "Hello"
    text_hello.color=ft.Colors.GREEN_900

    def text_name(e):
        print(name_input.value)

    

    # text_button=ft.TextButton("SEND")
    elevated_button=ft.ElevatedButton("send", on_click=text_name)
    # icon_button=ft.IconButton(icon=ft.Icons.SEND)

    name_input = ft.TextField(label="Введите что нибудь")  #label-подсказка в поле ввода


    #добоаление в страницу
    page.add(text_hello, elevated_button, name_input)

ft.app(target=main)