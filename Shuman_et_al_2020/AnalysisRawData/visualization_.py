#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:44:43 2019

@author: spiros
"""

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def make_dicts(dict_all, dict_input, case):

    if isinstance(dict_input[case], int):
        if case in dict_input.keys():
            dict_all[case].append(dict_input[case])
        else:
            dict_all[case] = [dict_input[case]]
    mean = np.mean(dict_input[case])
    std = np.std(dict_input[case])
    N = len(dict_input[case])
    if case in dict_all:
        dict_all[case].append([mean, std, N])
    else:
        dict_all[case] = [[mean, std, N]]

    return dict_all


def bar_plots(mydict, metric, path_figs, my_list):

    A, A_means, A_sems = mydict, [], []
    for case in my_list:
        A_means.append(np.mean(np.array(A[case])[:, 0]))
        A_sems.append(scipy.stats.sem(np.array(A[case])[:, 0]))

    y, labels = A_means, my_list
    N = len(y)
    x = range(N)

    fig_name = f"{path_figs}/{metric}_barplot.pdf"
    colors = ['blue', 'red', 'green', 'yellow', 'lightblue', 'olive',
              'darkmagenta','darkorange' ]
    # Create the figure
    plt.figure(1, dpi=300)
    plt.bar(x, y, color = colors[:len(my_list)], yerr=A_sems)
    plt.xticks(x, labels, rotation='45')
    plt.ylabel(metric, fontsize=16)
    plt.title(metric)
    plt.savefig(fig_name, format='pdf', dpi=300)
    plt.cla()
    plt.clf()
    plt.close()


def bar_plots2(mydict, metric, path_figs, my_list):

    A, A_means, A_sems = mydict, [], []
    for case in my_list:
        A_means.append(np.mean(A[case]))
        A_sems.append(scipy.stats.sem(A[case]))

    y, labels = A_means, my_list
    N = len(y)
    x = range(N)
    fig_name = f"{path_figs}/{metric}_barplot.pdf"

    colors = ['blue', 'red', 'green', 'yellow', 'lightblue', 'olive',
              'darkmagenta','darkorange' ]
    # Create the figure
    plt.figure(1, dpi=300)
    plt.bar(x, y, color = colors[:len(my_list)], yerr=A_sems)
    plt.xticks(x, labels, rotation='45')
    plt.ylabel(metric, fontsize=16)
    plt.title(metric)
    plt.savefig(fig_name, format='pdf', dpi=300)
    plt.cla()
    plt.clf()
    plt.close()

    # Make Boxplots
    A_list = []
    for case in my_list:
        A_list.append(list(mydict[case]))
    y, labels = A_means, my_list
    N = len(y)
    x = range(1, N+1)
    fig_name = f"{path_figs}/{metric}_boxplot.pdf"

    # notch shape box plot
    plt.figure(1, dpi=300)
    bplot = plt.boxplot(y, notch=True, vert=True,
                        patch_artist=True,
                        labels=labels)  # will be used to label x-ticks
    # fill with colors
    colors = ['blue', 'red', 'green', 'yellow', 'lightblue', 'olive',
              'darkmagenta','darkorange' ]
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    for element in ['fliers', 'means', 'medians', 'caps']:
        plt.setp(bplot[element], color='black')
    plt.xticks(x, labels, rotation='45')
    plt.ylabel(metric, fontsize=16)
    plt.savefig(fig_name, format='pdf', dpi=300)
    plt.cla()
    plt.clf()
    plt.close()
