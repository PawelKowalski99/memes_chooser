from itertools import combinations


def inside_calculate(usb, memes, memo_arr):
    """
    Knapsack problem algorithm that returns value and candidates for memes.
    This algorithm is needed to shorten candidates on memes. O(usb*len(memes))
    :param usb: usb_size in MiB
    :param memes: tuple of memes
    :param memo_arr: memoized array [len(memes)+1][usb+1] to make algorithm faster
    :return: (value, (tuple of candidates on memes_chooser to be sold))
    """
    n = len(memes) - 1
    if memo_arr[len(memes)][usb] != [0, []]:
        return memo_arr[len(memes)][usb]
    if usb == 0 or len(memes) == 0:
        result = [0, []]
    elif memes[n][1] > usb:
        result = inside_calculate(usb, memes[:-1], memo_arr)
    else:
        tmpval, name = list(inside_calculate(usb, memes[:-1], memo_arr)), (memes[n][0])
        value, list_memes = tmpval
        tmp2val, name2 = list(inside_calculate(usb - memes[n][1], memes[:-1], memo_arr)),  (memes[n][0])
        value2, list_memes2 = tmp2val
        value2 += memes[n][2]

        if list_memes:
            list_memes = list_memes + " " + name
        else:
            list_memes = name
        if list_memes2:
            list_memes2 = list_memes2 + " " + name2
        else:
            list_memes2 = name2
        if max(value, value2) is value:
            li = list_memes
        elif max(value, value2) is value2:
            li = list_memes2
        result = [max(value, value2), li]
    memo_arr[len(memes)][usb] = result
    return result[0], (result[1])


def delete_unnecessary_memes(value, memes_result, memes_original_list, size):
    """
    Deletes memes which don't comply with requierements
    :param value:
    :param memes_result: (value, (tuple of candidates on memes_chooser to be sold))
    :param memes_original_list: original memes_list
    :param size: usb_size in MiB
    :return: (tuple of memes to be sold)
    """
    memes_original_list = [x for x in memes_original_list if x[0] in set(memes_result)]
    memes_result = []
    for i, meme in enumerate(memes_original_list):
        memes_result.append([i for i in combinations(memes_original_list, len(memes_original_list) - i) if
                             sum([x[2] for x in i]) == value and sum(x[1] for x in i) < size])
        if memes_result[i]:
            return [x[0] for x in memes_result[i][0]]


def calculate(usb_size, memes):
    """
    Calculates memes_chooser seller problem by knapsack problem algorithm and combinations.
    :param usb_size: int max capacity of memes in usb
    :param memes:  list of tuples with memes
    :return: (value, (tuple of memes to be sold))
    """
    memes = list(set(memes))
    usb = usb_size*1024
    memo_arr = [[[0, []] for _ in range(usb + 1)] for _ in range(len(memes) + 1)]
    result = inside_calculate(usb, memes, memo_arr)
    print(result)
    result = result[0], result[1].split(" ")
    memes_list_modified = delete_unnecessary_memes(result[0], result[1], memes, usb)
    return result[0], set(memes_list_modified)