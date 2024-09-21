import numpy as np

class DownhillSimplexAlgorithm():
    def __init__(self, 
                 func, 
                 dim: int, 
                 initial_simplex: np.array = None,
                 alpha: float = 1.0, 
                 gamma: float = 1.5, 
                 rho: float = 0.5, 
                 sigma:float = 0.5, 
                 tol:float = 1e-6, 
                 max_iter:int = 1000):
        self.func = func
        self.dim = dim
        self.alpha = alpha
        self.gamma = gamma
        self.rho = rho
        self.sigma = sigma
        self.tol = tol
        self.max_iter = max_iter

        if initial_simplex is not None:
            self.simplex = initial_simplex
        else:
            self.simplex = np.random.randn(dim + 1, dim)

    def _sort_simplex(self):
        self.simplex = self.simplex[np.argsort([self.func(x) for x in self.simplex])]

    def _centroid(self):
        return np.mean(self.simplex[:-1], axis=0)

    def reflect(self, x_o, x_w):
        return x_o + self.alpha * (x_o - x_w)

    def expand(self, x_o, x_r):
        return x_o + self.gamma * (x_r - x_o)

    def contract(self, x_o, x_r, outside=True):
        if outside:
            return x_o + self.rho * (x_r - x_o)
        else:
            return x_o + self.rho * (self.simplex[-1] - x_o)

    def shrink(self):
        x_best = self.simplex[0]
        self.simplex = x_best + self.sigma * (self.simplex - x_best)

    def optimize(self):
        for _ in range(self.max_iter):
            self._sort_simplex()
            
            f_min = self.func(self.simplex[0])
            f_max = self.func(self.simplex[-1])
            if f_max - f_min < self.tol:
                break

            # Calculate centroid of all points except the worst point
            x_o = self._centroid()

            # Reflection
            x_r = self.reflect(x_o, self.simplex[-1])
            f_r = self.func(x_r)
            if f_min <= f_r < self.func(self.simplex[-2]):
                self.simplex[-1] = x_r
            
            # Expansion
            elif f_r < f_min:
                x_e = self.expand(x_o, x_r)
                if self.func(x_e) < self.func(x_r):
                    self.simplex[-1] = x_e
                else:
                    self.simplex[-1] = x_r

            # Contraction:
            else:
                if f_r < f_max:
                    # Outside contraction
                    x_c = self.contract(x_o, x_r, outside=True)
                else:
                    # Inside contraction
                    x_c = self.contract(x_o, self.simplex[-1], outside=False)
            
                if self.func(x_c) < min(f_r, f_max):
                    self.simplex[-1] = x_c
                else:
                    # Shrink
                    self.shrink()

        self._sort_simplex()
        return self.simplex[0], self.func(self.simplex[0])
    
def Rosenbrock_function(point, a=1, b=100):
    x, y = point
    return (a - x) ** 2 + b * (y - x ** 2) ** 2
    
if __name__ == "__main__":
    dsa = DownhillSimplexAlgorithm(Rosenbrock_function, dim=2)
    best_point, best_val = dsa.optimize()
    print(best_point, best_val)