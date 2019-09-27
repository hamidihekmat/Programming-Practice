

def mixed(type, percipitation, tenp):

    if percipitation <= 2.5:
        if type == 3:
            print('No Action Required!')
        if temp < -10.0:
            pass
        if temp
    elif percipitation >= 2.6 <= 5.0:
        pass
    elif percipitation >= 5.1 <= 15.0:
        pass
    elif percipitation >= 15.1 <= 45.0:
        pass
    else:
        pass



def ice(type, percipitation):
    print(percipitation_type)



if __name__ == '__main__':
    p_t = {1: 'Snow', 2: 'Ice', 3: 'Mixed'}
    percipitation_type = int(input("1. Snow\n 2. Ice\n 3. Mixed\nSelect percipitation type:"))
    if percipitation_type == 1 or percipitation_type == 3:
        percipitation = int(input("Enter depth of {} (cm)".format(p_t[percipitation_type])))
        temp = input("Enter temperature (Celsius)")
        mixed(percipitation_type, percipitation, temp)

    if percipitation_type == 2:
        percipitation = int(input("Enter depth of {} (mm)".format(p_t[percipitation_type])))
        ice(percipitation_type, percipitation, temp)
