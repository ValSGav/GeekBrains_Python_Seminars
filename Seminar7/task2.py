from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):

    # no_circle_orbit = list(filter(lambda x: x[0] != x[1], orbits))
    # index_of_max_orbit = 0
    # square_of_max = no_circle_orbit[0][0] * no_circle_orbit[0][1] * pi
    # for i in range(1, len(no_circle_orbit)):
    #     curr_orbit = no_circle_orbit[i][0] * no_circle_orbit[i][1] * pi
    #     if curr_orbit > square_of_max:
    #         square_of_max = curr_orbit
    #         index_of_max_orbit = i

    # return no_circle_orbit[index_of_max_orbit]

    result_list = [i for i in orbits if i[0] * i[1] * pi == max(map(lambda x: x[0] * x[1] * pi, 
                                                                    filter(lambda x: x[0] != x[1], orbits)))]
    return result_list[0]


print(*find_farthest_orbit(orbits))
