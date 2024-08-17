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
        self.set_position(self.get_position() + direction)

        pass

    @staticmethod
    def get_actions():
        actions = []
        # returns a list of valid actions
        return actions

    def bfs(self, environment):
        self.percept(environment)
        visited = []
        root = []
        open = []
        cell = self.position
        visited.append(cell)
        root.append(cell)
        open.append(cell)
        while open.__len__() > 0:
            cell = open.pop(0)
            childs = self.getChilds(cell)
            for child in childs:
                if self.isGoal(child):
                    visited.append(child)
                    root.append(cell)
                    self.print(environment, visited, root)
                    return
                else:
                    if not child in visited:
                        open.append(child)
                        visited.append(child)
                        root.append(cell)
            print(open)
        pass

    def dfs(self, environment):
        self.percept(environment)
        self.visited = []
        self.visited.append(self.get_position())
        self.recurciveDFS(environment, self.get_position())

    def a_star(self, environment):
        open = []
        g = []
        openRoot = []
        visited = []
        visitedRoot = []
        open.append(self.get_position())
        g.append(0)
        openRoot.append(self.get_position())
        while open.__len__() > 0:
            index = self.bestIndex(environment, open, g)
            cell = open.pop(index)
            coast = g.pop(index)
            root = openRoot.pop(index)
            visited.append(cell)
            visitedRoot.append(root)
            if self.isGoal(cell):
                self.print(environment, visited, visitedRoot)
                return
            childs = self.getChilds(cell)
            for child in childs:
                if not child in visited:
                    open.append(child)
                    g.append(coast+1)
                    openRoot.append(cell)

    def isGoal(self, cell):
        x, y = cell
        return self.current_state[x][y].isGoal

    def getChilds(self, cell): # left > right > up > down
        childs = []
        x, y = cell
        cell = x - 1, y
        childs.append(cell) if self.isValid(cell) else None
        cell = x + 1, y
        childs.append(cell) if self.isValid(cell) else None
        cell = x, y - 1
        childs.append(cell) if self.isValid(cell) else None
        cell = x, y + 1
        childs.append(cell) if self.isValid(cell) else None

        return childs

    def isValid(self, cell):
        x, y = cell
        board = self.current_state
        xUpperBound = len(board)
        yUpperBound = len(board[0])
        if x < 0 or x >= xUpperBound:
            return False
        if y < 0 or y >= yUpperBound:
            return False
        return not board[x][y].is_blocked()

    def recurciveDFS(self, environment, cell):
        board = self.current_state
        childs = self.getChilds(cell)
        for child in childs:
            if self.isGoal(child):
                environment.colorize(cell[0], cell[1])
                return 1
            else:
                if not child in self.visited:
                    self.visited.append(child)
                    if self.recurciveDFS(environment, child) == 1:
                        environment.colorize(child[0], child[1])
                        return 1
                    else:
                        self.visited.append(cell)
        return 0

    def print(self, environment, visited, root):
        cell = root[root.__len__() - 1]
        while not self.current_state[cell[0]][cell[1]].isStart:
            environment.colorize(cell[0], cell[1])
            cell = root[visited.index(cell)]

    def f(self, environment, cell, g):
        x, y = cell
        goalx, goaly = environment.goal_pos
        return abs(x - goalx) + abs(y - goaly) + g

    def bestIndex(self, environment, open, g):
        index = 0
        for i in range(open.__len__()):
            if self.f(environment, open[index], g[index]) > self.f(environment, open[i], g[i]):
                index = i
        return index