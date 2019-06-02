def calculate(usb_size, memes):
    """
    Knapsack problem solved by a bottom-up approach.
    :param usb_size: usb size given in GiB
    :param memes: list of memes in: [(name_meme, size in MiB, value), ...]
    :return: (optimal value, {set of optimal memes to be inside usb})
    """
    memes_number = len(memes)
    memes = list(set(memes))
    usb_size = int(usb_size * 1024)
    value_table = [[0 for _ in range(usb_size + 1)] for _ in range(memes_number + 1)]
    memes_table = [['' for _ in range(usb_size + 1)] for _ in range(memes_number + 1)]

    # Build table value_table[][] in bottom up manner
    for index in range(memes_number + 1):
        for weight in range(usb_size + 1):
            if index == 0 or weight == 0:
                value_table[index][weight] = 0
            elif memes[index - 1][1] <= weight:
                if memes[index - 1][2] + value_table[index - 1][weight - memes[index - 1][1]] \
                        >= value_table[index - 1][weight]:

                    value_table[index][weight] = memes[index - 1][2] + \
                                                 value_table[index - 1][weight - memes[index - 1][1]]

                    memes_table[index][weight] = memes[index - 1][0] + ' ' + \
                                                 memes_table[index - 1][weight - memes[index - 1][1]]
                else:
                    value_table[index][weight] = value_table[index - 1][weight]
                    memes_table[index][weight] = memes_table[index - 1][weight]
            else:
                value_table[index][weight] = value_table[index - 1][weight]
                memes_table[index][weight] = memes_table[index - 1][weight]
    memes_table[memes_number][usb_size] = memes_table[memes_number][usb_size].split(" ")
    memes_table[memes_number][usb_size].remove("")
    return value_table[memes_number][usb_size], set(memes_table[memes_number][usb_size])


print(calculate(1, [('Dick_butt.jpg', 205, 6),
                    ('do_you_even_lift?.gif', 410, 10),
                    ('Deal_With_It.avi', 126, 11),
                    ('Ricardo_Milos.gif', 584, 20),
                    ('homophobic_seal.gif', 320, 25),
                    ('delete_sys32.avi', 175, 16),
                    ('fus_ro_dah.jpg', 105, 10),
                    ('it_is_over_9000.gif', 210, 19),
                    ('Leeroy_jenkins.avi', 105, 14),
                    ('The_cake_is_a_lie.jpg', 265, 9),
                    ('swag.gif', 320, 15),
                    ('duck_face.avi', 635, 11)]))
