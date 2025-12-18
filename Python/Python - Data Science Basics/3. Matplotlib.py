import numpy as np

import matplotlib.pyplot as plt

def binary_search_visualization(arr, target):
    """
    Visualizes the binary search process on a sorted array.
    """
    low, high = 0, len(arr) - 1
    steps = []
    
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high))
        
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # Plot each step
    fig, axes = plt.subplots(len(steps), 1, figsize=(8, 4 * len(steps)))
    if len(steps) == 1:
        axes = [axes]
    
    for i, (low, mid, high) in enumerate(steps):
        ax = axes[i]
        colors = ['blue'] * len(arr)
        for j in range(low, high + 1):
            colors[j] = 'orange'  # Search range
        colors[mid] = 'red'  # Mid point
        
        ax.bar(range(len(arr)), arr, color=colors)
        ax.set_title(f'Step {i+1}: Low={low}, Mid={mid}, High={high}, Target={target}')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
    
    plt.tight_layout()
    plt.show()

# Example usage
arr = sorted([1, 3, 5, 7, 9, 11, 13, 15])
target = 3
binary_search_visualization(arr, target)