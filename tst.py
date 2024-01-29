def solution(seconds):
    rt_mean = dict()
    for j in ratings:
        rt_mean.setdefault(j[0],[]).append(j[1])
    # grade, id
    best = [0,0]
    for i in rt_mean:
        m = sum(rt_mean[i]) / len(rt_mean[i])
        if m > best[0]:
            best[0] = m
            best[1] = i
        if m == best[0]:
            if best[1] > i:
                best[0] = m
                best[1] = i
    return best[1]
    
ratings = [
    [512,2], 
    [123,3], 
    [987,4], 
    [123,5], 
    [321,5],
    [322,5]
]

solution(5,ratings)

def solution2(seconds):
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
        if res['year']
        print(i,j,res[j])
       
    print(res)
    
out_ = solution2(15731080)
print (out_)