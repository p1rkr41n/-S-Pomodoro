#f __name__ == "__main__":
def Pomodoro(time):
    if time == 0:
        return 25*60
    elif time > 120:
        return 25*60
    return time*60
