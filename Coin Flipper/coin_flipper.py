import random
import flet as ft

x = "Head"
y = "Tail"
coin = random.choice ([x,y])

def main (page : ft.Page) :
    page.tite = "Coin Flipper"
    page.add(ft.Text(value=coin))
    img1 = ft.Image(
        src= r"E:\python apps\flet\flipcoin\haed.jpg" ,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    img2 = ft.Image(
        src=r"E:\python apps\flet\flipcoin\htail.jpg",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    if coin == x :
        page.add(img1)
    else:
        page.add(img2)
    page.window_width = 350        # window's width is 200 px
    page.window_height = 350       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    
    page.update()
        
ft.app(target=main)
