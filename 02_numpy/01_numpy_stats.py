import numpy as np

if __name__ == "__main__":
    arr = np.random.randn(20)
    print("Array:", arr)
    print("Mean:", arr.mean())
    print("Median:", np.median(arr))
    print("Std:", arr.std())
    reshaped = arr.reshape(4, 5)
    print("Reshape 4x5:\n", reshaped)
    print("Druga kolona:", reshaped[:, 1])
