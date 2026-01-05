import matplotlib.pyplot as plt

def plot_petal_length_vs_width(X, y, save_path):
    # Column indices in X:
    # 2 = petal length, 3 = petal width
    x = X[:, 2] # [:, ] means all rows
    w = X[:, 3]

    # plt.scatter(x, w, c=y) #y is a parameter bound to c which is colour

    plt.scatter(x[y == 0], w[y == 0], label="setosa")
    plt.scatter(x[y == 1], w[y == 1], label="versicolor")
    plt.scatter(x[y == 2], w[y == 2], label="virginica")
    plt.legend()
    
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Petal width (cm)")
    plt.title("Iris: Petal length vs Petal width (colored by species)")

    plt.savefig(save_path)
    plt.close()
