# Festival_Schedule_Generator

## The goal
This project was created to solve one of the challenges created by Demcon, which can be found here:
https://careersatdemcon.com/decode-demcon

But this particular challenge was:

Demcon has decided to expand its activities, and to organize a musical festival. After being an expert in mechatronic systems engineering, the move to the entertainment business seems a rather logical choice.

For the festival 30 acts are hired, such as the Demcon band and other popular acts. Unfortunately, each band has a very tight schedule, and is only able to play at a fixed timeslot. This makes the planning difficult, and the festival organizer needs to know how many stages to prepare for the event.

Your job is to help the festival organization. You are given a list of shows, each with a start and end time. The start and end times are provided as an offset from the start of the festival since the festival goes on non-stop. For example, the first three shows are given like this:

```
show_1 36 39
show_2 30 33
show_3 29 36
```

show_1 is scheduled from 36 hours after festival start and will play for 4 long hours up to (and including) hour 39 after festival start.

It can be seen that show_1 and show_3 overlap, since they both play at hour 36. Also show_2 and show_3 overlap, so they cannot share a stage.

Your task is to create a planning program which takes the list of shows, and their start and end times, and creates a planning.

Good luck!

## How to use

This script can easily be run by running the following command:

``` bash
py .\PATH\TO\festival_schedular.py --input .\PATH\TO\shows.csv
```

The shows.csv file contains all shows with their given start and end time.
Each row contains:

| Column Name | Description | Data Type |
|-------------|-------------|-----------|
|show | Name of the show | String |
|start | Start time | Integer |
|end | End time | Integer |

The format of this file is as follows: show,start,end. 

As a result this file will look like this:
```
show,start,end
show_1,29,33
show_2,2,9
show_3,44,47
show_4,26,30
```