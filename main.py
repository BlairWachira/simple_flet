import flet as ft

def main(page: ft.Page):
    page.title = "Login UI"
    page.bgcolor = "#f0f2f5"
    page.window_width = 900
    page.window_height = 600

    def go_to_dashboard():
        page.clean()  # Clear the login page

        # Dashboard content
        page.title = "Welcome Dashboard"
        page.bgcolor = "#ffffff"

        page.add(
            ft.Column([
                ft.Text("🎉 Welcome, Admin!", size=30, weight="bold", color="green"),
                ft.Image(
                    src="https://images.unsplash.com/photo-1518770660439-4636190af475",
                    width=400,
                    height=300,
                    fit=ft.ImageFit.COVER
                ),
                ft.Text("You're now logged in to your secure dashboard.",
                        size=18, italic=True, color="black"),
                ft.ElevatedButton("Logout", on_click=lambda e: page.go("/"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
            )
        )

    # TextFields for login
    email_field = ft.TextField(label="Email address", value="admin")
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True)

    def handle_login(e):
        if email_field.value == "admin" and password_field.value == "1234":
            go_to_dashboard()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Invalid credentials!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # Left Panel
    left_panel = ft.Container(
        content=ft.Column([
            ft.Text("YOUR LOGO", size=20, color="white"),
            ft.Text("Hello,\nwelcome!", size=36, weight="bold", color="white"),
            ft.Text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nPhasellus nisl risus.",
                size=14,
                color="white"
            ),
            ft.ElevatedButton("View more", bgcolor="white", color="blue")
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=True,
        bgcolor=ft.Colors.BLUE_800,
        padding=40
    )

    # Right Panel
    right_panel = ft.Container(
        content=ft.Column([
            email_field,
            password_field,
            ft.Row([
                ft.Checkbox(label="Remember me"),
                ft.Text("Forgot password?", color="blue", size=12)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.ElevatedButton("Login", width=250, on_click=handle_login),
            ft.Text("Not a member yet?"),
            ft.ElevatedButton("Sign up", width=250, bgcolor="blue", color="white")
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=True,
        bgcolor="white",
        padding=40
    )

    # Initial page layout
    page.add(
        ft.Row([left_panel, right_panel], expand=True)
    )

ft.app(target=main, view=ft.WEB_BROWSER)

