# Setting Tariffs

To develop a tariff for a self-operated flight,

1.  In the **Products** menu, click Flights.
2.  Click the required flight and go to the Prices tab.
3.  On the Prices tab, in the\*\* \*\*Tariffs sub-tab, click Create. Tariff creating page appears:

![2024-10-29_11-26-44.jpg](/assets/2024-10-29_11-26-44.jpg)

1.  On the Tariff creating page, first, specify the tariff description: 1. **Name:** locate mouse pointer into the box and enter the name of the tariff. 2. **Contract number:** the contract number for the tariff to be connected to. 3. **Hide tariff name from client:** select the checkbox in order to hide the name of the tariff from product customers. 4. **Description for internal use:** locate mouse pointer into the box and enter tariff description. The information entered in the filed is not available for customers and is used for internal aims only. 5. **Description:** in the text field enter the tariff description.
2.  Click Save.

**Price-lists**

**Adding Price-lists within Tariff functionality is currently available via administration panel.** Click the Price-lists bar to expand the form. The following form appears:

![image-20200922-082038.jpg](/assets/image-20200922-082038.jpg)

To connect a price-list you need to:

- Specify price-lists for working with your suppliers and clients.
- Add corresponding price-lists to the tariff.

**Setting price-lists for customers and suppliers** If you are planning to use several price-lists for mutual settlement with suppliers and clients, you need several price-lists with net prices and gross prices for board and residence service.

Several price-lists can be useful when some of your suppliers apply complicated pricing schemes. In this case, the gross price of the seat can't be set by adding a common mark-up to a net price as usual but is set separately for different service classes, tourist categories, etc. For better distinction of your price lists and price types, we recommend adding \"gross\" and \"net\" to their titles correspondingly. You can set the price-lists that are used for working with clients and suppliers in the tariff settings.

If you want to create a new tariff that differs little from existing ones, then in tariff settings you can select the option \"Inherit prices from the following tariff\" and add only some changes to the new tariff.

![image-20200922-082424.png](/assets/image-20200922-082424.png)

If you use the same price-lists for both a customer and a supplier, click Use the same price-lists for both customer and supplier.

![image-20200922-082904.png](/assets/image-20200922-082904.png)

If you use different price-lists for customers and suppliers, click Use net price-lists for supplier and gross price-lists for customer. Separate forms for the net and gross price-lists appear:

![image-20200922-082934.png](/assets/image-20200922-082934.png)

If initially you click Use the same price-lists for both customer and supplier, add the price-list to the tariff and click Use net price-lists for supplier and gross price-lists for customer, your price-list is displayed in the Net price-lists group.

Note: You can set several tariffs with different payment methods for one charter.

**Price calculation for Search&Book** If you click Use the same price-lists for both customer and supplier option when editing the tariff, price calculation is implemented in the following way:

- The net-price of the service (the amount that is paid to a supplier) is equal to the price in the price-list after minus the supplier's discount and tour operator's commission, which is calculated according to the actual commission plan: **Net price = The price in the price-list -- Supplier's discount -- Tour operator's commission**
- The gross-price (the price for a tourist) is equal to the net-price with the tour operator's mark-up minus supplier's and tour operator's discounts: **Gross price = The price in the price-list + tour operator's mark-up -- supplier's discount -- tour operator's discount**

If you click Use net price-lists for supplier and gross price-lists for customer when editing the tariff, the price calculation will be implemented in the following way:

- The net-price of the service (the amount that is paid to a supplier) is equal to the price, specified in the \"net\" price-list minus supplier's and tour operator's discounts: **Net price = The price in the price-list with net-prices -- Supplier's discount -- Tour operator's commission**
- The gross-price (the price for a tourist) is equal to the price, specified in the \"gross\" price-list with the tour operator's mark-up minus tour operator's discount: **Gross price = The price in the price-list with gross-prices -- Tour operator's discount + Tour operator's mark-up**

