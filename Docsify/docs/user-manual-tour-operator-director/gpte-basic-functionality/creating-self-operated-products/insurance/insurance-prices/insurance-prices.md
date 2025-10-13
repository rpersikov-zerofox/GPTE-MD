# Insurance: Prices

## Tariffs Configuration

Tariff means combination of conditions for price offers -- e.g. you can have:

- *Standard tariff* with regular prices and ability to cancel without fees up to 1 day before the check-in date;
- *Promotional tariff* valid only for certain period with reduced prices, but non-refundable;
- *Early booking tariff* valid only 60 days in advance;
- etc.

To configure a tariff for a self-operated insurance,

1.  On the **Products** menu, click **Insurance**.
2.  In the profile of the required insurance, go to the **Prices tab**.
3.  On the Prices tab, **Tariffs** sub-tab, click **Create**. *Tariff creating* page appears:

![2024-11-13_14-40-20.png](/assets/2024-11-13_14-40-20.png)

4.  On the *Tariff creating* page, specify the tariff description: 1. **Name:** enter the name of the tariff. 2. **Contract number:** specify the number of contract with supplier related to this tariff. 3. **Hide tariff name from client:** select the check box in order to hide the name of the tariff from product customers. 4. **Description for internal use:** locate mouse pointer into the box and enter tariff description. The information entered in the filed is not available for customers and is used for internal aims only. 5. **Currency**: specify the currency of the tariff. 6. **Description:** in the text field enter the tariff description. This description will be shown for customers.
5.  After you have entered the tariff description, click **Save**.

## Flexible Check-in Dates

**This functionality is currently available via administration panel.**

The Flexible check-in dates form helps you establish the period from the service rendering date, when the tariff still will be applied. For example, you set that the tariff is active starting June, 1. You set the flexible check-in period to 3 days. It means that if a tourist searches for insurances and sets that insurance period starts on May, 30, the tariff will still apply to the searched service, since May, 30 is covered by the flexible check-in dates period.

To appoint a flexible check-in dates period, click the bar to expand the form:

![2024-11-13_16-11-29.jpg](/assets/2024-11-13_16-11-29.jpg)

From the drop-down, select the required number of days.

## Price-Lists

To set up a price-list for insurance policy,

On **Products** → Insurance **Prices** tab → **Price-lists** sub-tab click **Create**, *Price-list creating* page appears:

![2024-11-13_16-21-31.jpg](/assets/2024-11-13_16-21-31.jpg)

On the *Price-list creating* page, specify the following information:

1.  **Name:** locate mouse pointer into the box and type the name of the price list.
2.  **Price list is active during:** fill in the required information in the table. Specifically, 1. From the **Tariff** drop-down, select the tariff to connect the price-list to. In case you did not create any tariffs and decided to start with creating other constituent, select the default **Standard** item. 2. In the **Date from**... **to**... group specify the period of the price-list validity. 3. In the **Days of the week** group, select the days on which the price-list will be applied. For example, you can create different price-lists for week days and week-ends. 4. To create a copy of the period, click **Copy**. The identical table line will be created. It may particularly useful in case you create several price-lists with minor differences. It is easier to copy an existing price-list period and make some corrections.
3.  **Description:** locate mouse pointer onto the text field and enter the price-list description.
4.  In the **Prices** section, specify the prices for visa services. Select the method of price calculation: 1. **The price is the same for all the services:** the single price rate is specified for all the insurance types. 2. **The price depends on the type and the time of service:** separate prices are set for each insurance type.
5.  Click **Save**.

**Setting price-lists for customers and suppliers**

**This functionality is currently available via administration panel.**

If you're going to use only your net price-list (based on your contract with supplier) and add markup for your clients within the settings of your sales channels -- then within configuration of your transfer select the option **Use the same price-lists for both customer and supplier**.

![2024-11-13_16-37-56.jpg](/assets/2024-11-13_16-37-56.jpg)

If you want to set separate price-lists for customers and suppliers (not via logic of applying markups, but create absolutely different prices), click **Use net pricelists for supplier and gross price-lists for customer**. Separate forms for net and gross price-lists appear:

![2024-11-13_16-40-48.jpg](/assets/2024-11-13_16-40-48.jpg)

## Setting Commission Plans

To set up commission plan,

1.  On **Products** → Insurance **Prices** tab → **Commission** sub-tab click **Create**, *Commission creating* page appears:

![2024-11-13_16-45-34.jpg](/assets/2024-11-13_16-45-34.jpg)

