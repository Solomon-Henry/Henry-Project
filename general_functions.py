def min_max(min,max,val):
    ans = val
    if val < min:
        ans = min
    elif val > max:
        ans = max
    return ans