import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D


def actualVsPredictedGraph(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    sns.regplot(x=y_test, y=y_pred)
    # plot a line, a perfit predict would all fall on this line
    plt.plot([0, 350], [0, 350], color='red', lw=2)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    custom_lines = [Line2D([0], [0], color='blue', lw=4),
                    Line2D([0], [0], color='red', lw=4)]
    plt.legend(custom_lines, ['Predicted', 'Perfect Prediction'])
    plt.title('Actual vs Predicted Values')
    plt.show()