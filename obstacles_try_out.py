import random

obstacle_list = []
list_for_x = []
list_for_y = []


def get_all_four_points(x, y):
    """Returns all the other three points of the obstacle"""
    return [
            (x,y),
            (x + 20, y),
            (x + 20, y + 20),
            (x, y + 20),
            (x, y)
            ]

def is_position_blocked(x, y):
    """returns True if position (x,y) falls inside an obstacle."""
    for (x1, y1) in obstacle_list:
    
        # if x in range(x1, x1 + 19) and y in range(y1, y1 + 19):
        if x1 <= x <= x1 + 20 and y1 <= y <= y1 + 20:
            return True
        if get_all_four_points(x1, y1) == get_all_four_points(x, y):
            return True
    return False

def is_path_blocked(x1, y1, x2, y2):#position_x, position_y, new_y, new_x
    # (x1, y1) => position of the robot
    # (x2, y2) => # position of the obstacle
    
    #straight collision
    for x, y in obstacle_list:
        
        if x1 == x2:
            sorted_y = sorted([y1, y2])
            for i in range(sorted_y[0], sorted_y[1] + 1):
                if (x, i) in obstacle_list:
                    zero, one, two, three, four = get_all_four_points(x, i)
                    
                    """
                        zero  =>(x,y)
                        one   =>(x + 18, y)
                        two   =>(x + 18, y + 18)
                        three =>(x, y + 18)
                        four  =>(x, y)
                    """
                    # sorted_val = sorted([two[1], one[1]])
                    if x <= x1 <= (x + 20): #and sorted_val[1] < y2:
                        print("please show me that value:", (x, i))
                        return True

        if y1 == y2:
            sorted_x = sorted([x1, x2])
            for j in range(sorted_x[0], sorted_x[1] + 1):
                if (j, y) in obstacle_list:
                    zero, one, two, three, four = get_all_four_points(j, y)
                    
                    # sorted_val = sorted([two[1], one[1]])
                    if y <= y1 <= (y + 20):
                        print("please show me that value:", (j, y))
                        return True
    return False

def create_obstacles():

    global obstacle_list
    # random_no = random.randrange(0, 120)
    # random_no = 280
    random_no = 210

    for i in range(0, random_no + 1):
        random_num_x = random.randrange(-100, 91, 20)#105 random_num_x = random.randrange(-80, 105, 15) #105
        # random_num_x = random.randrange(-90, 81, 20)#105 random_num_x = random.randrange(-80, 105, 15) #105
        # while random_num_x in range(-20, 21) : #or random_num_x in list_for_x
        #     # print("Do over chief for x:", random_num_x)
        #     # if random_num_x % 15 == 1:
            # random_num_x = random.randrange(-100, 91, 20)#105
            # random_num_x = random.randrange(-90, 81, 20)
            # else:
            #     random_num_x = random.randrange(-85, 85, 30)#105

        random_num_y = random.randrange(-200, 181, 20)#200 random_num_y = random.randrange(-180, 200, 15)#200
        # random_num_y = random.randrange(-190, 171, 20)#200 random_num_y = random.randrange(-180, 200, 15)#200
        # while random_num_y in range(-5, 5):
            # random_num_y = random.randrange(-200, 181, 20)#200
            # random_num_y = random.randrange(-190, 171, 20)#200 random_num_y = random.randrange(-180, 200, 15)#200
        
        list_for_x.append(random_num_x)
        list_for_y.append(random_num_y)

        if not is_position_blocked(random_num_x, random_num_y):
            obstacle_list.append((random_num_x, random_num_y))
    
    no_dups = list(dict.fromkeys(obstacle_list))
    return no_dups

def create_exits():
    
    top_x = (random.randrange(-80, 91, 20), 200) #top x-value, y is always 200
    bottom_x = (random.randrange(-80, 91, 20), -220) #bottom x-value, y is always -200
    right_y = (100, random.randrange(-180, 181, 20)) #left y-value, x is always 100
    left_y = (-120, random.randrange(-180, 181, 20)) #left y-value, x is always -100
    # top_x = (random.randrange(-80, 81, 20), 190) #top x-value, y is always 200
    # bottom_x = (random.randrange(-80, 81, 20), -210) #bottom x-value, y is always -200
    # right_y = (90, random.randrange(-170, 171, 20)) #left y-value, x is always 100
    # left_y = (-110, random.randrange(-170, 171, 20)) #left y-value, x is always -100
    
    return top_x, bottom_x, right_y, left_y

def get_obstacles():
    return create_obstacles()

def clear_globals():
    obstacle_list.clear()