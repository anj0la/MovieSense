import matplotlib.pyplot as plt

def plot_accuracy(x_axis: list[int], val_accuracy: list[float], figure_path: str) -> None:
    """
    Plots a graph that visualizes how the accuracy changes over the epochs.

    Args:
        x_axis (list[int]): A list consisting of the epochs the model was trained on.
        val_accuracy (list[float]): A list containing all of the accuracies obtained for each epoch.
    """
    fig, ax = plt.subplots()
        
    # Plot validation accuracy
    ax.plot(x_axis, val_accuracy) 
        
    # Set labels and title
    ax.set_xlabel('Number of Epochs')
    ax.set_ylabel('Accuracy')
    ax.set_title(f'Accuracy as a Function of Epochs')

    # Save the plot
    plt.savefig(figure_path)

    # plt.show()
        
def plot_loss(x_axis: list[int], train_losses: list[float], val_losses: list[float], figure_path: str) -> None:
    """
    Plots a graph that visualizes how the loss decreases over the epochs for both the training and validation sets.

    Args:
        x_axis (list[int]): A list consisting of the epochs the model was trained on.
        train_losses (list[float]): A list containing the total training losses per epoch.
        val_losses (list[float]): A list containing the total validation losses per epoch.
    """
    fig, ax = plt.subplots()
        
    # Plot training losses
    ax.plot(x_axis, train_losses, label='Training Loss', color='blue')
        
    # Plot validation losses
    ax.plot(x_axis, val_losses, label='Validation Loss', color='orange', linestyle='--')

    # Set labels and title
    ax.set_xlabel('Number of Epochs')
    ax.set_ylabel('Total Loss')
    ax.set_title(f'Loss as a Function of Epochs')

    # Add legend to distinguish between train/validation
    ax.legend()

    # Save the plot
    plt.savefig(figure_path)
        
    # plt.show()