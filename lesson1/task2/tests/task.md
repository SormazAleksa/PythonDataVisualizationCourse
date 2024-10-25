## Task 2: Customize the plot

## Theory:
Customizing plots is important for improving readability and aesthetics
We can modify line color, markers, and other properties using additional
parameters.

## Task:
1. Reuse the plot from Task1, but this time:
  - Change the line color to red (`'r'`).
  - Add circle markers at each data point (`'o'`)
  - Enable a grid plot

2. Display the modified plot

### Example

```python
plt.plot(x_value, y_value, 'ro-') # red line with circle markers
plt.grid(True)
plt.show()
```

Let's begin.
