def function(x):
    x = sorted(x)
    n = [x[0]]
    for start, end in x[1:]:
        last_start, last_end = n[-1]
        if(start <= last_end):
            n[-1] = (last_start,max(last_end,end))
        else:
            n.append((start,end))
    return n