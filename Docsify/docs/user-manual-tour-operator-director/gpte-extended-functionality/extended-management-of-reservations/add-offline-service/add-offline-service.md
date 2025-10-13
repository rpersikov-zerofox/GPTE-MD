# Add offline service

With the Offline service module you can fill in details of any booking that was made by your staff in any system. Just fill in booking details, travellers, net and gross rates and the system will keep it in database easily accessible in future. With the offline bookings, you can:

- Create offline reservations;
- Fill in booking details and travelers;
- Specify prices and fees.

To add a service booked offline or in any other system to a reservation,

1.  On the reservation page, click **Add offline service**. *Add offline service* window appears:

![2024-11-18_13-30-34.jpg](/assets/2024-11-18_13-30-34.jpg)

![2024-11-18_13-31-21.jpg](/assets/2024-11-18_13-31-21.jpg)

2.  In the window, specify the following information:

- **General information**: specify the service *type* and enter its *name*, set its *status* (confirmed, confirmation pending, etc.), *ref number* and *supplier*, as well as *enter the service dates, quantity of pax, service details* and *description*.
- **Payment to supplier**: specify supplier's price, and set the cancellation fees. For more information, please see [Setting supplier and client price section](https://gp-team.atlassian.net/wiki/spaces/GPTEUG/pages/1922259452) below:

![2024-11-18_13-36-12.jpg](/assets/2024-11-18_13-36-12.jpg)

- **Payment from client**: specify client's price and set the cancellation price for the client. For more information, please see Setting supplier and client price section.
- **Traveler(s):** choose whether to specify all the travelers in the reservation or a primary traveler only, and select the primary traveler:

![2024-11-18_13-38-39.png](/assets/2024-11-18_13-38-39.png)

3.  Click **Save**.

## Flights parsing

When user adds a flight as an Offline Service it usually takes time to fill in all flight data, and it may also lead to mistakes. As an alternative way of entering this data parsing from text format was added - so you can copy the flight schedule and route from GDS and simply insert this into the system.

![2024-12-20_16-39-04.jpg](/assets/2024-12-20_16-39-04.jpg)

## Offline Services: Show real product type

Previously Offline Services were treated as a separate type of products, even though there were types "Hotel", "Flight", etc. Now the whole system was revised and they were added to general analytics of corresponding type (e.g. "Hotels") irrespective whether this hotel is booked via API connection, or from inventory, or added as offline service. Additionally you can filter by "Source of service" to see only bookings from Inventory, via API connections or added as Offline services.

![2024-12-20_16-54-58.jpg](/assets/2024-12-20_16-54-58.jpg)
