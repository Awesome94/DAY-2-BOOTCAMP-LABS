def find_missing(alist1, alist2):
    if len(alist1) == 0 and len(alist2) == 0:
        return 0
    elif len(alist1) == len(alist2):
        for num in alist1:
            if num in alist2:
                return 0
    else:
        if len(alist1) < len(alist2):
            for num in alist2:
                if num not in alist1:
                    return num
                elif len(alist2) < len(alist1):
                    for num in alist1:
                        if num not in alist2:
                            return num
