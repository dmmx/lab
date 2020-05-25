
example_3_9 = [1,4,6,13,16,17,18,19,19,22,24,26,28,29,34,36,38,42,45,53,56,64,73,81,94]

example_3_10 = [1,4,6,13,16,17,18,19,19,22,24,26,28,29,34,36,38,42,45,53,56,64,73,81,94,104]

def median_loc(data):
    return (len(data) + 1) / 2

def median(data):
    loc = median_loc(data)
    if len(data)/2 == 0:
        return data[int(loc) -1]
    else:
        a = int(loc) - 1
        b = int(loc)
        return (data[a] + data[b])/2

def mean(data):
    return sum(data) / len(data)

def quartile_loc(data):
    return (int(median_loc(data)) + 1) / 2

def quartile1(data):
    loc = int(quartile_loc(data))
    return data[loc - 1]

def quartile3(data):
    loc = int(quartile_loc(data))
    return data[len(data) - loc]

def eighths_loc(data):
    return (int(quartile_loc(data)) + 1) / 2

def eighths1(data):
    loc = int(eighths_loc(data))
    return data[loc - 1]

def eighths7(data):
    loc = int(eighths_loc(data))
    return data[len(data) - loc]

def quantile_summary(data):
    mloc = median_loc(data)
    qloc = quartile_loc(data)
    eloc = eighths_loc(data)
    med = median(data)
    q1 = quartile1(data)
    q3 = quartile3(data)
    e1 = eighths1(data)
    e7 = eighths7(data)
    midQ = mean([q1,q3])
    midE = mean([e1,e7])
    midR = mean([min(data), max(data)])

    col1_lengths = [len(f"M({mloc})"), len(f"Q({qloc})"), len(f"E({eloc})")]
    max_length = max(col1_lengths)
    n_str = " " * max_length
    divider = " " * max_length
    mloc_str = f"M({mloc})".rjust(max_length)
    qloc_str = f"Q({qloc})".rjust(max_length)
    eloc_str = f"E({eloc})".rjust(max_length)
    r_str = "R".rjust(max_length)

    col2_lengths = [len(f"{q1}"), len(f"{e1}"), len(f"{min(data)}")]
    max_length = max(col2_lengths)
    med_str = (" " * max_length) + f"{med}"
    med_spacer = int(len(f"{med}")/2) - int(len(f"{len(data)}")/2)
    n_str = (" " * (max_length + 3 + med_spacer)) + n_str + f"{len(data)}"
    q1_str = f"{q1}".rjust(max_length)
    e1_str = f"{e1}".rjust(max_length)
    r1_str = f"{min(data)}".rjust(max_length)
    spacer = " " * len(str(med))

    col3_lengths = [len(f"{q3}"), len(f"{e7}"), len(f"{max(data)}")]
    max_length = max(col3_lengths)
    med_str = med_str + (" " * max_length)
    n_str = n_str  + (" " * max_length)
    q3_str = f"{q3}".rjust(max_length)
    e7_str = f"{e7}".rjust(max_length)
    r2_str = f"{max(data)}".rjust(max_length)

    #print(f"{len(data)} Midsummaries")

    divider = divider + " +-" + ("-" * len(med_str)) + "-+"
    
    line1 = f"{mloc_str} | {med_str} |"
    line2 = f"{qloc_str} | {q1_str}{spacer}{q3_str} |"
    line3 = f"{eloc_str} | {e1_str}{spacer}{e7_str} |"
    line4 = f"{r_str} | {r1_str}{spacer}{r2_str} |"

    print(n_str + "    Midsummaries")
    print(divider)
    


    line1 = f"{mloc_str} | {med_str} | {med}"
    line2 = f"{qloc_str} | {q1_str}{spacer}{q3_str} | {midQ}"
    line3 = f"{eloc_str} | {e1_str}{spacer}{e7_str} | {midE}"
    line4 = f"{r_str} | {r1_str}{spacer}{r2_str} | {midR} "


    for line in [line1, line2, line3, line4]:
        print(line)
    



