import utility as utility
import loader as loader
import numpy as np


def main():

    # Paths to the data and solution files.
    vrp_file = "data/n32-k5.vrp"  # "data/n80-k10.vrp"
    sol_file = "data/n32-k5.sol"  # "data/n80-k10.sol"

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)

    # Displaying to console the distance and visualizing the optimal VRP solution.
    vrp_best_sol = loader.load_solution(sol_file)
    best_distance = utility.calculate_total_distance(vrp_best_sol, px, py, depot)
    print("Best VRP Distance:", best_distance)
    utility.visualise_solution(vrp_best_sol, px, py, depot, "Optimal Solution")

    # Executing and visualizing the nearest neighbour VRP heuristic.
    # Uncomment it to do your assignment!

    nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!
    
    # sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    # sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    # print("Saving VRP Heuristic Distance:", sh_distance)
    # utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")


def nearest_neighbour_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for the nearest neighbour heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Nearest Neighbour Heuristic to generate VRP solutions.

    #initilise a solution 
    #Append nearest feasible node to the end of current route
    #   Must be univisited, After inserting, route cost should not exceed capacity
    #if none is found return to depot and create a new route

    routes = [[]]
    visited = list()
    nodes = list()
    for node in range(len(px)):
        nodes.append(node)

    current_route = 0
    routes[current_route].insert(0,depot)
    for node in nodes:
       
        if(len(visited) != len(nodes)):

            if(visited.count(node)==0):
                nearest_node = find_nearest_neighbour(px,py,node)
                routes[current_route].append(nearest_node)
                visited.append(nearest_node)
            if(find_route_demand(demand)>capacity):
                visited.remove(nearest_node)
                routes[current_route].remove(nearest_node)
                current_route+=1
                routes[current_route].insert(depot,0)

    return routes

def find_route_demand(demand):
    total_demand = 0;

    for value in demand:
        total_demand+=value

    return total_demand

def find_nearest_neighbour(px, py, node):
    nearest_node = 0
    distance  = 999999


    for node1 in range(len(px)):
        euclidean_distance = utility.calculate_euclidean_distance(px,py,node,node)
        if(euclidean_distance<distance):
            distance = euclidean_distance
            nearest_node = node1

    return nearest_node


def savings_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for Implementing the savings heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Saving Heuristic to generate VRP solutions.

    return None


if __name__ == '__main__':
    main()
