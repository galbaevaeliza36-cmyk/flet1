import flet as ft 


def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text('История приветствий:')

   
    MAX_HISTORY = 5
    favorite_names = []
    last_name = ""
    favorite_text = ft.Text("Любимые:")


    def text_name(_):
        nonlocal last_name  
        name = name_input.value.strip()

        if name:
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = None

            last_name = name 

            greeting_history.append(name)
            greeting_history[:] = greeting_history[-MAX_HISTORY:]  

            history_text.value = ( 'История приветствий:\n' + '\n'.join(greeting_history))
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

        page.update() 

    elevated_button = ft.ElevatedButton('send',on_click=text_name,icon=ft.Icons.SEARCH,color=ft.Colors.RED,icon_color=ft.Colors.BLACK )

    name_input = ft.TextField(label='Введите что-нибудь', on_submit=text_name, expand=True)


    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

        page.update() 


    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)


    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update() 

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    main_object = ft.Row([name_input, elevated_button, thememode_button, clear_button])
    def add_to_favorite(_):
        if last_name and last_name not in favorite_names:
            favorite_names.append(last_name)
            favorite_text.value = (
                "Любимые:\n" +
                '\n'.join(favorite_names)
            )
            page.update()

    favorite_button = ft.IconButton(
        icon=ft.Icons.STAR,
        tooltip="Добавить в избранное",
        on_click=add_to_favorite
    )

    history_row = ft.Row([history_text, favorite_button])
   

    page.add(text_hello, main_object, history_text,history_row, favorite_text)

    


ft.app(target=main, view=ft.WEB_BROWSER)

