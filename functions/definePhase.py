def definePhase(systemName, atomNum):
    if systemName == 'mixed' or systemName == 'segregated':
        while atomNum > 3480:
            atomNum -= 3480
        if atomNum < 721:
            return 1
        elif atomNum < 1561:
            return 2
        return 3
    elif systemName == 'PA6x20':
        return 3
    elif systemName == '5x20':
        while atomNum > 3470:
            atomNum -= 3470
        if atomNum < 721:
            return 1
        elif atomNum < 1561:
            return 2
        return 3
    elif systemName == '10x20':
        while atomNum > 5380:
            atomNum -= 5380
        if atomNum < 721:
            return 1
        elif atomNum < 1561:
            return 2
        return 3
    return None