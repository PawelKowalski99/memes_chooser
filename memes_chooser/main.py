def calculate(usb_size, memes):
    """
    Knapsack problem solved by a bottom-up approach.
    :param usb_size: usb size given in GiB
    :param memes: list of memes in: [(name_meme, size in MiB, value), ...]
    :return: (optimal value, {set of optimal memes to be inside usb})
    """
    if len(memes) == 0 or usb_size == 0:
        return "There are no memes inside list or usb size is 0"
    memes_number = len(memes)
    memes = list(set(memes))
    usb_size = int(usb_size * 1024)
    values_table = [[0 for _ in range(usb_size + 1)] for _ in range(memes_number + 1)]
    memes_table = [['' for _ in range(usb_size + 1)] for _ in range(memes_number + 1)]

    # Build table values_table[len(memes)][usb_size] in bottom up approach
    # Build memes_table[len(memes)][usb_size] that follows values_table and adds adequate memes
    for index in range(memes_number + 1):
        for weight in range(usb_size + 1):
            if index == 0 or weight == 0:
                values_table[index][weight] = 0
            elif memes[index - 1][1] <= weight:
                if memes[index - 1][2] + values_table[index - 1][weight - memes[index - 1][1]] \
                        >= values_table[index - 1][weight]:

                    values_table[index][weight] = memes[index - 1][2] + \
                                                 values_table[index - 1][weight - memes[index - 1][1]]

                    memes_table[index][weight] = memes[index - 1][0] + ' ' + \
                                                 memes_table[index - 1][weight - memes[index - 1][1]]
                else:
                    values_table[index][weight] = values_table[index - 1][weight]
                    memes_table[index][weight] = memes_table[index - 1][weight]
            else:
                values_table[index][weight] = values_table[index - 1][weight]
                memes_table[index][weight] = memes_table[index - 1][weight]
    memes_table[memes_number][usb_size] = memes_table[memes_number][usb_size].split(" ")
    memes_table[memes_number][usb_size].remove("")
    return values_table[memes_number][usb_size], set(memes_table[memes_number][usb_size])
