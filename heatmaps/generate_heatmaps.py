import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn.functional as F
import argparse

def plot_layer_contribution_heatmap(checkpoint_path):
    # Load the model state dictionary
    state_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))

    weights = []
    
    # extract and process weights for each layer
    for i in range(12): 
        alpha_weights_key = 'transformer.layers.' + str(i) + '.prev_layer_weights'
        
        if alpha_weights_key in state_dict:
            alpha_weights = state_dict[alpha_weights_key]
            softmax_alpha_weights = F.softmax(alpha_weights, dim=-1)
            weights.append(softmax_alpha_weights.tolist())
        else:
            print(f"Key {alpha_weights_key} not found in state_dict")

    normalised_weight = []
    
    # loop through the weights and noramlise thenm
    for i, layer_weights in enumerate(weights):
        norm_weight_layer = []
        for num in layer_weights:
            num2 = num * (i + 1)
            norm_weight_layer.append(num2)
        normalised_weight.append(norm_weight_layer)

    max_length = 12

    #padding to the weights
    padded_weights = []
    for weight_list in normalised_weight:
        padding = [0] * (max_length - len(weight_list))
        padded_sublist = weight_list + padding
        padded_weights.append(padded_sublist)

    weights_array = np.array(padded_weights)

    # for visualisation-  to set upper portion of the heatmap to blank space essentially
    mask = np.triu(np.ones_like(weights_array, dtype=bool), k=1)

    # create the heatmap plot
    plt.figure(figsize=(10, 8))
    sns.heatmap(weights_array, mask=mask, cmap='coolwarm', square=True, annot=True, 
                cbar_kws={"shrink": .8}, linewidths=0, 
                xticklabels=np.arange(0, 12), yticklabels=np.arange(1, 13))

    plt.xlabel('Layer Outputs', fontsize=14, color='black')
    plt.ylabel('Layer Inputs', fontsize=14, color='black')
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')

    #save img as a png file
    output_file = checkpoint_path.split('/')[-1].replace('.bin', '.png')
    plt.savefig(output_file, dpi=500, bbox_inches='tight', transparent=False)


    plt.show()
    print(f"Heatmap saved as {output_file}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Generate layer contribution heatmap from a model checkpoint.")
    parser.add_argument('--input_path', type=str, required=True, help="Path to the model checkpoint (e.g., 'eim/200.bin')")
    
    
    args = parser.parse_args()
    
    
    plot_layer_contribution_heatmap(args.input_path)
