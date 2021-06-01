#if __name__ == "__main__":
def LongRelax(time):
    if time == 0:
        return 25*60
    elif time > 60:
        return 25*60
    return time*60
