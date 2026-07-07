import flet as ft

class CalculatorApp:
    def __init__(self):
        self.expression = ""
        # Дисплей результата
        self.result_display = ft.Text(value="0", size=48, text_align=ft.TextAlign.RIGHT)

    def main(self, page: ft.Page):
        page.title = "Калькулятор"
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.padding = 20

        def on_button_click(e):
            btn_text = e.control.content.value

            if btn_text == "AC":
                self.expression = ""
                self.result_display.value = "0"
                page.update()
                return

            if btn_text == "=":
                try:
                    result = str(eval(self.expression))
                    self.result_display.value = result
                    self.expression = result
                except Exception:
                    CalculatorApp.show_error(page, "Ошибка вычисления")
                    self.result_display.value = "Ошибка"
                page.update()
                return

            self.expression += btn_text
            self.result_display.value = self.expression
            page.update()

        # Раскладка кнопок
        buttons_layout = [
            ["AC", "+/-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        rows = []
        for row in buttons_layout:
            row_controls = []
            for label in row:
                btn = ft.ElevatedButton(
                    content=ft.Text(label, size=20),
                    expand=True,
                    on_click=on_button_click,
                    style=ft.ButtonStyle(padding=0)  # чтобы кнопки были аккуратнее
                )
                row_controls.append(btn)
            rows.append(ft.Row(controls=row_controls, expand=True))

        # Тут самое важное: вместо ft.colors.SURFACE_VARIANT ставим просто строку цвета
        page.add(
            ft.Container(
                content=self.result_display,
                padding=15,
                bgcolor="grey200",          # <-- вот это исправили
                border_radius=10,
                expand=False
            ),
            ft.Column(controls=rows, spacing=8, expand=True)
        )

    @staticmethod
    def show_error(page: ft.Page, message: str):
        snackbar = ft.SnackBar(
            content=ft.Text(message, color="white"),
            bgcolor="red",
            open=True
        )
        page.snack_bar = snackbar
        page.update()


if __name__ == "__main__":
    # Запускаем в браузере, чтобы не было проблем с SSL и скачиванием движка
    ft.run(CalculatorApp().main, view=ft.AppView.WEB_BROWSER)
