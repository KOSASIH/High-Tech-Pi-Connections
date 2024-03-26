import random
import time

class Particle:
    def __init__(self, index, dimension):
        self.position = [random.uniform(0, 100) for _ in range(dimension)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimension)]
        self.best_position = self.position.copy()
        self.best_fitness = self.calculate_fitness(self.position)

    def update_velocity(self, pbest_position, gbest_position, w, c1, c2):
        for i in range(len(self.velocity)):
            r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
            self.velocity[i] = (w * self.velocity[i] +
                                c1 * r1 * (pbest_position[i] - self.position[i]) +
                                c2 * r2 * (gbest_position[i] - self.position[i]))

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

            # Applying position boundaries
            if self.position[i] < bounds[0]:
                self.position[i] = bounds[0]
            elif self.position[i] > bounds[1]:
                self.position[i] = bounds[1]

    def calculate_fitness(self, position):
        # A placeholder for fitness function
        result = sum(position)
        return result

class Swarm:
    def __init__(self, dimensions, particles_count, iterations, bounds, w, c1, c2):
        self.dimensions = dimensions
        self.particles_count = particles_count
        self.iterations = iterations
        self.bounds = bounds
        self.w, self.c1, self.c2 = w, c1, c2
        
        self.particles = [Particle(i, dimensions) for i in range(particles_count)]

    def best_particle(self):
        return max(self.particles, key=lambda p: p.best_fitness)

    def update_global_best(self):
        for particle in self.particles:
            gbest = self.best_particle()
            particle.best_fitness = max(particle.best_fitness, particle.calculate_fitness(particle.position))

    def step(self):
        for particle in self.particles:
            pbest_position, gbest = particle.best_position, self.best_particle().position
            particle.update_velocity(pbest_position, gbest, self.w, self.c1, self.c2)
            particle.update_position(self.bounds)

    def run(self):
        self.update_global_best()

        for iteration in range(self.iterations):
            print(f'Iteration: {iteration + 1}')
            for particle in self.particles:
                particle.update_position(self.bounds)

            self.update_global_best()

        print('Optimal solution found:')
        print(self.best_particle().best_position, self.best_particle().best_fitness)

if __name__ == '__main__':
    dimensions, particles_count, iterations, bounds = 10, 5, 100, [0, 100] * dimensions
    w, c1, c2 = 0.8, 1.2, 1.2

    Swarm(dimensions, particles_count, iterations, bounds, w, c1, c2).run()
