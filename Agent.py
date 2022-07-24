class Agent:
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()

        pass

    def move(self, direction):
        # make your next move based on your perception
        # check if the move destination is not blocked
        # if not blocked , move to destination - set new position
        # something like :
        self.set_position(self.get_position() + direction, self.current_state)

        pass

    @staticmethod
    def get_actions():
        actions = []
        # returns a list of valid actions
        return actions

    def bfs(self, environment):
        self.percept(environment)
        # now go on !
        queue = []
        x, y = self.get_position()
        node = x, y
        queue.append(node)
        find = False
        passed = {}
        passed[node] = node
        while len(queue) > 0:
            node = queue.pop(0)
            x, y = node
            new_node = x, y - 1
            if (y - 1 >= 0) and (not self.current_state[x][y - 1].is_blocked()) and (not new_node in passed.keys()):
                queue.append(new_node)
                passed[new_node] = node
                if self.current_state[x][y - 1].isGoal:
                    find = True
                    node = new_node
                    break
            new_node = x + 1, y
            if (x + 1 < len(self.current_state)) and (not self.current_state[x + 1][y].is_blocked()) and (
                    not new_node in passed.keys()):
                queue.append(new_node)
                passed[new_node] = node
                if self.current_state[x + 1][y].isGoal:
                    find = True
                    node = new_node
                    break
            new_node = x, y + 1
            if (y + 1 < len(self.current_state[x])) and (not self.current_state[x][y + 1].is_blocked()) and (
                    not new_node in passed.keys()):
                queue.append(new_node)
                passed[new_node] = node
                if self.current_state[x][y + 1].isGoal:
                    find = True
                    node = new_node
                    break
            new_node = x - 1, y
            if (x - 1 >= 0) and (not self.current_state[x - 1][y].is_blocked()) and (not new_node in passed.keys()):
                queue.append(new_node)
                passed[new_node] = node
                if self.current_state[x - 1][y].isGoal:
                    find = True
                    node = new_node
                    break
            print(queue)
        if find:
            old_node = passed[node]
            x, y = old_node
            while not self.current_state[x][y].isStart:
                environment.colorize(x, y)
                old_node = passed[old_node]
                x, y = old_node

    def dfs(self, environment):
        self.percept(environment)
        # now go on !
        stack = []
        x, y = self.get_position()
        node = x, y
        stack.append(node)
        find = False
        passed = {}
        while len(stack) > 0:
            node = stack.pop(len(stack) - 1)
            x, y = node
            new_node = x, y - 1
            if (y - 1 >= 0) and (not self.current_state[x][y - 1].is_blocked()) and (not new_node in passed.values()):
                stack.append(new_node)
                passed[new_node] = node
                if self.current_state[x][y - 1].isGoal:
                    node = new_node
                    find = True
                    break
            new_node = x + 1, y
            if (x + 1 < len(self.current_state)) and (not self.current_state[x + 1][y].is_blocked()) and (
                    not new_node in passed.values()):
                stack.append(new_node)
                passed[new_node] = node
                if self.current_state[x + 1][y].isGoal:
                    node = new_node
                    find = True
                    break
            new_node = x, y + 1
            if (y + 1 < len(self.current_state[x])) and (not self.current_state[x][y + 1].is_blocked()) and (
                    not new_node in passed.values()):
                stack.append(new_node)
                passed[new_node] = node
                if self.current_state[x][y + 1].isGoal:
                    node = new_node
                    find = True
                    break
            new_node = x - 1, y
            if (x - 1 >= 0) and (not self.current_state[x - 1][y].is_blocked()) and (not new_node in passed.values()):
                stack.append(new_node)
                passed[new_node] = node
                if self.current_state[x - 1][y].isGoal:
                    node = new_node
                    find = True
                    break
            print(stack)
        if find:
            old_node = passed[node]
            x, y = old_node
            while not self.current_state[x][y].isStart:
                environment.colorize(x, y)
                old_node = passed[old_node]
                x, y = old_node

    def a_star(self, environment):
        self.percept(environment)
        open_list = []
        close_dic = {}
        x, y = self.get_position()
        g = 0
        goalx, goaly = environment.goal_pos
        node = x, y, x, y, g
        open_list.append(node)
        find = False
        while len(open_list) > 0:
            node = open_list[0]
            for item in open_list:
                node_f = node[4] + abs(node[0] - goalx) + abs(node[1] - goaly)
                item_f = item[4] + abs(item[0] - goalx) + abs(item[1] - goaly)
                if node_f > item_f:
                    node = item
            open_list.remove(node)
            node1 = node[0], node[1]
            if node1 in close_dic:
                continue
            x = node[0]
            y = node[1]
            parent_x = node[2]
            parent_y = node[3]
            g = node[4]
            parent_node = parent_x, parent_y
            child_node = x, y
            close_dic[child_node] = parent_node
            if self.current_state[x][y].isGoal:
                find = True
                break
            new_node = x, y - 1, x, y, g + 1
            new_node_dic = x, y - 1
            if (y - 1 >= 0) and (not self.current_state[x][y - 1].is_blocked()) and (not new_node_dic in close_dic.keys()):
                open_list.append(new_node)
            new_node = x + 1, y, x, y, g + 1
            new_node_dic = x + 1, y
            if (x + 1 < len(self.current_state)) and (not self.current_state[x + 1][y].is_blocked()) and (
                    not new_node_dic in close_dic.keys()):
                open_list.append(new_node)
            new_node = x, y + 1, x, y, g + 1
            new_node_dic = x, y + 1
            if (y + 1 < len(self.current_state[x])) and (not self.current_state[x][y + 1].is_blocked()) and (
                    not new_node_dic in close_dic.keys()):
                open_list.append(new_node)
            new_node = x - 1, y, x, y, g + 1
            new_node_dic = x - 1, y
            if (x - 1 >= 0) and (not self.current_state[x - 1][y].is_blocked()) and (not new_node_dic in close_dic.keys()):
                open_list.append(new_node)
            print(open_list)
        if find:
            node = node[0], node[1]
            old_node = close_dic[node]
            x, y = old_node
            while not self.current_state[x][y].isStart:
                environment.colorize(x, y)
                old_node = close_dic[old_node]
                x, y = old_node
