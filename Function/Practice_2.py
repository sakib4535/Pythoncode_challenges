def banner_text(text, screen_width):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        center_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(center_text)
        print(output_string)

banner_text("*", 56)
banner_text("Always look on the bright side of life...", 56)
banner_text("If life seems jolly rotten,", 56)
banner_text("There's something you've forgotten!", 56)
banner_text("And that's to laugh and smile and dance and sing,", 56)
banner_text(" ", 56)
banner_text("When you're feeling in the dumps,", 56)
banner_text("Don't be silly chumps,", 56)
banner_text("Just purse your lips and whistle - that's the thing!", 56)
banner_text("And... always look on the bright side of life...", 56)
banner_text("*", 56)