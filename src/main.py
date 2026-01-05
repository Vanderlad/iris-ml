from load_data import load_iris_data
from visualize import plot_petal_length_vs_width, plot_sepal_length_vs_width 

def classify_flower(petal_length):
    if petal_length < 2.5:
        return 0 #setosa
    else:
        return 1 #not setosa (temp)

def main():
    X, y, feature_names, target_names = load_iris_data()


#Basic Classification Rules Test

    correct = 0
    total = len(y)

    for i in range(total):
        petal_length = X[i][2] #column 2
        prediction = classify_flower(petal_length)

        actual = y[i]

        if actual == 0 and prediction ==0:
            correct += 1
        elif actual != 0 and prediction != 0:
            correct += 1

    print("# of correct classifications:", correct)
    print("Total samples:", total)
    print("Accuracy:", correct / total)


    # Plot petal length vs width
    save_path = "results/figures/petal_length_vs_width.png"
    plot_petal_length_vs_width(X, y, save_path)
    print("Saved petal plot to:", save_path)


    # Plot sepal length vs width
    save_path = "results/figures/sepal_length_vs_width.png"
    plot_sepal_length_vs_width(X, y, save_path)
    print("Saved sepal plot to:", save_path)

if __name__ == "__main__":
    main()