
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
    (13, 2), (13, 3),
    
    (14, 2)]


#starting board is (8, 4)
#max distance is 10
def rawfunc(passengers = passen, res = res):
    # passengers is the # on people to be boarded
    # prio is the # of priority passengers in the list of passengers
    for r in passengers:
        if r[0] == 'p':
            max_dist = [0, [0,0]]
            min_dist = [99999, [0,0]]
            for i in prio_seats:
                for e in ent:
                    x = get_seat(e, i)
                    if max_dist[0] < x:
                        max_dist[0] = x
                        max_dist[1] = i
                    elif min_dist[0] > x:
                        min_dist[0] = x
                        min_dist[1] = i
            if r[1] <= 5:
                res[min_dist[1][0]][min_dist[1][1]] = r
                x = prio_seats.index((min_dist[1][0],min_dist[1][1]))
                prio_seats.pop(x)
            else:
                res[max_dist[1][0]][max_dist[1][1]] = r
                x = prio_seats.index((max_dist[1][0],max_dist[1][1]))
                prio_seats.pop(x)
            #print(res, prio_seats)
        else:
            max_dist = [0, [0,0]]
            min_dist = [99999, [0,0]]
            #print('pass')
            if seats:
                for i in seats:
                    for e in ent:
                        x = get_seat(e, i)
                        if max_dist[0] < x:
                            max_dist[0] = x
                            max_dist[1] = i
                        elif min_dist[0] > x:
                            min_dist[0] = x
                            min_dist[1] = i
                if r[1] <= 5:
                    res[min_dist[1][0]][min_dist[1][1]] = r
                    x = seats.index((min_dist[1][0],min_dist[1][1]))
                    seats.pop(x)
                else:
                    res[max_dist[1][0]][max_dist[1][1]] = r
                    x = seats.index((max_dist[1][0],max_dist[1][1]))
                    seats.pop(x)
                #print(res)
            else: 
                for i in stand:
                    for e in ent:
                        x = get_seat(e, i)
                        if max_dist[0] < x:
                            max_dist[0] = x
                            max_dist[1] = i
                        elif min_dist[0] > x:
                            min_dist[0] = x
                            min_dist[1] = i
                if r[1] <= 5:
                    res[min_dist[1][0]][min_dist[1][1]] = r
                    x = stand.index((min_dist[1][0],min_dist[1][1]))
                    stand.pop(x)
                else:
                    res[max_dist[1][0]][max_dist[1][1]] = r
                    x = stand.index((max_dist[1][0],max_dist[1][1]))
                    stand.pop(x)
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
    c = 0
    for r in passengers:
        if r[0] == 'p':
            max_dist = [0, [0,0]]
            min_dist = [99999, [0,0]]
            for i in list(prio_seats):
                for e in ent:
                    x = get_seat(e, i)
                    if max_dist[0] < x:
                        max_dist[0] = x
                        max_dist[1] = i
                    elif min_dist[0] > x:
                        min_dist[0] = x
                        min_dist[1] = i
            if r[1] <= 5:
                seat = (min_dist[1][0], min_dist[1][1])
                if seat in prio_seats:
                    prio_seats.remove(seat)
                g.center.after(1000, g.create_passenger, ent[c], seat, r)
            else:
                seat = (max_dist[1][0], max_dist[1][1])
                if seat in prio_seats:
                    prio_seats.remove(seat)
                g.center.after(1000, g.create_passenger, ent[c], seat, r)
            if c < 3: c+=1 
            else: c=0
            #print(res, prio_seats)
        else:
            max_dist = [0, [0,0]]
            min_dist = [99999, [0,0]]
            #print('pass')
            if seats:
                for i in list(seats):
                    for e in ent:
                        x = get_seat(e, i)
                        if max_dist[0] < x:
                            max_dist[0] = x
                            max_dist[1] = i
                        elif min_dist[0] > x:
                            min_dist[0] = x
                            min_dist[1] = i
                if r[1] <= 5:
                    seat = (min_dist[1][0], min_dist[1][1])
                    if seat in seats:
                        seats.remove(seat)
                    g.center.after(1000, g.create_passenger, ent[c], seat, r)
                else:
                    seat = (max_dist[1][0], max_dist[1][1])
                    if seat in seats:
                        seats.remove(seat)
                    g.center.after(1000, g.create_passenger, ent[c], seat, r)
                if c < 3: c+=1 
                else: c=0
                #print(res)
            else: 
                for i in list(stand):
                    for e in ent:
                        x = get_seat(e, i)
                        if max_dist[0] < x:
                            max_dist[0] = x
                            max_dist[1] = i
                        elif min_dist[0] > x:
                            min_dist[0] = x
                            min_dist[1] = i
                if r[1] <= 5:
                    seat = (min_dist[1][0], min_dist[1][1])
                    if seat in stand:
                        stand.remove(seat)
                    g.center.after(1000, g.create_passenger, ent[c], seat, r)
                else:
                    seat = (max_dist[1][0], max_dist[1][1])
                    if seat in stand:
                        stand.remove(seat)
                    g.center.after(1000, g.create_passenger, ent[c], seat, r)
                if c < 3: c+=1 
                else: c=0
    #print(res)
                


def get_seat(pos, seatpos):
    return get_dist(pos[0], pos[1], seatpos[0], seatpos[1])

#Manhattan distance
def get_dist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)
