from load_data import load_iris_data

def main():
    X, y, feature_names, target_names = load_iris_data()

    # count how many of each class, should be 50 each
    counts = [0, 0, 0]
    for label in y:
        counts[label] +=1

    print("=== CLASS COUNTS ===")
    for i in range(3):
        print(target_names[i], ":", counts[i])

if __name__ == "__main__":
    main()