import time
def get_next_node(grid, path, min_path, end_node,pre_move=None):
    cur_node = path[-1]
    if cur_node is end_node:
        return min_path,path[:-1]
    if cur_node.position.x != end_node.position.x:
        right_node = grid[cur_node.position.x + 1][cur_node.position.y]
        path.append(right_node)
        # print("right_node:")
        # print(right_node)
        # print(path)
        # print("--------------------")
        if min_path != [] and len(min_path) <= len(path):
            return min_path, path[:-1]
        else:
            if right_node is end_node:
                if min_path == []:
                    min_path = path
                else:
                    min_path = min_path if len(min_path) <= len(path) else path
                return min_path, path[:-1]
            else:
                if right_node.passable is True:
                    min_path, path = get_next_node(grid,path,min_path,end_node)
            path = path[:-1]
    if cur_node.position.y != end_node.position.y and pre_move != "up":
        down_node = grid[cur_node.position.x][cur_node.position.y + 1]
        path.append(down_node)
        # print("down_node:")
        # print(down_node)
        # print(path)
        # print("--------------------")
        if min_path != [] and len(min_path) <= len(path):
            return min_path, path[:-1]
        else:
            if down_node is end_node:
                # print(123123)
                if min_path == []:
                    min_path = path
                else:
                    min_path = min_path if len(min_path) <= len(path) else path
                return min_path,path[:-1]
            else:
                if down_node.passable is True:
                    min_path, path = get_next_node(grid,path,min_path,end_node,pre_move = "down")
            path = path[:-1]
    # if cur_node.position.x != 0:
    #     left_node = grid[cur_node.position.x - 1][cur_node.position.y]
    #     path.append(left_node)
    #     # print("left_node:")
    #     # print(left_node)
    #     # print(path)
    #     # print("--------------------")
    #     if min_path != [] and len(min_path) <= len(path):
    #         return min_path, path[:-1]
    #     else:
    #         if left_node is end_node:
    #             if min_path == []:
    #                 min_path = path
    #             else:
    #                 min_path = min_path if len(min_path) <= len(path) else path
    #             return min_path, path[:-1]
    #         else:
    #             if left_node.passable is True and not path[:-1].__contains__(left_node):
    #                 min_path, path = get_next_node(grid,path,min_path,end_node)
    #         path = path[:-1]
    if cur_node.position.y != 0 and pre_move != "down":
        up_node = grid[cur_node.position.x][cur_node.position.y - 1]
        path.append(up_node)
        # print("up_node:")
        # print(up_node)
        # print(path)
        # print("--------------------")
        if min_path != [] and len(min_path) <= len(path):
            return min_path, path[:-1]
        else:
            if up_node is end_node:
                if min_path == []:
                    min_path = path
                else:
                    min_path = min_path if len(min_path) <= len(path) else path
                return min_path, path[:-1]
            else:
                if up_node.passable is True:
                    min_path,path = get_next_node(grid,path,min_path,end_node,pre_move = "up")
            path = path[:-1]
    return min_path,path
def find_shortest_path(grid, start_node, end_node):
    # print(grid)
    # print(start_node)
    # print(end_node)
    cur_path = [start_node]
    min_path = []
    pre_move = None
    if start_node is None or end_node is None:
        return []
    else:
        min_path,path = get_next_node(grid, cur_path,min_path,end_node,pre_move)
        return min_path