from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse

def visualize_days():
    """ Visualize days of the week """

    # grab our parsed data that we parsed earlier
    data_file = parse.parse(parse.MY_FILE, ',')

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week

    counter = Counter(item["DayOfWeek"] for item in data_file)
    
    # separate the x-axis data (days of the week) from
    # 'counter' variable from the y-axis data (number of incidents for each day)

    data_list = [counter["Monday"], counter["Tuesday"], counter["Wednesday"],
                 counter["Thursday"], counter["Friday"], counter["Saturday"], counter["Sunday"]]

    day_tuple = tuple(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    
    # with that y-axis data, assign it to a matplotlib plot distance

    plt.plot(data_list)

    # create the amount of ticks needed for our x-axis, and assign the labels

    plt.xticks(range(len(day_tuple)), day_tuple)
                 
    # save the plot!

    plt.savefig("Days.png")
    
    # close plot file

    plt.clf()

def visualize_type():
    """ Visualize data by category in a bar graph """

    #grab our parsed data

    data_file = parse.parse(parse.MY_FILE, ",")

    #make a new variable counter

    counter = Counter([item["Category"] for item in data_file])

    #set labels based on key of counter

    labels = tuple(counter.keys())

    #Set where the labels hit the x-axis

    xlocations = np.arange(len(labels)) + 0.5

    #Set width
    width=0.5

    #Assign data to bar plot
    plt.bar(xlocations, counter.values(), width=width)

    #Assign labels and tick location to x-axis
    plt.xticks(xlocations + width /2, labels, rotation=90)

    
    #Give more room to that labels aren't cut off
    plt.subplots_adjust(bottom=0.5)

    #Make overall figure larger
    plt.rcParams['figure.figsize'] = 12,8

    #Save the plot
    plt.savefig("Type.png")
    
    #Close the plot
    #plt.close()
    
def main():
    visualize_type()

if __name__ == "__main__":
    main()

