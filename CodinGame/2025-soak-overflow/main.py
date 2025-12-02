import sys


def debug(*args):
    print(*args, file=sys.stderr, flush=True)


class Controller:
    def __init__(self):
        self.id = int(input())

        self.player_agents: list[Agent] = []
        self.enemy_agents: list[Agent] = []
        self.dead_agents: list[Agent] = []
        self.agents: dict[int: Agent] = {}

        for agent in [Agent(self, *[int(j) for j in input().split()]) for _ in range(int(input()))]:
            if agent.is_player:
                self.player_agents.append(agent)
            else:
                self.enemy_agents.append(agent)
            self.agents[agent.id] = agent

        self.grid = Grid()

    def turn(self):
        self.handle_input()
        self.do_actions()

    def do_actions(self):
        self.add_shoot_actions()

        for agent in self.player_agents:
            agent.action()

    def handle_input(self):
        new_agents = {}
        for _ in range(int(input())):
            agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
            agent = self.agents[agent_id]
            agent.update_vals(x, y, cooldown, splash_bombs, wetness)
            new_agents[agent.id] = agent
        input()     # agent_count is redundant
        self.player_agents = []
        self.enemy_agents = []
        for agent_id, agent in self.agents.items():
            if agent_id not in new_agents:
                self.dead_agents.append(agent)
            elif agent.is_player:
                self.player_agents.append(agent)
            else:
                self.enemy_agents.append(agent)
        self.agents = new_agents

    def add_shoot_actions(self):
        for agent in self.player_agents:
            top_score = 0
            target = None
            for enemy in self.enemy_agents:
                if (score := agent.shoot_score(enemy)) > top_score:
                    top_score = score
                    target = enemy
            if target and top_score:
                agent.shoot(target)


class Agent:
    def __init__(self, controller, agent_id, player_id, shoot_cooldown, optimal_range, soaking_power, splash_bombs):
        self.controller: Controller = controller
        self.id = agent_id
        self.is_player = self.controller.id == player_id
        self.shoot_cooldown = shoot_cooldown
        self.optimal_range = optimal_range
        self.soaking_power = soaking_power
        self.splash_bombs = splash_bombs

        self.x, self.y = 0, 0
        self.cooldown = 0
        self.splash_bombs = 0
        self.wetness = 0
        self.actions = []

    def update_vals(self, x, y, cooldown, splash_bombs, wetness):
        self.x = x
        self.y = y
        self.cooldown = cooldown
        self.splash_bombs = splash_bombs
        self.wetness = wetness
        self.actions = []

    def move(self, x, y):
        return self.actions.append(["MOVE", x, y])

    def shoot(self, agent):
        self.actions.append(["SHOOT", agent.id])

    def action(self):
        actions = self.actions or [['HUNKER_DOWN'], ['MESSAGE', 'No actions']]
        actions = [[self.id]] + actions
        actions = [[str(_) for _ in action] for action in actions]

        actions_messages = [' '.join(action) for action in actions]
        message = ';'.join(actions_messages)
        print(message)

    def distance(self, agent):
        return abs(self.x - agent.x) + abs(self.y - agent.y)

    def shoot_score(self, agent):
        d = self.distance(agent)
        score = agent.wetness
        if d > 2*self.optimal_range:
            score = 0
        elif d > self.optimal_range:
            score /= 2

        return score


class Tile:
    def __init__(self, n):
        self.is_empty = n == 0
        self.low_cover = n == 1
        self.high_cover = n == 2
        self.cover = self.low_cover or self.high_cover


class Grid:
    def __init__(self):
        self.w, self.h = [int(i) for i in input().split()]
        self.grid = [[None for x in range(self.w)] for y in range(self.h)]
        for y in range(self.h):
            inputs = [int(i) for i in input().split()]
            for x in range(self.w):
                self.grid[inputs[3 * x + 1]][inputs[3 * x]] = Tile(inputs[3 * x + 2])

    def get(self, x, y) -> Tile:
        return self.grid[y][x]



controller = Controller()
while True:
    controller.turn()
