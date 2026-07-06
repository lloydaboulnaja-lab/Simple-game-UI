play_image = CTkImage(light_image=Image.open("PLAY.png"),
                                  dark_image=Image.open("PLAY.png"),
                                  size=(200, 200))

play_button = CTkButton(master=window,text="",command=play,image=play_image,fg_color='transparent')
play_button.place(relx=0.2,rely=0.3)
