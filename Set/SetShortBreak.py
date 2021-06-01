#if __name__ == "__main__":
def ShortRelax(time):
    if time == 0:
        return 5*60
    elif time > 30:
        return 5*60
    return time*60