Note: If you choose Use net price-lists for supplier and gross price-lists for customer and the price-list does not affect certain dates, all offers for this date are not displayed in the search results.

**Penalties**

**Adding Penalties within Tariff functionality is currently available via administration panel.** To connect a penalty plan to a tariff,

1.  On the tariff page, click Penalties to expand the form. The following form appears:

![image-20200922-083057.png](/assets/image-20200922-083057.png)

2\.

![image-20200922-084003.png](/assets/image-20200922-084003.png)

3.  From the Name of the penalty to be applied within the indicated tariff drop-down, select the item of your choice. Specifically, 1. In case you have previously created a separate penalty plan on the Prices tab, select the required one from the drop-down. 2. In case you create a tariff first, click Create. The New penalty window appears. 3. Fill in the required information the way it is described in Penalties.

![image-20200922-084129.png](/assets/image-20200922-084129.png)

4.  Click Save. The new penalty plan is added to the tariff.

**Terms of use**

**Adding Terms of use within Tariff functionality is currently available via administration panel.** To connect the terms of use to a tariff,

1.  On the Tariff page, click Terms of use to expand the form. The following form appears:

![image-20200922-084227.jpg](/assets/image-20200922-084227.jpg)

2.  Click Add. The Terms of use window appears:

![image-20200922-084434.png](/assets/image-20200922-084434.png)

3.  In the Terms of use window, specify the list of conditions under which the tariff is applied. Specifically, 1. **Early booking a certain number of days before the check-in:** the tariff only applies if a customer books a service a specified number of days before a service start date. 2. **The offer is booked within the period:** the tariff applies if a customer books a service any day within the specified interval. 3. **Charter is performed any day:** the tariff applies if the charter is performed on any day from the specified range. 4. **Direction:** the tariff applies to the selected types of charters.
4.  Click Save.

**Membership level**

**Adding Membership level within Tariff functionality is currently available via administration panel.** This option helps to apply corresponding prices during the search under B2C members or non-members access.

![image-20200922-092552.png](/assets/image-20200922-092552.png)

**Discounts**

**Adding Discounts within Tariff functionality is currently available via administration panel.** To connect a discount to a tariff,

1.  On the Tariff page, click Discounts to expand the form. The following form appears:

![image-20200922-092831.png](/assets/image-20200922-092831.png)

2.  Click Add. The Discounts window appears:

![image-20200922-092910.png](/assets/image-20200922-092910.png)

3.  In the Discounts window, from the\*\* \*\*Add drop-down, select the item of your choice. Specifically, 1. In case you have previously created a separate discount, select the required one from the drop-down. 2. In case you create a tariff first, click Create discount.
4.  Specify the discount validity period. Select the required dates on the calendar.
5.  Specify the type of discount: supplier\'s discount or tour operator\'s discount. The description for each type is displayed in the Discounts window. 1. Supplier\'s discount: the discount is provided by a supplier and is calculated from the net price. 2. Tour operator\'s discount: the discount is provided by you and is calculated from gross price, while your commission is calculated from the net price.
6.  Click Apply.

**Tags**

**Adding Tags within Tariff functionality is currently available via administration panel.** Every new product or tariff has a "public" tag by default. This means that they are available for search and booking for all customers.

![image-20200922-093609.png](/assets/image-20200922-093609.png)

However, you can create additional tags. In this case, if a product or a tariff contains at least one additional tag along with the "public" tag, the conditions of the additional tag are applied to them.

For instance, if you add the "private" tag to the product, it is only displayed in search results for the customers that have access to the "private" products according to the contract. This means that the customer contract must contain either the "private" tag or several tags, including the mentioned above, for example, the \"public\" and \"private\" tags. The product is unavailable for customers if the "private" tag is not included in their tag list.

Note: Please remember, that in order to manage product availability through tags you should list them in the customer contract in the same way.
