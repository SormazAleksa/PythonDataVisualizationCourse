# Step 1: Create a Basic Line Plot

## Theory:
`matplotlib` is a powerful library for creating a wide variety of visualizations. In this step, we’ll start with a simple line plot using `plt.plot`.

## Task:
1. Import `matplotlib.pyplot` as `plt`.
2. Create a simple line plot using the following x and y data:
  ```python
    import matplotlib as plt
    import numpy as np

    x_value = np.random.random(50) * 100
    y_value = np.random.random(50) * 100

    plt.plot(x_value, y_value)
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()
```

