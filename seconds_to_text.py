def convert(seconds: int) -> str:
    if seconds == 0:
        return "now"

    minutes = 60
    hours = 3600
    days = 86400
    years = 31536000
    
    res = {}
    while seconds > 0:
        #sec
        if seconds == 1:
            res['second'] = 1
            break
        #secs
        if seconds < minutes:
            res['second'] = seconds
            break
        #mins
        if seconds < hours:
            m = seconds // minutes
            res['minute'] = m
            seconds = seconds%minutes
            continue
        #hours
        if seconds < days:
            h = seconds // hours
            res['hour'] = h
            seconds = seconds%hours
            continue
        #days
        if seconds < years:
            d = seconds // days
            res['day'] = d
            seconds = seconds%days
            continue
        #years
        y = seconds // years
        res['year'] = y
        seconds = seconds%years
    
    fstr = ""
    for i,j in enumerate(res):
        if (atual:=i+1) == len(res):
            if res[j] > 1:
                fstr = fstr + f"{res[j]} {j}s"
            else:
                fstr = fstr + f"{res[j]} {j}"
            continue
        if (atual:=i+2) < len(res):
            if res[j] > 1:
                fstr = fstr + f"{res[j]} {j}s, "
            else:
                fstr = fstr + f"{res[j]} {j}, "
            continue 
        if res[j] > 1:
            fstr = fstr + f"{res[j]} {j}s and "
        else:
            fstr = fstr + f"{res[j]} {j} and "
    return(fstr)
    
result = convert(2115731080)
print(result)