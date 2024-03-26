import random

class StrategicPlanning:

    def __init__(self, objective_count, uncommitted_proportion=0.1):
        self.n = objective_count
        self.p = uncommitted_proportion

    def generate_objectives(self, team, model, capacity):
        objectives, max_score, uncommitted = [], 0, 0

        features = model.get_pi_features()

        for _ in range(self.n):
            objective = {
                'feature': random.choice(features),
                'score': 0,
                'committed': False
            }

            # Assign score based on alignment to team
            alignment_score = random.random()
            objective['score'] = alignment_score

            if random.random() < self.p:
                uncommitted += 1
                objective['committed'] = False
                objective['score'] = 0
            else:
                objectives.append(objective)

        objectives_count = len(objectives)

        # Normalize scores
        total_score = sum(o['score'] for o in objectives)

        for objective in objectives:
            objective['weight'] = objective['score'] / total_score

        # Assign capacities
        for i, objective in enumerate(objectives):
            objective['capacity'] = int((1 - self.p) * capacity * (objective['score'] / total_score))

        remaining_capacity = capacity

        for objective in objectives:
            capacity_left = remaining_capacity - objective['capacity']
            remaining_capacity -= objective['capacity']

            if capacity_left > 0 and uncommitted > 0:
                uncommitted -= 1
                random_obj = {
                    'feature': random.choice(features),
                    'score': 0,
                    'committed': False
                }

                remaining_capacity = capacity_left

                objectives.append(random_obj)

        return objectives


if __name__ == "__main__":
    # Setup
    strategic_planning = StrategicPlanning(50, 0.1)

    # Assume pi_model is a class that represents the AI model you use
    pi_model = PiModel()

    # As a placeholder, let's assume
    pi_model.get_pi_features = lambda: list(range(1, 101))

    team_capacity = 20

    team = "AI-Team-A"

    objectives = strategic_planning.generate_objectives(team, pi_model, team_capacity)

    print(f"Objectives generated for {team} with {team_capacity} capacity:")

    for objective in objectives:
        status = "Committed (score: {:.1%})" if objective['committed'] else "Uncommitted (score: {:.1%})"
        print(f"- Objective: Feature ID {objective['feature']},  {status} , Weight: {objective['weight']:.1%}, Capacity: {objective['capacity']}")
