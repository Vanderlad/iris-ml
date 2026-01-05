from load_data import load_iris_data
from visualize import plot_petal_length_vs_width, plot_sepal_length_vs_width 

def main():
    X, y, feature_names, target_names = load_iris_data()

    # count how many of each class, should be 50 each
    counts = [0, 0, 0]
    for label in y:
        counts[label] +=1

    print("=== CLASS COUNTS ===")
    for i in range(3):
        print(target_names[i], ":", counts[i])

    save_path = "results/figures/petal_length_vs_width.png"
    plot_petal_length_vs_width(X, y, save_path)
    print("Saved petal plot to:", save_path)

    save_path = "results/figures/sepal_length_vs_width.png"
    plot_sepal_length_vs_width(X, y, save_path)
    print("Saved sepal plot to:", save_path)

if __name__ == "__main__":
    main()