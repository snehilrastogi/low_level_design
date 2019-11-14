This is Swiggy Assignment -

Execution - python run.py

The num_parking_slots and commands list given in run.py are used as a sample and can be changed to see the changes in the output

All the print statements are just to provide an insight into the code and to tell the state of objects as they travel through the code.

All the models are under the models directory, services are defined under services directory and constants file hold the constants.

Working --

- run.py calls SmartParkingSystem() which initializes and sets up the object of Parking with slots objects defined as num_of_slots.
- The commands are taken with Action defined as <leave, park, status allocated, status free> which are executed through the ParkingSystemService.
- The run.py and smart_parking_system.py files are created just to simulate the testing environment and showcase the execution of the code.
Process continues until all the commands are executed.