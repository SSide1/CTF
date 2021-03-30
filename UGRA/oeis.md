
![main](https://user-images.githubusercontent.com/76822573/113013408-5b652d00-9184-11eb-8953-33ebaa3f9295.png)

The idea of the assignment is simple and straightforward. We need to choose such a Pin so that no more than 5
reasons are displayed why this number is "simple"

The first step is to understand how these errors appear, to find a database of such errors, since they are
repeated very rarely and are well structured.

Having searched the site better, you can easily notice how errors are formed.

![id_error](https://user-images.githubusercontent.com/76822573/113013878-c4e53b80-9184-11eb-9f89-84694a67d8dc.png)

These ids are mapped to values from oeis.org
There is a base with these id, which are indexed as A0{id}
Then the task is simple, we need to write a parser that will go through all 4-digit numbers and look for the
number where the errors are less than 10. To do this, we will use the Displaying 1-10 line, since we need less
than 10, then the output will be different.

![python_worked](https://user-images.githubusercontent.com/76822573/113014470-46d56480-9185-11eb-8066-374aef027a4d.png)

It’s not hard to guess that by the end there will most likely be a better chance of finding the number we need.
Therefore, it is worth starting the search from the end

As expected, the number was found quickly enough and this number is 9935
Enter this number on the site and get the correct answer

![flag](https://user-images.githubusercontent.com/76822573/113014760-8a2fd300-9185-11eb-9598-b10ca677d3cb.png)

(*Python3 code is attached*)

The answer is: ugra_what_a_beautiful_number_256e84ee7404
