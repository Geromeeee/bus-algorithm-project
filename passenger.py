
import copy

passengers = [3, 5, 6, 4, 9, 9, 5, 9, 8, 5, 4, 1, 8, 5, 6, 6, 8, 10, 10, 9, 4, 5, 5, 7, 8, 2, 
              10, 8, 10, 4, 4, 1, 6, 1, 7, 2, 2, 6, 7, 6, 3, 5, 7, 9, 9, 9, 8, 10, 9, 4]
p = [('p', val) for val in passengers[:6]]
r = [('r', val) for val in passengers[6:]]
passen = p + r

rows, cols = 15, 6
row = [0] * cols
res = [copy.deepcopy(row) for _ in range(rows)]

# entrances passengers will come out from
ent = [(0,4), (1,4), (8, 4), (9,4)]
prio_seats = [(7, 0), (7,1), (8,0),(8,1), (9, 0), (9, 1)]
seats = [(2,0), (2, 5), (3,0), (3,5), (4,0), (4,5), (5, 0), (5,5), (6, 0), (6, 5),
        (10, 0), (10, 1), (10, 4), (10, 5),
        (11, 0), (11, 1), (11, 4), (11, 5),
        (12, 0), (12, 1), (12, 4), (12, 5),
        (13, 0), (13, 1), (13, 4), (13, 5),
    
        (14, 0), (14, 1), (14, 2), (14, 4), (14, 5)]

stand = [
    (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 3), (1, 4),
    
    (2, 2), (2, 3),
    (3, 2), (3, 3),
    (4, 2), (4, 3),
    (5, 2), (5, 3),
    (6, 2), (6, 3),
    
    (7, 2), (7, 3),
    
    (8, 2), (8, 3), (8, 4),
    (9, 2), (9, 3), (9, 4),
    
    (10, 2), (10, 3),
    (11, 2), (11, 3),
    (12, 2), (12, 3),
    (13, 2), (13, 3)]

computed_pseats = [] # computed Priority seats
computed_seats = [] # computed Regular seats
computed_stand = [] # conputed Standing seats
#starting board is (8, 4)
#max distance is 10
def rawfunc(passengers = passen, res = res):
    # passengers is the # on people to be boarded
    # prio is the # of priority passengers in the list of passengers
    comp_seats_dist()
    for r in passengers:
        dist = None
        
        if r[0] == 'p':
            if computed_pseats:
                for i in range(0, len(computed_pseats), 2):
                    if r[1] > 5:
                        if dist is None:
                            dist = [computed_pseats[i][0], computed_pseats[i][1]]
                        elif computed_pseats[i][0] > dist[0]:
                            dist = [computed_pseats[i][0], computed_pseats[i][1]]
                    else:
                        if dist is None:
                            dist = [computed_pseats[i+1][0], computed_pseats[i+1][1]]
                        elif computed_pseats[i+1][0] < dist[0]:
                            dist = [computed_pseats[i+1][0], computed_pseats[i+1][1]]
                    
                res[dist[1][0]][dist[1][1]] = r
                #print(r, '( ',dist, ')')
                x = computed_pseats.index(dist)
                if r[1] <= 5:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x-1)
                    #print('popping', x, x-1)
                else:
                    computed_pseats.pop(x+1)
                    computed_pseats.pop(x)
                    #print('popping', x, x+1)
                #print('computed_pseats:', computed_pseats)
            #print(res, prio_seats)
        else:
            #print('pass')
            dist = None
            if computed_seats:
                for i in range(0, len(computed_seats), 2):
                    if r[1] > 5:
                        if dist is None:
                            dist = [computed_seats[i][0], computed_seats[i][1]]
                        elif computed_seats[i][0] > dist[0]:
                            dist = [computed_seats[i][0], computed_seats[i][1]]
                    else:
                        if dist is None:
                            dist = [computed_seats[i+1][0], computed_seats[i+1][1]]
                        elif computed_seats[i+1][0] < dist[0]:
                            dist = [computed_seats[i+1][0], computed_seats[i+1][1]]
                        
                res[dist[1][0]][dist[1][1]] = r

                x = computed_seats.index(dist)
                #print(r, '( ',dist, ')')
                if r[1] <= 5:
                    computed_seats.pop(x)
                    computed_seats.pop(x-1)
                else:
                    computed_seats.pop(x+1)
                    computed_seats.pop(x)
                #print('computed_seats:', computed_seats)
                #print(res)
            else: 
               if computed_stand:
                for i in range(0, len(computed_stand), 2):
                    if r[1] > 5:
                        if dist is None:
                            dist = [computed_stand[i][0], computed_stand[i][1]]
                        elif computed_stand[i][0] > dist[0]:
                            dist = [computed_stand[i][0], computed_stand[i][1]] 
                    else:
                        if dist is None:
                            dist = [computed_stand[i+1][0], computed_stand[i+1][1]]
                        elif computed_stand[i+1][0] < dist[0]:
                            dist = [computed_stand[i+1][0], computed_stand[i+1][1]]
                res[dist[1][0]][dist[1][1]] = r
                x = computed_stand.index(dist)
                #print(r, '( ',dist, ')')
                if r[1] <= 5:
                    computed_stand.pop(x)
                    computed_stand.pop(x-1)
                else:
                    computed_stand.pop(x+1)
                    computed_stand.pop(x)
                    
    #print(res)


