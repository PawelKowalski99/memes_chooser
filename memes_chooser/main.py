def calculate(usb_size, memes):
    """
    Knapsack problem solved by a bottom-up approach.
    :param usb_size: usb size given in GiB
    :param memes: list of memes in: [(name_meme, size in MiB, value), ...]
    :return: (optimal value, {set of optimal memes to be inside usb})
    """
    n = len(memes)
    memes = list(set(memes))
    usb_size = int(usb_size*1024)
    value_table = [[0 for _ in range(usb_size + 1)] for _ in range(n + 1)]
    memes_table = [['' for _ in range(usb_size + 1)] for _ in range(n + 1)]

    # Build table value_table[][] in bottom up manner
    for i in range(n + 1):
        for w in range(usb_size + 1):
            if i == 0 or w == 0:
                value_table[i][w] = 0
            elif memes[i - 1][1] <= w:
                value_table[i][w] = max(memes[i - 1][2] + value_table[i - 1][w - memes[i - 1][1]],
                                        value_table[i - 1][w])
                if memes[i - 1][2] + value_table[i - 1][w - memes[i - 1][1]] >= value_table[i - 1][w]:
                    memes_table[i][w] = memes[i - 1][0] + ' ' + memes_table[i - 1][w - memes[i - 1][1]]
                else:
                    memes_table[i][w] = memes_table[i - 1][w]
            else:
                value_table[i][w] = value_table[i - 1][w]
                memes_table[i][w] = memes_table[i - 1][w]
    memes_table[n][usb_size] = memes_table[n][usb_size].split(" ")
    memes_table[n][usb_size].remove("")
    return value_table[n][usb_size], set(memes_table[n][usb_size])