def get_index_different_char(chars):
    an=0
    for char in chars:
        an+=1 if str(char).isalnum() else -1
    for i, char in enumerate(chars):
        if an>0:
            if not str(char).isalnum():
                return (i)
        else:
            if str(char).isalnum():
                return (i)
