def first_word(s):
    if s.strip() == "":
        return ""
    return s.strip().split()[0]