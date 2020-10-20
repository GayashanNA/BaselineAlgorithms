from functools import total_ordering

"""
Implements the IoT Task placement algorithm by Taneja et al.

[1] Taneja, M., Davy, A.: Resource aware placement of IoT application modules in fog-cloud computing paradigm. 
In: IFIP/IEEE Symp. on Integrated Net. and Service Mgmt (IM) (May 2017).
"""


@total_ordering
class NetworkNode:
    def __init__(self, node_id, cpu, ram, bandwidth):
        self.node_id = node_id
        self.cpu = cpu
        self.ram = ram
        self.bandwidth = bandwidth

    def __str__(self):
        return f'{self.node_id} {self.cpu} {self.ram} {self.bandwidth}'

    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        return score(self) == score(other)

    def __lt__(self, other):
        return score(self) < score(other)


@total_ordering
class AppModule:
    def __init__(self, module_id, cpu, ram, bandwidth):
        self.module_id = module_id
        self.cpu = cpu
        self.ram = ram
        self.bandwidth = bandwidth

    def __str__(self):
        return f'{self.module_id} {self.cpu} {self.ram} {self.bandwidth}'

    def __hash__(self):
        return hash(self.module_id)

    def __eq__(self, other):
        return score(self) == score(other)

    def __lt__(self, other):
        return score(self) < score(other)


def score(e):
    return e.cpu * e.ram * e.bandwidth


def sort_list(elements):
    from sortedcontainers import SortedList
    return SortedList(elements)


def compare(network_node, app_module):
    if network_node.cpu >= app_module.cpu and network_node.ram >= app_module.ram and network_node.bandwidth >= app_module.bandwidth:
        return 1
    return -1


def lower_bound(network_nodes, app_module, low, high):
    length = len(network_nodes)
    mid = (low + high) // 2
    while True:
        x = network_nodes[mid]
        if compare(x, app_module) == 1:
            high = mid - 1
            if high < low:
                return mid
        else:
            low = mid + 1
            if low > high:
                if mid < (length - 1):
                    return mid + 1
                return -1
        mid = (low + high) // 2


def place_module_on_node(mapped_modules, network_node, module):
    network_node = update_capacity(network_node, module)
    if network_node not in mapped_modules:
        mapped_modules[network_node] = [module]
    else:
        mapped_modules[network_node].append(module)
    return mapped_modules


def update_capacity(network_node, app_module):
    network_node.cpu -= app_module.cpu
    network_node.ram -= app_module.ram
    network_node.bandwidth -= app_module.bandwidth
    print(network_node.cpu, network_node.ram, network_node.bandwidth)
    return network_node


def module_map(network_nodes, app_modules):
    sorted_network_nodes = sort_list(network_nodes)
    sorted_app_modules = sort_list(app_modules)
    mapped_modules = {}
    low = 0
    high = len(sorted_network_nodes) - 1
    num_modules = len(sorted_app_modules)
    num_network_nodes = len(sorted_network_nodes)
    mapped_modules_count = 0
    for start in range(0, num_modules):
        i = lower_bound(sorted_network_nodes, sorted_app_modules[start], low, high)
        if i != -1:
            mapped_modules = place_module_on_node(mapped_modules, sorted_network_nodes[i], sorted_app_modules[start])
            sorted_network_nodes = sort_list(sorted_network_nodes)
            low = i + 1
        else:
            mapped_modules = place_module_on_node(mapped_modules, sorted_network_nodes[num_network_nodes - 1],
                                                  sorted_app_modules[start])

    for _, modules in mapped_modules.items():
        mapped_modules_count += len(modules)

    if num_modules > mapped_modules_count:
        print('Unable to map all the modules to the network nodes.')
    return mapped_modules
