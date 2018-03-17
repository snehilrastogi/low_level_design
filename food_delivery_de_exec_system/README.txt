This is swiggy Assignment -

Execution - python run.py

The orders list and delivery executives list given in run.py are used as a sample and can be changed to see the changes in the output

All the print statements are just to provide an insight into the code and to tell the state of objects as they travel through the code.

All the models are under the models directory and utils contain the datetime and haversine distance utilities.

Working --

- run.py calls AutoAssignmentSystem() which initializes and sets up the objects of order, customer and delivery executives and one by
one calls each strategy.
- The strategy are chosen by the strategy factory which returns the object for the chosen strategy.
- Now the startegy is called and OrdersService and DeliveryExecutivesService are called and Order and DeliveryExecutive
objects are mapped and returned.
Process continues until either all the delivery executives are in BUSY state or all PENDING orders are finished.

I have implemented two strategies - low first mile and premium customer

All the assumptions are mentioned under assumptions.txt and all the extensions are explained under extensions.txt