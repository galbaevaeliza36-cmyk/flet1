import flet as ft
from datetime import datetime, timezone, timedelta





def main (page:ft.Page):
    text_hello=ft.Text(value="Hello world")
    page.theme_mode = ft.ThemeMode.DARK
    text_hello.value = "Hello"
    greeting_history=[]
    history_text = ft.Text("История привествий:")

    def text_name(e):
        print(name_input.value)
        tz = timezone(timedelta(hours=6))
        now = datetime.now(tz)
      

        text_hello.value=f"{now.strftime("%Y-%m-%d %H:%M:%S")} hello {name_input.value}"
        name_input.value=None

        greeting_history.append(name)
        print(greeting_history)
        history_text.value = "История привествий :\n" +",\n".join(greeting_history)
        ""
    def change_theme(e):
        if page.theme_mode==ft.ThemeMode.DARK:
           page.theme_mode=ft.ThemeMode.LIGHT
        else:
            page.theme_mode=ft.ThemeMode.DARK

    def clear_history(_):
        print(greeting_history)
        greeting

    

    # text_button=ft.TextButton("SEND")
    elevated_button=ft.ElevatedButton("send", on_click=text_name)
    # icon_button=ft.IconButton(icon=ft.Icons.SEND)
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=change_theme)
    name_input = ft.TextField(label="Введите что нибудь",on_submit=text_name)  #label-подсказка в поле ввода


    #добоаление в страницу
    page.add(text_hello, elevated_button, name_input,thememode_button )

ft.app(target=main)