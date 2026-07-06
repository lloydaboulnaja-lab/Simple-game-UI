exit_image = CTkImage(light_image=Image.open("EXIT.png"),
                                  dark_image=Image.open("EXIT.png"),
                                  size=(200, 200))

exit_button = CTkButton(master=window,text='',command=exiting, image=exit_image,fg_color="transparent")
exit_button.place(relx=0.2,rely=0.7)
