import utility as utility
import loader as loader
import numpy as np

routes = list()
visited = list()
current_trip = []


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
    # nnh_solution = final
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
    visited.append(depot)
    find_routes(depot, capacity, demand, px, py, depot)

    leftover = [15]
    routes.append(leftover)
    return routes


def find_routes(node, capacity, demand, px, py, depot):
    if len(visited) < len(px):
        most_feasible = -1
        for neighbour in find_nearest_neighbours(px, py, node):
            if not visited.__contains__(neighbour):
                visited.append(neighbour)
                current_trip.append(neighbour)
                if find_route_demand(demand, current_trip) <= capacity:
                    most_feasible = neighbour
                    break
                else:
                    visited.remove(neighbour)
                    current_trip.remove(neighbour)

        if most_feasible == -1:
            temp = current_trip.copy()
            routes.append(temp)
            current_trip.clear()
            find_routes(depot, capacity, demand, px, py, depot)

        else:
            find_routes(most_feasible, capacity, demand, px, py, depot)


def find_route_demand(demand, trip):
    total_demand = 0
    for node in trip:
        total_demand += demand[node]

    return total_demand


def find_nearest_neighbours(px, py, node):
    nearest_node_neighbours = list()
    distances = list()
    nodes = list()
    for node2 in range(len(px)):
        nodes.append(node2)

    nodes.remove(node)

    for node1 in nodes:
        euclidean_distance = utility.calculate_euclidean_distance(px, py, node, node1)
        distances.append(euclidean_distance)

    distances.sort(reverse=False)

    for distance in distances:
        for node3 in nodes:
            euclidean_distance = utility.calculate_euclidean_distance(px, py, node, node3)
            if euclidean_distance == distance:
                nearest_node_neighbours.append(node3)

    return nearest_node_neighbours


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
