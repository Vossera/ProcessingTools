# encoding=gbk
import flet as ft

def main(page: ft.Page):
    destinations = [
        ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Home"),
        ft.NavigationBarDestination(icon=ft.icons.SETTINGS_ROUNDED, label="Settings"),
    ]
    
    home_view = ft.Container(content=ft.Text("这是主页"), visible=True)
    settings_view = ft.Container(content=ft.Text("这是设置页"), visible=False)
    views = [home_view, settings_view]
    
    nav_bar = ft.NavigationBar(
        destinations=destinations,
        on_change=lambda e: on_nav_change(e, views, page)
    )
    
    page.title = "Flet Navigation Bar Example"
    page.navigation_bar = nav_bar
    
    page.add(home_view)
    page.add(settings_view)
    
    page.update()

def on_nav_change(e, views, page):
    for i, view in enumerate(views):
        view.visible = (i == e.control.selected_index)
    page.update()

ft.app(target=main)