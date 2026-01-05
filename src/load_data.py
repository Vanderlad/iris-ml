from sklearn.datasets import load_iris

def load_iris_data():
    iris = load_iris()
    X = iris.data      #2D array: 150 rows, 4 columns (X -> input data/features)
    y = iris.target    #1D array: 150 labels (0, 1, 2) (y-> output/labels) e.g. setosa y[0], versicolor y[1, virginica y[2]
    feature_names = iris.feature_names
    target_names = iris.target_names
    return X, y, feature_names, target_names


if __name__ == "__main__":
    X, y, feature_names, target_names = load_iris_data() #tuple unpacking

    print("=== IRIS DATASET ===")
    print("Samples (rows):", len(X))
    print("Features (columns):", len(X[0]))
    print("Feature names:", feature_names)
    print("Target names:", target_names)

    print("\nFirst row (first flower):", X[0])
    print("First label (as number):", y[0])
    print("First label (as name):", target_names[y[0]])