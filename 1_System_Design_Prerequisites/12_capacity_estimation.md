# Capacity Estimation

# Why is this important?
Back-of-the-envelope calculations are often expected in system design questions. 
They help logically state the parameters influencing a result, 
and estimating the capacity requires multiple estimations on the way. 
Also lets us individually state our assumptions.

# Examples
Eg 1: Estimate the hardware requirements to set up a system like YouTube.

1. Let's start with storage requirements:

First, always try to estimate the number of user.
About 1 billion active users.
I assume 1/1000 produces a video a day.
Which means 1 million new videos a day.

Next, for youtube, it makes sense to try and estimate size of a video.
What's the size of each video?
Assume the average length of a video to be 10 minutes.
Assume a 10 minute video to be of size 1 GB.

If asked for details about the assumption,
A video is a bunch of images. 10 minutes is 600 seconds.
Each second has 24 frames.
So a video has 25*600 = 150,000 frames.
Each frame is of size  50KB. Which means (1.5 10^5) (50^3) bytes = 0.75 GB.

Next, try and estimate storage per video.
As each video is of about 1GB, we assume the storage requirement per day is 1GB * 1 million = 1 PB.
This is the bare minimum storage requirement to store the original videos. 
If we want to have redundancy for fault tolerance and performance, we have to store copies. 
Lets choose 3 copies.
That's 3 petabytes of raw data storage.

Next, for resolutions,
Let's assume a single type of encoding, mp4, and the formats will take a 720p video and store it in 480, 360, 240 and 144p respectively. 
That means approximately half the video size per codec.
If X is the original storage requirement = 1 PB,
We have X + X/2 + X/4 + X/8 == 2*X.
With redundancy, that's 2X 3 = 6X.
That's 6 PB(processed) + 3PB (raw) == 10 PB of data. 

Next, lets try and estimate the cache requirements.
First, we need to decide, what will be in the cache.
Here, we consider, the thumbnail image, title, and description text.
We need to do this for the most watched/trending videos of all time, 
and the most frequent/popular/trending videos of the day.
For one video detail in the cache, if the thumbnail is 1MB,
lets say that the cache stores a downscaled version that is 100KB. (10x smaller)
So, the cache requirement is 10KB * 100 * 250K (storage per vid * 100 days * 250k most popular videos from those days).
That is 25 * 10^10 = 250 GB.
But since this is a cache, this is a 250 GB of RAM, and is more expensive.
Lets say we use 16GB computers, so we need 250/16 = 16 nodes
Plus, we would want to have redundancy again, so 16*3 = 50 nodes.
Plus, you don't want all nodes to be at 100% capacity, so lets work them at 50% capacity, so 50*2 = 100 nodes.


Next, for storage cost.
The cost of this system (10 PB) is about 1 million per day.
For a 3 year plan, we can expect a 1 billion dollar storage price.


Now let's look at the real numbers:
Video upload speed = 3 * 10^4 minutes per minute.
That's 3 * 10^4 * 1440 video footage per day = 4.5 * 10^7 minutes.
Video encoding can reduce a 1-hour film to 1 GB. 
So 1 million GB is the requirement. 
That's 1 PB.
So the original cost is similar to what the real numbers say.

If we are off by order of magnitude, it's good. 
However, being off by 3 or more orders of magnitude is too much. 
We can then highlight the following:
Where our assumption was wrong, or
Which factor we didn't take into account.

Eg: Estimate the number of petrol pumps in the city of Mumbai.










