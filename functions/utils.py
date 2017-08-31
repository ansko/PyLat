def orderParameter(cosTheta):
    return (3 * cosTheta**2 - 1) / 2


def clayRanges(systemName):
    if systemName == 'mixed':
        return (4.8, 12.5)
    elif systemName == 'segregated':
        return (51.7, 59.4)
    return None