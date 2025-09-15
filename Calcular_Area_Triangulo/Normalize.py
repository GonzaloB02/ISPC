def normalize_number(msg_1, msg_2, default_height = '1'):
    base = ''
    height = ''
    base = input(msg_1).strip().replace(",", ".")
    height = input(msg_2).strip().replace(",", ".")

    if not height:
        height = default_height
    
    return base, height