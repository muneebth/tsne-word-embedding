import os
import sys
import csv
import numpy as np
from tsne import tsne
import matplotlib.pyplot as plt
import json

def tsne_viz(
        mat=None,
        rownames=None,
        indices=None,
        colors=None,
        output_filename=None,
        figheight=40,
        figwidth=50,
        display_progress=False): 
    if not colors:
        colors = ['black' for i in range(len(mat))]
    temp = sys.stdout
    if not display_progress:
        # Redirect stdout so that tsne doesn't fill the screen with its iteration info:
        f = open(os.devnull, 'w')
        sys.stdout = f
    tsnemat = tsne(mat)   
    sys.stdout = temp
   # print tsnemat
    # Plot coordinates:
    if not indices:
        indices = range(len(mat))        
    vocab = np.array(rownames)[indices]
    xvals = tsnemat[indices, 0] 
    yvals = tsnemat[indices, 1]
    # Plotting:
    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.set_figheight(100)
    fig.set_figwidth(500)
    ax.plot(xvals, yvals, marker='', linestyle='')
    # Text labels:
    for word, x, y, color in zip(vocab, xvals, yvals, colors):
        ax.annotate(word, (x, y), fontsize=8, color=color)
    print "Output:"
    if output_filename:
        plt.savefig(output_filename, bbox_inches='tight')
    else:
        plt.show()

  
if __name__ == "__main__":
	fp=open('word2vecproj.json','r')
	word_list=json.load(fp) 
	tsne_viz(mat=np.array(word_list[0]),rownames=word_list[1])	
	fp.close()
	       
	    
	    