def simulate_algo(passengers = passen):
    import sys

    g = sys.modules.get("__main__")
    if g is None or not hasattr(g, "build_window"):
        import grid_sim as g

    if g.center is None:
        g.build_window()
    # working with a 15 x 9 matrix grid
    # r x c
    # entracnes are (8,4), (9, 4), (0,4), (1,4)
    delay = 1000
    comp_seats_dist()
    for r in range(0, len(passengers), 4):
        try:
            if passengers[r][0] == 'p':
                dist = comp_dist(passengers[r][1], 'p')
                x = computed_pseats.index(dist)
                seat = (dist[1][0], dist[1][1])
                if passengers[r][1] <= 5:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x-1) 
                else:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x)
                    
                g.center.after(delay, g.create_passenger, ent[0], seat, passengers[r])
                #print(res, prio_seats)
            else:
                if computed_seats:
                    dist = comp_dist(passengers[r][1], 'r')
                    x = computed_seats.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r][1] <= 5:
                        computed_seats.pop(x)
                        computed_seats.pop(x-1)
                    else:
                        computed_seats.pop(x)
                        computed_seats.pop(x)
                        
                    g.center.after(delay, g.create_passenger, ent[0], seat, passengers[r])
                    #print(res)
                else: 
                    dist = comp_dist(passengers[r][1], 'r')
                    x = computed_stand.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r][1] <= 5:
                        computed_stand.pop(x)
                        computed_stand.pop(x-1)
                    else:
                        computed_stand.pop(x)
                        computed_stand.pop(x)
                        
                    g.center.after(delay, g.create_passenger, ent[0], seat, passengers[r])
        except IndexError:
            pass
        try:
            if passengers[r+1][0] == 'p':
                dist = comp_dist(passengers[r+1][1], 'p')
                x = computed_pseats.index(dist)
                seat = (dist[1][0], dist[1][1])
                if passengers[r+1][1] <= 5:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x-1) 
                else:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x)
                g.center.after(delay, g.create_passenger, ent[1], seat, passengers[r+1])
                #print(res, prio_seats)
            else:
                if computed_seats:
                    dist = comp_dist(passengers[r+1][1], 'r')
                    x = computed_seats.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+1][1] <= 5:
                        computed_seats.pop(x)
                        computed_seats.pop(x-1)
                    else:
                        computed_seats.pop(x)
                        computed_seats.pop(x)
                    g.center.after(delay, g.create_passenger, ent[1], seat, passengers[r+1])
                    #print(res)
                else: 
                    dist = comp_dist(passengers[r+1][1], 'r')
                    x = computed_stand.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+1][1] <= 5:
                        computed_stand.pop(x)
                        computed_stand.pop(x-1)
                    else:
                        computed_stand.pop(x)
                        computed_stand.pop(x)
                    g.center.after(delay, g.create_passenger, ent[1], seat, passengers[r+1])
        except IndexError:
            pass
        try:
            if passengers[r+2][0] == 'p':
                dist = comp_dist(passengers[r+2][1], 'p')
                x = computed_pseats.index(dist)
                seat = (dist[1][0], dist[1][1])
                if passengers[r+2][1] <= 5:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x-1) 
                else:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x)
                g.center.after(delay, g.create_passenger, ent[2], seat, passengers[r+2])
                #print(res, prio_seats)
            else:
                if computed_seats:
                    dist = comp_dist(passengers[r+2][1], 'r')
                    x = computed_seats.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+2][1] <= 5:
                        computed_seats.pop(x)
                        computed_seats.pop(x-1)
                    else:
                        computed_seats.pop(x)
                        computed_seats.pop(x)
                    g.center.after(delay, g.create_passenger, ent[2], seat, passengers[r+2])
                    #print(res)
                else: 
                    dist = comp_dist(passengers[r+2][1], 'r')
                    x = computed_stand.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+2][1] <= 5:
                        computed_stand.pop(x)
                        computed_stand.pop(x-1)
                    else:
                        computed_stand.pop(x)
                        computed_stand.pop(x)
                    g.center.after(delay, g.create_passenger, ent[2], seat, passengers[r+2])
        except IndexError:
            pass
        try:
            if passengers[r+3][0] == 'p':
                dist = comp_dist(passengers[r+3][1], 'p')
                x = computed_pseats.index(dist)
                seat = (dist[1][0], dist[1][1])
                if passengers[r+3][1] <= 5:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x-1) 
                else:
                    computed_pseats.pop(x)
                    computed_pseats.pop(x)
                g.center.after(delay, g.create_passenger, ent[3], seat, passengers[r+3])
                #print(res, prio_seats)
            else:
                if computed_seats:
                    dist = comp_dist(passengers[r+3][1], 'r')
                    x = computed_seats.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+3][1] <= 5:
                        computed_seats.pop(x)
                        computed_seats.pop(x-1)
                    else:
                        computed_seats.pop(x)
                        computed_seats.pop(x)
                    g.center.after(delay, g.create_passenger, ent[3], seat, passengers[r+3])
                    #print(res)
                else: 
                    dist = comp_dist(passengers[r+3][1], 'r')
                    x = computed_stand.index(dist)
                    seat = (dist[1][0], dist[1][1])
                    if passengers[r+3][1] <= 5:
                        computed_stand.pop(x)
                        computed_stand.pop(x-1)
                    else:
                        computed_stand.pop(x)
                        computed_stand.pop(x)
                    g.center.after(delay, g.create_passenger, ent[3], seat, passengers[r+3])
        except IndexError:
            pass

    #print(res)
        delay += 1000


