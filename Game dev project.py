from customtkinter import * 
from PIL import Image

set_appearance_mode('dark')
set_default_color_theme('green')


window = CTk()

window.geometry('500x500')

window.title('Main Menu UI')





def play():
    print('Playing the game!!.')

    window = CTk()
    window.mainloop()
    

def exiting():
    print('Exiting the game!!.')

def options():
    print('Opening the options menu!!.')


play_image = CTkImage(light_image=Image.open("PLAY.png"),
                                  dark_image=Image.open("PLAY.png"),
                                  size=(200, 200))

set_image = CTkImage(light_image=Image.open("SETTINGS.png"),
                                  dark_image=Image.open("SETTINGS.png"),
                                  size=(200,200))

exit_image = CTkImage(light_image=Image.open("EXIT.png"),
                                  dark_image=Image.open("EXIT.png"),
                                  size=(200, 200))

play_button = CTkButton(master=window,text="",command=play,image=play_image,fg_color='transparent')
play_button.place(relx=0.2,rely=0.3)

options_button = CTkButton(master=window,text='',command=options,image=set_image,fg_color='transparent')
options_button.place(relx=0.2,rely=0.5)

exit_button = CTkButton(master=window,text='',command=exiting, image=exit_image,fg_color="transparent")
exit_button.place(relx=0.2,rely=0.7)




window.mainloop()

