usb_size_input = 1
memes_list = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12),
        ]


def greedy_algorithm(usb_size, memes):
    """
    Function that solves rucksack problem in greedy way. Calculates the most cost-effective packing memes into usb
    :param usb_size: int that is size of usb in GiBs
    :param memes: list of tuples where every tuple is different memes_chooser. Tuples indexes are name, size of memes_chooser in MiB(int),
                                                                                                    value of memes_chooser
                    [(name, size of memes_chooser in MiB (int), value of memes_chooser
    :return: (sum of memes values, {set of memes which are the best options due to usb_size})
    """
    usb_size = usb_size*1024
    usb = []
    values = []
    usb_size_taken = 0
    for i, meme in enumerate(memes):
        name, size, value = meme
        memes[i] = name, size, value, value/size
    sorted_memes = sorted(memes, key=lambda wage: wage[3], reverse=True)
    for meme in sorted_memes:
        if meme[1] + usb_size_taken <= usb_size:
            usb_size_taken += meme[1]
            values.append(meme[2])
            usb.append(meme[0])

    return sum(values), set(usb)


print(greedy_algorithm(usb_size_input, memes_list))
