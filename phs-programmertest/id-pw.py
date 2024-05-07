def solution(ID, PW):
    ID_chk = False
    PW_lower_chk = False
    PW_upper_chk = False
    PW_num_chk = False
    PW_chk = True
    if " " not in ID:
        ID_chk = True
    PW_arr = [i for i in PW]
    for i in PW_arr:
        if i == ' ':
            PW_chk = False
        if i.islower():
            if PW_lower_chk == False:
                PW_lower_chk = True
        elif i.isupper():
            if PW_upper_chk == False:
                PW_upper_chk = True
        elif i.isdigit():
            if PW_num_chk == False:
                PW_num_chk = True
    print(PW_lower_chk, PW_upper_chk, PW_num_chk)
    if PW_lower_chk == False or PW_upper_chk == False or PW_num_chk == False:
        PW_chk = False

    if ID_chk == False and PW_chk == False:
        print("ID PW UNAVAILABLE")
    elif ID_chk == False:
        print("ID UNAVAILABLE")
    elif PW_chk == False:
        print("PW UNAVAILABLE")
    else:
        print("AVAILABLE")

solution("seongjukang", "goodpassworD1234")
solution("seongju kang","BadIDPW")