There is only one elevator whose starting position is configurable

This elevator system takes some inputs and generates the request data like
[
{
customer:"id, curremt floor"
destination: "dest floor"
},
{
}

]

Now to simulate we take on request one by one and move the elevator to customer and then go to destination and
then updates both curremt postion and then takes on next req. doesnot consider intern=mediate floor req while moving to serve one rquest.

Basically each req is served individually.

Can be extended..use m elevators, make use of building to apply different strategies (what i applied could be one basic strategy)
other could be serving request while we are at it. like if while serving req 1 we see that we have reached a floor where
the other req can be served, do serve that.


Kindly suggest changes and updates and modifications and use cases.


