# Seat Map

**Seat map** module allows to configure and use ability to select seat on bus schema, or show stadium or concert halls maps for further selection of seats. This gives better visibility of available places and gives clients the ability to define their preferences (free or at surcharge). Alternatively - it is also possible to assign seats from manual correction and scheduler (if this module is active in the corresponding installation).

For each booking it is possible to assign seats. Currently this is available for:

- flights
- transfers
- activities (excursions & events).

In future - other products will be added.

Seats can be assigned in the following ways:

- in Manual Correction mode: checking *Seats Prebooked* checkbox and specifying a proper seat in a *Seat Number* field for a traveler (*Show seat number for Travel Agent / Client* checkbox can be selected so that TO1 can decide whether this information should be used only for internal assignment or visible for clients);

![2024-12-18_16-21-15.jpg](/assets/2024-12-18_16-21-15.jpg)

- in Offline Services: the same behaviour as for Manual Correction;
- in Scheduler: assigning a seat in Scheduler for every passenger via the column "Seat". Any number and text can be accepted as seat number, because different vehicles / venues have different numbering -- e.g. all these options are ok: \* 10, 11, 12 \* 2A, 2B \* Row 1, Seat 1

![2024-12-18_16-24-38.jpg](/assets/2024-12-18_16-24-38.jpg)

![2024-12-18_16-25-31.jpg](/assets/2024-12-18_16-25-31.jpg)

After a seat number is assigned - it is shown in reservation:

![2024-12-18_16-29-32.jpg](/assets/2024-12-18_16-29-32.jpg)

## Configure Vehicle Types

In order to be able to select seats on seat map - it's necessary to have Vehicle types that will be configured in advance and then seat maps will be linked with them - e.g. **Microbus 9 seats**, **Microbus 17 seats**, **Bus 36 seats etc.**

*Note: For other products such objects already exist:*

- *Hotels - there are descriptions, which can be further linked with floor plan*
- *Cruises - already have link with Ship, which may have Cabin plan*
- *Events - already have link with Venue, which can have Seat map*

To configure a vehicle type:

Navigate to General settings menu → Vehicle types → Click **Create**:

![2024-12-18_16-29-41.jpg](/assets/2024-12-18_16-29-41.jpg)

![2024-12-18_16-31-52.png](/assets/2024-12-18_16-31-52.png)

![2024-12-18_16-32-36.png](/assets/2024-12-18_16-32-36.png)

## Adding Vehicle Types to Scheduler

It is possible to select Vehicle type within schedule and automatically calculate how many seats in it are sold, and how many remain.

![2024-12-18_16-32-46.png](/assets/2024-12-18_16-32-46.png)

1.  When selecting "Vehicle type" in Scheduler for Transfers -- quantity of seats, quantity of occupied seats and quantity of free seats are automatically shown.
2.  When selecting "Vehicle type" in Scheduler for Excursions, type "off site" -- quantity of seats, quantity of occupied seats and quantity of free seats are automatically shown.

## Adding Seat Maps

It is possible to create Seat Maps for each installation to use for Transfers and Events in the current version (and other products - in future).

Each Seat Map can be assigned to certain object - either Vehicle Type or Venue.

*E.g. Seat Map of Vehicle, Seat Map of Venue (concert hall / stadium), Cabin Map of Ship, Room Map of Hotel.*

*Note: in the current version seat map will be simple matrix, in future versions - additional graphical implementation will be added. In current version there will be no UI for their creation, only upload directly to database.*

![2024-12-19_10-23-58.jpg](/assets/2024-12-19_10-23-58.jpg)

Additionally, it is possible to view seat map for Vehicle or Venue from Scheduler and see what seats are available and what are occupied:

![2024-12-19_10-28-34.jpg](/assets/2024-12-19_10-28-34.jpg)
