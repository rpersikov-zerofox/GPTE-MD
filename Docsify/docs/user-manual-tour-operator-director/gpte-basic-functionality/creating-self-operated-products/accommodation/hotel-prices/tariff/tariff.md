# Tariff

To create a new tariff,

1.  Open the profile of the required self-operated product.
2.  On the **Prices** tab, **Tariffs** sub-tab, click **Create**. *Tariff creating*page appears:

![2024-11-16_10-26-41.jpg](/assets/2024-11-16_10-26-41.jpg)

3.  Pay attention the Active check box is selected. Otherwise the new tariff will be saved and available for viewing, but won\'t function.
4.  Locate mouse pointer into the **Name** box and type the full name of a tariff.
5.  Locate mouse pointer into the **Contract number** box and enter the contract number for the tariff to be connected to.
6.  Select the **Hide tariff name from client** checkbox in order to hide the name of the tariff from end customers.
7.  Locate mouse pointer into the **Description for internal use** box and type the tariff description. This description will be displayed on the list of the tariffs that are created for the hotel.
8.  Select tariff currency from **Currency** drop-down.
9.  Locate mouse pointer into the **Description** field and describe the peculiarities of the tariff.
10. Click **Save**.

Let us consider the constituents to be filled in on the **Tariff** page.

**Determining check-in dates flexibility** Click the **Flexible check-in dates** bar in order to expand the additional configurations tab.

If you plan to use flexible check-in dates, you should create a separate tariff and set the difference in the number of days from the initial date.

For package tours with fixed duration, for example, those lasting for 7 days, tour operators often organize staying in a hotel according to a fixed schedule. When tourists search for offers they can specify other days and thus the tariff is not displayed in the search results. For example, a tour operator sells offers with the check-in date of September 5 and one week stay. For this purpose the corresponding tariff is created and the allotment for September 5-11 is specified. A tourist searches for the offers at the operator\'s web-site and specifies the following search data: September 6-12. So the offer can not be booked. In order to provide a tourist with an option to view this tariff, you should specify so-called "flexible tariff"

In the Flexible check-in dates section, from the drop-down, select the number of days from the initial date, when this tariff may be offered.

![2025-01-10_14-51-23.jpg](/assets/2025-01-10_14-51-23.jpg)

**Connecting price-lists** In the Price-lists group you can view the list of already connected price-lists, if you are adjusting the tariffs of a previously created hotel, and connect new price-lists.

The table of connected price-lists is displayed as follows:

![2025-01-10_14-53-59.png](/assets/2025-01-10_14-53-59.png)

To edit an existing price-list just update available price-list fields.

To disconnect a price-list from a tariff, click Delete icon opposite the price-list you want to remove.

To connect a new price-list to the tariff, you need to click **Add** button.

**Setting price-lists for customers and suppliers** If you are planning to use several price-lists for mutual settlement with suppliers and clients, you need several price-lists with net prices and gross prices for board and residence service.

Several price-lists can be useful, when some of your suppliers apply complicated pricing schemes. In this case the gross price of the seat can't be set by adding a common mark-up to a net price as usual, but is set separately for different service classes, tourist categories, etc. For better distinction of your price lists and price types we recommend to add \"gross\" and \"net\" to their titles correspondingly. You can set the price-lists that are used for working with clients and suppliers in the tariff settings.

- If you want to include taxes for customers and suppliers, then in tariff settings you can select the option \"\*\*Taxes included\*\*\":

![2025-01-10_14-57-24.jpg](/assets/2025-01-10_14-57-24.jpg)

- If you want to create a new tariff that differs little from existing ones, then in tariff settings you can select the option \"\*\*Inherit prices from the following tariff\*\*\" and add only some changes to new tariff.

![2025-01-10_15-10-25.jpg](/assets/2025-01-10_15-10-25.jpg)

- If you want to set daily rates, click **Use daily rates**.

![2025-01-10_15-10-25.jpg](/assets/2025-01-10_15-10-25.jpg)

- If you use the same price-lists for both a customer and a supplier, click **Use the same price-lists for both customer and supplier.**

![2025-01-10_15-10-25.jpg](/assets/2025-01-10_15-10-25.jpg)

- If you use different price-lists for customers and suppliers, click **Use net price-lists for supplier and gross price-lists for customer**. Separate forms for net and gross price-lists appear:

![2025-01-10_15-14-53.png](/assets/2025-01-10_15-14-53.png)

- If initially you click **Use the same price-lists for both customer and supplier**, add the price-list to the tariff and click **Use net price-lists for supplier and gross price-lists for customer**, your price-list is displayed in the Net price-lists group.

You can set several tariffs with different payment methods for one product.

**Price calculation for Search&Book** If you click **Use the same price-lists for both customer and supplier** option when editing the tariff, price calculation is implemented in the following way:

- The net-price of the service (the amount that is paid to a supplier) is equal to the price in the price-list after minus the supplier's discount and tour operator's commission, which is calculated according to the actual commission plan: **Net price = The price in the price-list -- Supplier's discount -- Tour operator's commission**
- The gross-price (the price for a tourist) is equal to the net-price with the tour operator's mark-up minus supplier's and tour operator's discounts: **Gross price = The price in the price-list + Tour operator's mark-up -- Supplier's discount -- Tour operator's discount**

If you click **Use net price-lists for supplier and gross price-lists for customer** when editing the tariff, the price calculation will be implemented in the following way:

