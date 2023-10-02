import random
import flet as ft

x = "head"
y = "tail"
coin = random.choice ([x,y])

def main (page : ft.Page) :
    page.title = "Coin Flipper"
    page.add(ft.Text(value=coin))
    img1 = ft.Image(
        src=f"E:\CS\haed.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    img2 = ft.Image(
        src=f"E:\CS\htail.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    if coin == x :
        page.add(img1)
    else:
        page.add(img2)
    page.window_width = 200        # window's width is 200 px
    page.window_height = 200       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    
    page.update()
        
ft.app(target=main)
