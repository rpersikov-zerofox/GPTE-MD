# Calculation

**This functionality is currently available via administration panel.**

In the Calculation subsection you can specify the mark up and commission calculation. The type of calculation depends on the type of the partner and the approved way of pricing:

- **Markup:** a standard form of configuring prices for end-consumers (Private Clients and Corporate Clients) and for multi-level distribution via other Tour Operators (see more in ). When you configure markup -- it will be added to the Net Rate from supplier to form the sales price. *For example, a double room offered by supplier costs you EUR 100. With a 20% markup you can sell it to your client for EUR 120. So your profit will be EUR 20.*

![image-20201005-161217.png](/assets/image-20201005-161217.png)

- **Markup & Commission:** a standard form of configuring prices for travel agencies. When you configure both markup and commission system will apply the markup in order to calculate the sales price and will additionally show the commission that Agency will get for this sale. The commission is being calculated from the total sales price. *For example, a double room offered by supplier costs EUR 100. With a 20% markup and 10% commission agency will see that the price for traveler is EUR 120 and the commission is 10% from the sales price. The profit of your company is "markup minus commission" = EUR 20 -- EUR 12 = EUR 8.*

![image-20201005-161237.png](/assets/image-20201005-161237.png)

There are several ways to calculate a sale price in percentage and fixed amount:

1.  The calculation of a sale price in percent is always based on the full cost of the service. For example the net price is EUR 100 and the markup is 20%, the total price is then calculated by the following formula: Total price = net price + markup = EUR 120.
2.  The fixed commission is calculated based on the service rate and depends on the service. Fixed commission for accommodation services is added to the price of each night, for transfer services - to the price of the whole transfer service, etc. For example the room is booked for 5 nights with the net rate of EUR 100 per night and a markup of EUR 20. The total price is then calculated by the following formula: Total price = net price \* number of nights + markup \* number of nights = 100\*5 + 20\*5 = EUR 600. Please also pay attention that for direct sales contract setting, setting commission is unavailable.

**Configuring markup**

To set the rules for price calculation,

1.  Go to the contract, tab Calculation.
2.  Click **Edit** to switch to editing mode.

![image-20201005-162043.png](/assets/image-20201005-162043.png)

3.  From the **Currency** drop-down, select the currency of contract. It's necessary if you're going to configure markup or commission in fixed amount (not %) or if you need to set certain currency of contract for this sales channel.
4.  Specify the mark-ups and commissions for services: 1. If you want to set the same amount for all products, suppliers and destinations -- simply put amount of markup and commission into the fields;

![image-20201005-162156.png](/assets/image-20201005-162156.png)

5.  Configure whether sales should happen in original currencies or suppliers of in fixed currency as defined in contract
6.  Click **Save**.

For configuration of flexible hierarchy of conditions for markups&commissions:

1.  Click . The Adding elements window appears:

![image-20201005-162336.png](/assets/image-20201005-162336.png)

2.  In the Adding elements window, set the first-level distinctive item, for example supplier. Select the check boxes compliant to those suppliers for whom you would like to set mark-ups.
3.  Click **Apply**.
4.  Specify the mark up and the mark-up and commission for each supplier appeared on the screen:

![image-20201005-162411.jpg](/assets/image-20201005-162411.jpg)

You can add another level inside the 1st-level classification by suppliers. For example, set separate mark up for accommodation services from a particular supplier. The second-level distinctive properties include product type (accommodation, flights. tours, etc.), group of tags (private, public, etc. See more at Tags), country.

To add a second-level distinctive property,

1.  Click in the required line. The Adding Elements window appears:

![image-20201005-162541.png](/assets/image-20201005-162541.png)

2.  From the Category drop-down, select the distinctive property, e.g. product type.
3.  Select the required check boxes.
4.  Click **Apply**.
5.  Specify the mark up as it was described above.

You can add more levels of distinction. For example, further specify the mark up for hotels located in a particular country/city or of a particular category. To add another level of distinction, follow the steps mentioned above.

![image-20201005-162628.jpg](/assets/image-20201005-162628.jpg)

The figure above illustrates an example of mark up calculation,

- Separate mark ups are added for different suppliers;
- Separate mark up is added for hotels from Amadeus supplier;
- Separate mark up is added for hotels located in France from Amadeus supplier

The tree of mark ups may have a complicated structure. The rules of navigating the tree are as follows:

- Click the arrow next to a folder to expand its constituents;
- To add another level of mark up calculation, click the button opposite the required item.
- To remove an item from the tree, click the button.

You can choose your own logic how to "build" this hierarchy -- e.g. you can start not from suppliers, but from product types or from whatever other criteria that is available in classification field.

Commission column is only available for contracts with Agencies and within groups of contracts. It's not available for Corporate Clients and for Private Clients (within direct or web sales).
