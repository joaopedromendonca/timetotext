# Receives a list of reviews(lists) containing the restaurant id and the grade, returns the best evaluated place id, if there is a tie, the lowest id will be returned.

def best_review(ratings):
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

best_review(5,ratings)