1.  Specify *the commission name*, as well as the *tariff*, *the period* when it is active, *the description and the currency for commission calculation*.
2.  Specify,

- **Commission per tourist:** specify single commission for the tourist.
- **Commission for extra services.**

1.  Click **Save**.

## Connecting Penalties to a Tariff

To set up a penalty plan,

1.  On the Prices tab → **Penalties** sub-tab, click **Create**:

![image-20201013-085551.png](/assets/image-20201013-085551.png)

1.  In the window, specify the following information: 1. **Name:** type the name of the penalty plan. 2. **Description (for internal use and for tourists):** in the text field describe the penalty plan. 3. **Penalty conditions:** in the group specify the conditions for penalties application and the cancellation charges:

![image-20201013-085822.jpg](/assets/image-20201013-085822.jpg)

1.  from the drop-down select the number of days before the check-in date when the penalties are applied.

2.select whether to calculate penalties in currency units or in per cent from a certain sum.

[3.in](http://3.in) case the penalties are calculated in per cents, specify the price from which they are calculated: total price or a price for a particular number of nights/days.

:   To add another penalty rule, click **Add** button.

d\*\*. Penalties are active during:\*\* in the group, specify the tariff for which the penalty plan will be applied and the terms of its application.

1.  Click **Save**.

## Setting Terms of Use

**This functionality is currently available via administration panel.**

To connect the terms of use to a tariff,

1.  On the Tariff page, click **Terms of use** to expand the form. The following form appears:

![image-20201013-090206.png](/assets/image-20201013-090206.png)

2.  Click **Add**. The Terms of use window appears:

![image-20201013-090250.png](/assets/image-20201013-090250.png)

3.  In the Terms of use window, specify the list of conditions under which the tariff is applied. Specifically, 1. **Early booking more than:** specify the period a tourist has to wait before a visa is ready. 2. **Booking occurs at the day of the specified interval:** the tariff applies if a customer applies for a visa the duration of which is covered by the specified period. 3. **Check in occurs with the specified interval:** the tariff applies only in case check in occurs within the period you specify. 4. **Reservation dates covers at least one day from the specified interval:** the tariff applies only if at least one day of the reservation period is covered by the specified period. *You can link the tariff to one, several or all specified conditions. In the latter case the tariff is applied only if all the conditions are observed.*
4.  Click **Save**.

## Setting Discounts

To set up a price-list for insurance,

On **Products** → Insurance **Prices** tab → **Discounts** sub-tab click **Create**, *Discount creating* page appears:

![image-20201013-090349.png](/assets/image-20201013-090349.png)

1.  On the *Discount creating* page, specify the following information: \* **Name**: locate mouse pointer int the box and type the name of the discount plan. \* **Discount is equal to**: specify the amount of the discount. From the drop-down, select whether to calculate the discount in per cents or in currency units. Then locate mouse pointer into the box and type the value itself. \* **Discount period**: specify the period when the discount is active. \* Specify **dates from ... to** for discount period; \* Choose one option from the list Apply for discount.  Optional: This discount is applied in accordance with the conditions configured in the \"Discounts\" section of this tariff; Always: This is discount applies regardless of tariff. \* Choose the option from the list Discount type who will be provided by.  Supplier\'s discount: A discount that is provided by a supplier and is calculated from the net price;Tour operator\'s discount: A discount that is provided by a tour operator and is calculated from the gross price. Tour operator\'s commission is calculated from the net price. \* **Restrictions on tourists**: specify whether the discount is applied for all tourists or for groups consisting of a particular number of persons only. Click the required option and specify the number of persons in the group if needed. \* **Terms of use**: specify the discount conditions.
2.  Click **Save**.

## Setting Tags

**This functionality is currently available via administration panel.**

Every new product or tariff has a "public" tag by default. This means that they are available for search and booking for all customers.

![image-20201013-090511.jpg](/assets/image-20201013-090511.jpg)

However, you can create additional tags. In this case, if a products or a tariff contains at least one additional tag along with the "public" tag, the conditions of the additional tag are applied to them.

For instance, if you add the "private" tag to the product, it is only displayed in search results for the customers that have access to the "private" products according to the contract. This means that the customer contract must contain either the "private" tag, or several tags, including the mentioned above, for example: the \"public\" and \"private\" tags. The product is unavailable for customers if the "private" tag is not included in their tag list.

Please remember, that in order to manage product availability through tags you should list them in the customer contract in the same way.
