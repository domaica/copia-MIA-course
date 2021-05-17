# Python Homework - Py Me Up, Charlie IGNACIO DOMAICA

# PYBANK SOLUTION

### Stored solution

* As requested, created a new repository for this project called `python-challenge`.
  Inside it I created 2 new folders, `PyBank` and `PyPoll` to proceed with both homeworks respectively as it was required # Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Still not using GitHub. Hopefully I will progress in that regard. Yet not confident enough.

* Inside the folder `PyBank` , you can find following stuff:

  * A new file called `main_PyBank.py`. This is the main script to run for PyBank solution.
  * A `Resources-PyBank` folder has been created & contains the CSV files I used.
    Inside this folder you can also find a file named: `budget_test.csv`. It contains a subset of biggest data .csv for testing purposes
  * An `Analysis-PyBank` folder contains the text file that has the results from your analysis.
    It also contains a PowerPoint with some print screens with results of this analysis: `Solution PyBank results.pptx`


## PyBank

Regarding Python script main challenges or remarks have been:

  * I save versions every time I get a meaningful result. In this project I have reached up to 15 versions

  * My approach at the beginning was just using sequentially the code and solve each issue or request one by one. But when coding progresses,
    you find that one posterior solution affects your previous results. I am not familiar with breakpoints or debugging using Visual Studio so
    I had to guess reaction of loops, commands and variables by trial and error. I came to a stop, I was stuck.

  * So I learned in the hard way that using functions to split portions or subsets of code is a much better way to solve things. This is my lesson with this exercise

  * Good use of mathematics is another important outcome. When I began to calculate average of changes for every period,
    I began to calculate them with every difference between amounts one by one. In a smaller subset of data, playing with Excel, I realize that you can calculate this
    average by just calculate difference between initial value a final one divided by number of rows (skipping 1st own because there was no delta in first row).
    That simplified a lot the whole calculation.

  * Finally, I waste a considerable amount of time trying to find out why I was getting an empty or blank line between rows when I was writing and exporting a text file with
    the results. The solution was to apply a parameter 'newline' in cvswriter as follows:

    instead of using `with open(output_path, 'w') as csvfile:`
    right way:       `with open(output_path, 'w', newline='') as csvfile:`

    the solution was found out via google, of course.