def get_seat(pos, seatpos):
    return get_dist(pos[0], pos[1], seatpos[0], seatpos[1])

#Manhattan distance
def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def comp_seats_dist():
    for i in seats:
        max_dist = [0, [0,0]]
        min_dist = [99999, [0,0]]
        for e in ent:
            x = get_seat(e, i)
            if max_dist[0] < x:
                max_dist[0] = x
                max_dist[1] = i
            if min_dist[0] > x:
                min_dist[0] = x
                min_dist[1] = i
        computed_seats.append(max_dist)
        computed_seats.append(min_dist)
    
    for i in stand:
        max_dist = [0, [0,0]]
        min_dist = [99999, [0,0]]
        for e in ent:
            x = get_seat(e, i)
            if max_dist[0] < x:
                max_dist[0] = x
                max_dist[1] = i
            if min_dist[0] > x:
                min_dist[0] = x
                min_dist[1] = i
        computed_stand.append(max_dist)
        computed_stand.append(min_dist)
    for i in prio_seats:
        max_dist = [0, [0,0]]
        min_dist = [99999, [0,0]]
        for e in ent:
            x = get_seat(e, i)
            if max_dist[0] < x:
                max_dist[0] = x
                max_dist[1] = i

            if min_dist[0] > x:
                min_dist[0] = x
                min_dist[1] = i
        computed_pseats.append(max_dist)
        computed_pseats.append(min_dist)
    #print('Computed Seats:', computed_seats)
    #print('Computed Stand:', computed_stand)
    #print('Computed Priority Seats:', computed_pseats)

def comp_dist(p_dist, type):
    if type == 'p':
        if computed_pseats:
            dist = None
            for i in range(0, len(computed_pseats), 2):

                if p_dist > 5:
                    if dist is None:
                        dist = [computed_pseats[i][0], computed_pseats[i][1]]
                    elif computed_pseats[i][0] > dist[0]:
                        dist = [computed_pseats[i][0], computed_pseats[i][1]]
                else:
                    if dist is None:
                        dist = [computed_pseats[i+1][0], computed_pseats[i+1][1]]
                    elif computed_pseats[i+1][0] < dist[0]:
                        dist = [computed_pseats[i+1][0], computed_pseats[i+1][1]]
    else:
        dist = None
        if computed_seats:
            for i in range(0, len(computed_seats), 2):
                if p_dist > 5:
                    if dist is None:
                        dist = [computed_seats[i][0], computed_seats[i][1]]
                    elif computed_seats[i][0] > dist[0]:
                        dist = [computed_seats[i][0], computed_seats[i][1]]
                else:
                    if dist is None:
                        dist = [computed_seats[i+1][0], computed_seats[i+1][1]]
                    elif computed_seats[i+1][0] < dist[0]:
                        dist = [computed_seats[i+1][0], computed_seats[i+1][1]]
        elif computed_stand:
            for i in range(0, len(computed_stand), 2):
                if p_dist > 5:
                    if dist is None:
                        dist = [computed_stand[i][0], computed_stand[i][1]]
                    elif computed_stand[i][0] > dist[0]:
                        dist = [computed_stand[i][0], computed_stand[i][1]] 
                else:
                    if dist is None:
                        dist = [computed_stand[i+1][0], computed_stand[i+1][1]]
                    elif computed_stand[i+1][0] < dist[0]:
                        dist = [computed_stand[i+1][0], computed_stand[i+1][1]]
    print(dist)      
    return dist
#rawfunc()
print(res)