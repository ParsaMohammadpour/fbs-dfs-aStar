# find path using BFS, DFS and A*<br>
&emsp; In this assignment, we had a maze, which had some blocks that we can't enter. And we are in a specified location. We have to find the path to the goal location by different algorithms.
we used bfs, dfs and A* algorithms for this purpos and we can use them and visually see their answer.<br/>
<br/>
## how to use different algorithms:<br/>
&emsp; In the main.py file, we can simple replace this line `agent.a_star(gameBoard)` with any of the following lines to see each algorithms results.<br>
#### - current file:<br/>
&emsp; shows the result of **A*** algorithm.
#### - replacing by  `agent.bfs(gameBoard)`:<br/>
&emsp; shows the result for **BFS** algorithm.
#### - replacing by `agent.dfs(gameBoard)`:<br/>
&emsp; shows the result for dfs algorithm
<br/>
<br/>
<br/>
## Agent-v2:<br/>
&emsp; I also implemented it in another version (same functionality with different approaches) and put it here in the Agent-v2.py file. For example it has recursive implementation for dfs algorithm. 
For running this project, you only need one of these (Agent.py and Agent-v2.py) files. It doesn't matter which of them you are using, the **how to use different algorithms** section, remains the same.
