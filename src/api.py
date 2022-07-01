from collections import defaultdict

class ApiError(RuntimeError):
    pass

def openFile(filename):
    '''
    Open file.
    File format: 4 lines per record for date, event type, money delta, and note.
    Such as:
    (file.example, encoding=utf-8)
      (Record 1)
        (ln 1) date1
        (ln 2) event_type1
        (ln 3) money_delta1
        (ln 4) note1
      (Record 2)
        (ln 5) date2
        (ln 6) event_type2
        (ln 7) money_delta2
        (ln 8) note2
    @param filename: File name.
    Returns: data in the format [[date1, event_type1, money_delta1, note1], ...]
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        res = []
        while date := f.readline():
            if (etype := f.readline()) and (mdelta := f.readline()) and (note := f.readline()):
                res.append([date.rstrip('\n'), etype.rstrip('\n'), mdelta.rstrip('\n'), note.rstrip('\n')])
            else:
                raise ApiError('Unexpected EOF at ' + filename)
        return res

def saveFile(filename, data): # Save
    '''
    Save with the same format mentioned in openFile().
    @param filename: File name.
    @param data: Data with the same format returned in openFile().
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        for line in data:
            print(*line, sep='\n', file=f)

def query(data, key):
    return [record for record in data if any(key in x for x in record)] if key else data

def total(data):
    in_total = out_total = 0
    for _, _, mdelta, _ in data:
        mdelta = int(mdelta)
        if mdelta < 0:
            out_total -= mdelta
        else:
            in_total += mdelta
    return in_total, out_total

def totalByEvent(data):
    cnt = defaultdict(lambda: [0, 0])
    for _, event, mdelta, _ in data:
        mdelta = int(mdelta)
        if mdelta < 0:
            cnt[event][1] -= mdelta
        else:
            cnt[event][0] += mdelta
    return cnt

def totalByDate(data):
    cnt = defaultdict(lambda: [0, 0])
    for date, _, mdelta, _ in data:
        mdelta = int(mdelta)
        if mdelta < 0:
            cnt[date][1] -= mdelta
        else:
            cnt[date][0] += mdelta
    return cnt
