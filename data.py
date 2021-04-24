import random
def datap(message):
    random_no = random.randrange(3)
    if "how are you" in str(message).lower():
        if random_no == 0:
            return "fine and you :D?"
        elif random_no == 1:
            return "ummm....i m fine"
        elif random_no == 2:
            return "good at all"
        else:
            return "absoutely fine :D"

    elif "where are you?" in str(message).lower():
        return "at my home and you:D"
    elif "i am also in home" in str(message).lower():
        return "okay:D"
    elif "bye" in str(message).lower():
        return "bye take care :D"
    # You can add data here using elif ladder
    else:
        return "  "



