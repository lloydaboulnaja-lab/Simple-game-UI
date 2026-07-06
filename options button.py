set_image = CTkImage(light_image=Image.open("SETTINGS.png"),
                                  dark_image=Image.open("SETTINGS.png"),
                                  size=(200,200))


options_button = CTkButton(master=window,text='',command=options,image=set_image,fg_color='transparent')
options_button.place(relx=0.2,rely=0.5)
