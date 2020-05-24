
example_2_9 = [84,77,59,91,82,62,78,54,74,72,96,65,44,84,76,38,85,76,66,70]

exersise_2_26 = [24,31,54,62,36,28,37,55,18,27,58,32,37,41,55,39,56,42,29,35]

example_3_1 = [60,72,81,93,72,66,71,94,81,76,84,81,82,99,89,78,90,89,79,74]

example_3_2 = [2.2,3.4,3.0,2.6,3.8,1.8,2.8,3.2,3.7,1.4,2.7,3.6,1.9,2.2,3.0,3.3,2.3,1.7,2.6,3.5,3.0,2.9,3.4,3.1,2.4]

example_3_3 = [3,11,14,9,5,6,5,19,4,4,7,2,2,4,10,16,5,2,4,4,1,4,9,6,4,6,1,2,4,5,8,9,3,3,9]

example_3_4 = [-5,+5,-25,+22,+10,+9,-32,-26,+24,-14,-6,+17,-8,-25,+31,-12]

data = example_3_4

def stem_and_leaf_plot(data, ordered=False, vertical=False, double=False, five_stem=False):
    
    plot = {}
    for d in data:
        s = str(d)

        if d < 10:
            s = '0' + s
        
        stem = s[0]
        leaf = s[1]

        if "." in s:
            i = s.index(".")
            stem = s[:i]
            leaf = s[i+1:]

        if five_stem == True:
            if int(leaf) < 2:
                stem = stem + "*"
            elif int(leaf) < 4:
                stem = stem + "t"
            elif int(leaf) < 6:
                stem = stem + "f"
            elif int(leaf) < 8:
                stem = stem + "s"
            else:
                stem = stem + "-"
            
        elif double==True:
            if int(leaf) < 5:
                stem = stem + "*"
            else:
                stem = stem + "-"
        else:
            pass
            
        if stem in plot:
            plot[stem].append(leaf)
        else:
            plot[stem] = [leaf]

    stems = list(plot.keys())

    def stem_sort_val(stem):
        if len(stem) > 1 and stem[-1] == '*':
            return stem[:-1] + "A"
        elif len(stem) > 1 and stem[-1] == 't':
            return stem[:-1] + "B"
        elif len(stem) > 1 and stem[-1] == 'f':
            return stem[:-1] + "C"
        elif len(stem) > 1 and stem[-1] == 's':
            return stem[:-1] + "D"
        elif len(stem) > 1 and stem[-1] == '-':
            return stem[:-1] + "E"
        else:
            return int(stem)
        
    stems.sort(key=stem_sort_val)

    if ordered:
        for stem in stems:
            plot[stem].sort()

    if not vertical:
        for stem in stems:
            
            line = stem + " | "
            for leaf in plot[stem]:
                line += leaf + " "
                
            print(line)
    else:

        max_length = 0
        for leaf in plot.values():
            if len(leaf) > max_length:
                max_length = len(leaf)

        space = " "
        if double==True or five_stem==True:
            space = "  "
            
        for y in range(max_length-1, -1, -1):
            line =""
            for stem in stems:
                # print(y, stem)
                if len(plot[stem])-1 >= y:
                    line += plot[stem][y] + space
                else:
                    line += " " + space
            print(line)

        line=""
        divider = "-"
        divider_scalar = 2
        if double==True or five_stem==True:
            divider_scalar = 3
            
        for i in range(len(stems)*divider_scalar):
            line += divider
        print(line)

        line = ""
        for stem in stems:
            line += stem + " "
        print(line)

            
            
    

    
          
    
    
    
