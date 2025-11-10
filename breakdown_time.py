def breakdown_time(seconds):

    if not isinstance(seconds, int) or seconds < 0:
        return -1
    
    if seconds == 0:
        return {}
    

    hours = seconds // 3600
    remainingseconds = seconds % 3600
    minutes = remainingseconds // 60
    realremainingseconds = remainingseconds % 60
    
    finaldict = {} 
    
    if hours > 0:
        finaldict[3600] = hours
        
    if minutes > 0:
        finaldict[60] = minutes
        
    if realremainingseconds > 0:
        finaldict[1] = realremainingseconds
    
    return finaldict