- The net-price of the service (the amount that is paid to a supplier) is equal to the price, specified in the \"net\" price-list minus supplier's and tour operator's discounts: **Net price = The price in the price-list with net-prices -- Supplier's discount -- Tour operator's commission**
- The gross-price (the price for a tourist) is equal to the price, specified in the \"gross\" price-list with the tour operator's mark-up minus tour operator's discount: **Gross price = The price in the price-list with gross-prices -- Tour operator's discount + Tour operator's mark-up**

If you choose **Use net price-lists for supplier and gross price-lists for customer** and the price-list does not affect certain dates, all offers for this date are not displayed in the search results.

**Penalties** To connect a penalty plan to a tariff,

1.  On the tariff page, click **Penalties** to expand the form. The following form appears:

![2025-01-10_15-15-31.jpg](/assets/2025-01-10_15-15-31.jpg)

2.  Click **Add**. The Penalty record appears:

![2025-01-10_15-17-25.jpg](/assets/2025-01-10_15-17-25.jpg)

3.  From the Name of the penalty to be applied within the indicated tariff drop-down, select the item of your choice. Specifically, 1. In case you have previously created a separate penalty plan on the Prices tab, select the required one from the drop-down. 2. In case you create a tariff first, click **Penalty creating**from\*\* Name \*\*drop-down. The New penalty window appears.

![2025-01-10_15-20-33.png](/assets/2025-01-10_15-20-33.png)

4.  Click **Save**. The new penalty plan is added to the tariff.

**Board types**

**This functionality is currently available via administration panel.** In the Board types group, define which of the previously created board types should be displayed on the Search results page and which should be displayed as alternatives. To specify the board types for the tariff,

1.  Click **Board types** to expand the form. The following form appears:

![2025-01-10_15-21-17.png](/assets/2025-01-10_15-21-17.png)

2.  Opposite a certain board type, select the check box corresponding to the required mode of display.
3.  Click **Save**.

**Terms of use** To connect the terms of use to a tariff,

1.  On the Tariff page, click **Terms of use** to expand the form. The following form appears:

![2025-01-10_15-24-40.png](/assets/2025-01-10_15-24-40.png)

2.  Click **Add**. The Terms of use record appears:

![2025-01-10_15-25-23.png](/assets/2025-01-10_15-25-23.png)

3.  In the Terms of use window, specify the list of conditions under which the tariff is applied. Specifically, 1. **Days prior to the service rendering date:** the tariff only applies if a customer books a service a specified number of days before a service start date. 2. **Booking dates from-to interval:** the tariff applies if a customer books a service on any day within the specified interval. 3. **Check in dates from-to interval:** the tariff applies if the check-in date is covered by the interval you specify.

**Limits of citizenship** Some hotels offer different prices for customers depending on the client's citizenship. You can customize on the search results the availability of a particular tariff for self-operated hotel, depending on the specified nationality of the guest.

![2025-01-10_15-27-10.png](/assets/2025-01-10_15-27-10.png)

**Membership level** This option helps to apply corresponding prices during the search under B2C members or non-members access.

![2025-01-10_15-27-57.png](/assets/2025-01-10_15-27-57.png)

**Payment terms**

**This functionality is currently available via administration panel.** In the Payment terms section, select the payment method: either to the tour operator or directly to the supplier.

![image-20200921-075313.jpg](/assets/image-20200921-075313.jpg)

Click the button of your choice.

**Discounts**

**This functionality is currently available via administration panel.** To connect a discount to a tariff,

1.  On the Tariff page, click **Discounts** to expand the form. The following form appears:

![image-20200922-084003.png](/assets/image-20200922-084003.png)

2.  Click **Add**. The Discounts window appears:

![image-20200922-084129.png](/assets/image-20200922-084129.png)

3.  In the Discounts window, from the\*\* Add\*\* drop-down, select the item of your choice. Specifically, 1. In case you have previously created a separate discount, select the required one from the drop-down. 2. In case you create a tariff first, click **Create discount**.
4.  Specify the discount validity period. Select the required dates on the calendar.
5.  Specify the type of discount: supplier\'s discount or tour operator\'s discount. The description for each type is displayed in the Discounts window. 1. Supplier\'s discount: the discount is provided by a supplier and is calculated from the net price. 2. Tour operator\'s discount: the discount is provided by you and is calculated from gross price, while your commission is calculated from the net price.
6.  Click **Apply**.

To make any corrections to a created discount, select the required one from the dropdown and click . The Discount window appears where you can make the required corrections.

**Tags** Every new product or tariff has a "public" tag by default. This means that they are available for search and booking for all customers.

![image-20200922-084434.png](/assets/image-20200922-084434.png)

However, you can create additional tags. In this case, if a product or a tariff contains at least one additional tag along with the "public" tag, the conditions of the additional tag are applied to them.

For instance, if you add the "private" tag to the product, it is only displayed in search results for the customers that have access to the "private" products according to the contract. This means that the customer contract must contain either the "private" tag or several tags, including the mentioned above, for example, the \"public\" and \"private\" tags. The product is unavailable for customers if the "private" tag is not included in their tag list.

Please remember, that in order to manage product availability through tags you should list them in the customer contract in the same way.

**Setting reservation modifications** On the Setting reservation modifications tab you can set conditions upon which users can modify hotel booking reservations. Select from the following options:

- Allow to change dates: users can change check-in and check-out dates for tourists.
- Allow to change tour leader: users can change the name and the surname of a tourist, specified as a tour leader in the current order.
- Allow to change all tourists except tour leader: users can change names and surnames of all tourists in the order except for a tour lead.

![image-20200922-092831.png](/assets/image-20200922-092831.png)
