# Setting Contracts with Agencies

**This functionality is currently available via administration panel.**

For managing contracts with agencies there are two alternatives:

- You can group several agencies and configure the same contract conditions for the whole group.
- You can specify an individual contract for a particular agency.

In case you want to configure an individual contract that regulates the relationship between your company and an agency,

1.  On the Navigation menu, point to **Clients**, click **Agencies/Distributors** and then click the client company for which you need to configure the contract terms.
2.  Click the **Contract** tab, and then click **Edit** to switch to the editing mode.

![image-20201002-134526.jpg](/assets/image-20201002-134526.jpg)

3.  Configure the terms of contract as described below in further subsections.
4.  Click **Save**.

According to specific settings of your installation version, you can define the currency that is used for settlements with the client company: the supplier\'s currency or the contract one. Depending on this parameter chosen, the prices might be shown in the specified currency on the search and book forms, and on the Reservations page.

**Assigning Managers**

An employee of your company can be appointed as a Manager. The Manager supervises a client travel agency/distributor or direct sales and manages their reservations. Any user with the **Director**, or the **Supervisor**, or the **Manager** role can act as a manager.

*Assigning a Manager is an obligatory condition for regular operations. You cannot create a reservation in the system if a manager for a particular travel agency/sales channel is not defined.*

*If you change a manager in the contract settings, all the previously created reservations are automatically assigned to a new manager.*

When changing your managers in the contract settings, you should specify the reservations they will be accountable for: new and existing reservations or new reservations only. In the list of reservations this manager will be specified as a manager in charge of the selected orders.

![image-20201002-134813.png](/assets/image-20201002-134813.png)

The first step of setting a contract is defining travel products which are to be sold in compliance with the contract terms. On the Products tab, specify travel products and services that fall under the regulations of a contract.

![image-20201002-135434.png](/assets/image-20201002-135434.png)

1.  Click **Edit** to switch to the editing mode.
2.  Select the required check boxes.
3.  Click **Save** to save the changes.

In the Calculation subsection specify the mark up and commission calculation. The type of calculation depends on the type of the partner and the approved way of pricing.

There are two ways of pricing:

![image-20201002-140213.png](/assets/image-20201002-140213.png)

- **Markup:** a standard form of payment for tour operators. If you select the Markup calculation, your partner company will be able to set sale prices independently by adding a markup to the rates displayed in its system (commission value is 0). The markup value is set in percent or in fixed amount in certain currency. For example, a double room offered by your company costs EUR 100. With a 20% markup you can sell it to your partner for EUR 120. In his turn, the partner can add its own markup to your sale price. In this case your profit will be EUR 20, while your partner's profit will depend on the defined markup.
- **Commission:** a standard form of payments for travel agencies. With the Commission payment your partner will sell products and services at fixed rates. These rates already include agency's commission for each sale (markup and commission are defined).

**Pricing methods** You can set markups and commissions in percent or in fixed amount with the Switch button .

There are several ways to calculate a sale price in percentage and fixed amount:

- The calculation of a sale price in percent is based on the full cost of the service. For example the net price is EUR 100 and the markup is 20%, the total price is then calculated by the following formula: Total price = net price + markup = 100+20 = EUR 120.
- The fixed commission is calculated based on the service rate per night. For example the room is booked for 5 nights with the net rate of EUR 100 per night and a markup of EUR 20. The total price is then calculated by the following formula: Total price = net price \* number of nights + markup \* number of nights = 100\*5 + 20\*5 = EUR 600

**Configuring markup** On the Calculation tab, set the rules for price calculation, specifically:

- Set the contract currency to perform sales
- Specify the mark-ups
- Specify the commission for services
- Specify whether to use original currency from suppliers or the currency specified in the contract.

Please pay attention that for direct sales contract setting, setting commission is unavailable.

To set the rules for price calculation,

1.  On the Calculation tab, click **Edit** to switch to editing mode.

![image-20201002-155211.png](/assets/image-20201002-155211.png)

2.  From the Currency drop-down, select the currency of contract.
3.  Specify the mark-ups for services: 1. Click . The Adding elements window appears:

![image-20201002-155609.png](/assets/image-20201002-155609.png)

![image-20201002-155807.png](/assets/image-20201002-155807.png)

You can add another distinctive property inside the 1st-level classification by suppliers. For example, set separate mark up for accommodation services from a particular supplier. The second-level distinctive properties include product type (accommodation, flights. tours, etc.), group of tags (private, public, etc. See more at Tags), country.

To add a second-level distinctive property,

1.  Click opposite the required supplier. The Adding Elements window appears:

![image-20201002-160028.png](/assets/image-20201002-160028.png)

2.  From the **Category** drop-down, select the distinctive property.
3.  In case of specifying mark up for accommodation, select by product type.
4.  Select the required check boxes.
5.  Click **Apply**.
6.  Specify the mark up as it was described above.

You can add more levels of distinction. For example, further specify the mark up for hotels located in a particular country/city or of a particular category. To add another level of distinction, follow the steps mentioned above.

![image-20201002-160222.jpg](/assets/image-20201002-160222.jpg)

The figure above illustrates an example of mark up calculation,

- Separate mark ups are added for different suppliers;
- Separate mark up is added for hotels from Amadeus supplier;
- separate mark up is added for hotels located in France from Amadeus supplier.

The tree of mark ups may have a complicated structure. The rules of navigating the tree are as follows:

- Click the arrow next to a folder to expand its constituents;
- To add another level of mark up calculation, click the button opposite the required item.
- To remove an item from the tree, click the button.

From the **End-price VAT** and **Commission VAT** drop-downs, specify the VAT rate.

**End-price VAT:** the VAT will be applied to the final price for a service;

**Commission VAT:** the VAT will be applied only to the commission rate.

The items available in the drop-downs, should be previously specified in the Payment settings sectoin.

To set the VAT plan,

1.  On the Navigation bar, point to Finance and click Payments settings.
2.  Click VAT to proceed to the VAT tab.
3.  On the VAT tab, click Create to add a new VAT plan.
4.  In the New VAT plan window, fill in the required information.
5.  Click Save. The new VAT plan is added to the list.

For further information, please see .

In the sales terms section, specify the minimal number of days from the date of booking to the date when the service is rendered. Assuming today is August 12, 2022 and the restriction period is 5 days, then a user will not be able to submit the reservation until August 17.

On the Sales terms tab,

1.  Click Edit to switch to editing mode.
2.  Configure the following: 1. Availability of services 2. Printing vouchers 3. Sales mode 4. Credit limit 5. Payment plan
3.  Click Save.

**Availability of services** Specify the date when a service becomes available for direct sales in respect of the service start date:

![image-20201002-161802.jpg](/assets/image-20201002-161802.jpg)

Select the required number of days from the drop-down opposite the service of your choice. Let us consider an example. You set the availability period for tour booking to 14 days. The tour start date id July, 18. It means that the tour becomes available for direct sales starting July, 4.

**Printing vouchers:** Configure the printing of vouchers:

![image-20201002-161920.png](/assets/image-20201002-161920.png)

Click the button of your choice:

- Always: the voucher is printed after the reservation confirmation.
- After payment only: the voucher is printed only after a tourist pays for the booked service.
- After disabling AUTOCANCELLATION only: Autocancellation presupposes canceling the service the number of days before the commission period starts. The option may be set selected by default. In this case the voucher will be printed only when a user deselects the Autocancellation option.
- Never: The voucher printout is disabled.

**Sales mode** With the **Sales Mode Activation** parameters you can set which sales channels will be available withing the current contract.

![image-20201002-162043.png](/assets/image-20201002-162043.png)

- B2B: If a B2B channel is selected, you will be able to sell products to other companies as well as directly to tourists from an office.
- B2C: With the B2C channel a company can provide tourists with tour products directly via a B2C website.
- Both B2B and B2C: Activate both sales channels if you want to use all sales channels for distribution of tour products.

If you select the B2C sales channel, you still will be able to enter a B2B system and obtain information on the reservations made by tourists via web-site. However you will not be able to search and book services in the B2B system.

**Credit limit** With the The Credit Limit parameter you can set the price range within which your clients can book or invoice services paying for them later:

![image-20201002-162244.png](/assets/image-20201002-162244.png)

- First select the check boxes compliant to the types of services for which you wan to set a credit limit: booked services, invoices services or combined.
- Specify the credit limit: locate mouse pointer into the box and type the credit limit value.

**Payment plan** With the The Payment Plan parameter you can define basic set of methods of payment.

As clients of tour operator who bought your service for further sale (travel agents and tourists that bought services via B2C web-site) don't have the possibility to manage contract settlements of this tour operator with its supplier, it's necessary to specify payment plans or some mutually exclusive methods of payment (for example, when the first specified method is applied only before the penalty period, then the second is applied after it).

![image-20201002-162356.png](/assets/image-20201002-162356.png)

From the drop-down select the required payment plan.

Please note that the payment plans available in the list should be previously configured. For more information click Finance. (See Payment settings).

On the Cross-rates tab you can set the increases to the exchange rates.

The rates for products and services can be displayed in different currencies. You convert rates into single currency -- the one you use in your company as the accounting currency. For such conversions the system uses currency exchange rates established on the day of payment. According to the common practice a fixed percentage is added to these rates.

For example the exchange rate is EUR 1 = BGN 36,1715. With a 3% increment to the rate it will be BGN 37,2603. Locate mouse pointer into the respective boxes and specify the cross-rate for the currencies:

![image-20201002-163531.png](/assets/image-20201002-163531.png)

With the cancellation fees configuration, you can specify the terms and conditions for canceling services booked withing the direct sales channel.

You can set your own cancellation conditions and adjust the cancellation conditions of suppliers:

- Independent (own) cancellation policies: In the group, specify the duration of the penalty period, the per cent rate of the cancellation fee, and the price from which the cancellation fee is calculated (usually total cost; for hotels the one night option is available).
- Management of supplier cancellation policies: In the group, specify the shift of deadline and the value by which the cancellation fee increases.

![image-20201002-163901.jpg](/assets/image-20201002-163901.jpg)

- The agency\'s penalty charge is set in percent from the full price of a product or service or the price of the product for the first night, including the tour operator's markup.
- To configure the deadline and the amount of a penalty charge you can set up your own terms of the penalty application and connect these to the penalty charges applied by the supplier.
- The strictest penalty provisions have the highest priority, that is those with higher penalty charge or that are applied earlier.

**Penalty calculation rules**

Supposing a travel agency books a hotel room from your company for June 1-5, 2022. The total room rate from the supplier is 200 EUR and the markup is 20%, thus the service is sold to the travel agency for 240 EUR (which makes EUR 60 per night). The initial cancellation terms set by the supplier include penalty charges of 50 per cent of the total service rate if the booking is canceled seven or fewer days before the service start date.

**Case 1. Cancellation terms are not specified in the contract** If you specify no values either for independent cancellation terms or for supplier penalty charges, the initial cancellation terms set by the supplier are applied.

![image-20201002-171027.jpg](/assets/image-20201002-171027.jpg)

In our case this means that the penalty charges are applied on May 25, 2022. If the travel agency cancels the reservation within the period from May 25-31, it pays you 120 EUR of penalty charge (50% of the supplier rate including the markup 240 EUR). In your turn, you pay 100 EUR to your supplier (50% of the supplier rate). 20 EUR difference is your company profit.

**Case 2. Cancellation terms are specified for supplier penalty charges only** If you enter no values for independent cancellation terms, but set up the shift of deadlines and increase of the initial supplier penalty charge, then the supplier penalty charges are applied in accordance to your settings.

![image-20201002-171250.jpg](/assets/image-20201002-171250.jpg)

Thus, if you set the shift of the cancellation deadline for 3 days and set the increase of the penalty charge to 10 per cent, then the penalty period will be extended to 10 days:

cancellation period = 7 days according to supplier's terms + 3 days according to your terms.

The penalty period starts on May 22, that is 3 days before the supplier\'s cancellation terms start. At the same time the amount of penalty charge additionally increases by 10 per cent of the initial supplier penalty charge including the markup of the tour operator.

In this case if a reservation is canceled within the period from May 22 to May 31, the travel agency pays the penalty charge of 132 EUR.

120 EUR (50% of the initial supplier\'s penalty charge including the tour operator\'s markup) + 10% (penalty increase) = 132 EUR Penalty charge

You pay 100 EUR to the supplier. The remaining amount of 32 EUR is your company profit. Similarly you can configure supplier\'s penalty terms by changing only the deadline shifts or the penalty charge increase

**Case 3. Only independent (your own) cancellation terms are set up.** If you set up only your custom cancellation terms and they overlap with the initial penalty charge terms set by a supplier for some dates, stricter penalty rules are applied for these dates.

**Example А.** Assume that you set up a 100 per cent penalty charge if the service is canceled five days before it is rendered.

![image-20201002-171450.jpg](/assets/image-20201002-171450.jpg)

In this case:

- If the service is canceled during the period from May 25 to May 26, the travel agency pays you the penalty charge of 120 EUR (according to the supplier cancellation terms).
- If the service is canceled during the period from May 27 to May 31, the travel agency pays you the penalty fees of 240 EUR (according to your independent cancellation terms, because they are stricter than those applied by the supplier).

**Example B** Suppose you set stricter conditions, according to which the cancellation of the service 10 days before it is rendered results in 100% penalty charge.

![image-20201002-171631.jpg](/assets/image-20201002-171631.jpg)

In this case if the service is canceled during the period from May 22 to May 31, the travel agency pays you a penalty charge of 240 EUR (your independent cancellation conditions are applied since they are stricter than those of the supplier throughout the whole penalty period). You can configure the calculation of penalty charge by using the percentage of the total price of the service as well as that of the first night.

**Example C.** Suppose you set up a rule according to which a penalty charge of 100% of the price of the first night is charged if the service is canceled five days before it is rendered.

![image-20201002-171755.jpg](/assets/image-20201002-171755.jpg)

In this case:

- If the service is canceled during the period from May 25 to May 26, the travel agency pays you 120 EUR of penalty fees (according to the supplier cancellation terms).
- If the service is canceled during the period from May 27 to May 31, the travel agency pays you the same 120 EUR of penalty fees, since the supplier cancellation fees are stricter than yours.

**Example D.** Suppose you set up a condition according to which the penalty of 100% of the price of the first night is charged if the service is canceled 10 days before it is rendered.

![image-20201002-171918.jpg](/assets/image-20201002-171918.jpg)

In this case:

- If the service is canceled during the period from May 22 to May 24, the travel agency pays you 60 EUR penalty fees (according to your own terms, since the terms of the supplier are not yet active).
- If the service is canceled during the period from May 25 to May 31, the travel agency pays you 120 EUR penalty charge (the supplier cancellation are applied since they are stricter than yours).

**Case 4. All possible cancellation terms are set up** You can set up custom cancellation conditions and change the cancellation conditions of the supplier at the same time. In this case stricter penalty conditions are used to determine the amount of charge and the deadline.

**Example A.** Suppose you set up a rule, according to which a penalty of 100% of the total service price is applied if the the service is canceled five days before it is rendered. Additionally you shift the supplier's penalty deadline by 3 days and increase the penalty charge by 25%.

![image-20201002-172050.jpg](/assets/image-20201002-172050.jpg)

In this case the shifted penalty deadline attaches from May 22 and if the service is canceled during the period from May 22 to May 26, the travel agency pays you 150 EUR of penalty charge (0,5\*240 +25%). Your custom penalty charges take effect starting from May 27 and since it is stricter than that of the supplier, if the service is canceled within the period from from May 27 to May 31, the travel agency pays you 240 EUR.

**Example B.** Suppose you set up a condition, according to which the cancellation that occurs five days before the service is rendered results in 100% penalty fee of the first night. Additionally you shift the supplier's penalty deadline by 3 days and increase the penalty charge by 25%.

![image-20201002-172218.jpg](/assets/image-20201002-172218.jpg)

In this case the shifted supplier\'s penalty charges take effect from May 22 and if the service is canceled within the period from May 22 to May 26, the travel agency pays 150 EUR (0,5\*240 +25%) to you.

Your custom cancellation terms take effect starting from May 27 (that include the penalty charge of 60 EUR payable by the travel agency), but since your conditions are less strict than those of the supplier (150 EUR), if the service is canceled within the period from May 27 to May 31, the conditions of the supplier are still active and the travel agency pays 150 EUR to you.

Here you can:

- Enable requst invoices for customer
- Allow the client to request an invoice for prepayment
- Apply custom currency recalculation rules
- Allow to edit/cancel services after the issuing of invoice

![image-20201002-172354.jpg](/assets/image-20201002-172354.jpg)

One and the same service can have different names and be provided by different suppliers. As a result, this service can be displayed in the search results as several different services. For example, you have a direct contract with the Hilton hotel located in Prague. However the same hotel is sold as a part of the agreement with GTA, Hotelbeds and RoomsXML suppliers. You want all the variants for this hotel to be displayed as one offer, when searching hotels in Prague. By using GP Travel Enterprise, you can group identical services from different suppliers and display them as one offer. To do this, you should group respective hotels and specify the rules of displaying hotels of this group in contract settings.

On the Grouping tab you can configure the conditions of displaying the groups of services:

1.  Select the product for which you would like to configure grouping conditions. After you select a service, the following form appears:

![image-20201002-172603.png](/assets/image-20201002-172603.png)

2.  Select one of the following options: 1. Show all offers in group: in this case all services that are included in the group are displayed on the search results page as one offer. At the same time if you click **Hide offers** when browsing search results, the best offer of all the offers included in the group is displayed. To see all other offers from the group, click **All offers**. 2. **Remove duplicating offers** and 1. show only the cheapest among them: in this case, only the best offer, excluding all other hotels of the group is displayed. 2. show the most profitable offers for Tour Operator: in this case the most profitable offer of the group is displayed.

![image-20201002-172703.jpg](/assets/image-20201002-172703.jpg)

3.  For hotels, besides the basic grouping configurations, the additional form appears:

![image-20201003-132205.png](/assets/image-20201003-132205.png)

Mark up adjustment:

- Click the Adjust mark up check box.
- Set the values for mark up adjustment: \* Click either of the buttons to calculate the values in per cents or in currency units. \* Specify the value.

1.  Click Save.

By using tags you can manage access of certain groups of customers to products and rates. For example, by labeling certain products with the \"private\" tag you show them only to the customers that are interested in exclusive offers, while the standard offers with the \"public\" tag are available to all customers.

You can create, edit and delete all tags, except for the default \"public\" tag. There are certain restrictions to the tag names:

- A tag name should consist of one or several words written in Latin characters.
- A tag name can include maximum 500 characters.
- If you use several tags, they should be separated with a comma

**Setting tags for products and tariffs** Every new product or tariff has a "public" tag by default. This means that they are available for search and booking for all customers.

![image-20201003-132423.jpg](/assets/image-20201003-132423.jpg)

However, you can create additional tags. In this case, if a products or a tariff contains at least one additional tag along with the "public" tag, the conditions of the additional tag are applied to them.

For instance, if you add the "private" tag to the product, it is only displayed in search results for the customers that have access to the "private" products according to the contract. This means that the customer contract must contain either the "private" tag, or several tags, including the mentioned above, for example: the \"public\" and \"private\" tags. The product is unavailable for customers if the "private" tag is not included in their tag list.

Please remember, that in order to manage product availability through tags you should list them in the customer contract in the same way

**Setting tags in a contract**

By default only products with the "public" tag are specified as available in the contract. This means that all the products marked with other tags are not available for customers unless you add these tags to the customer\'s contract.

Thus, to tag products as "private" and make them available for the customer you should add a respective tag in the customer contract:

![image-20201003-132531.jpg](/assets/image-20201003-132531.jpg)

After this, the products tagged as "public" as well as products tagged as"private" are displayed in the search results for this customer.

On the contrary if you want to make products with certain tags unavailable to the certain type of customers, place a respective tag into the **Products marked with these tags will not be offered via this contract**box:

![image-20201003-134407.png](/assets/image-20201003-134407.png)

As a result, the customer can access all your offers except for those tagged with the "VIP" tag.

If you use the same tag in both the fields of the contract, the excluding tag has a priority. The products tagged with it are not displayed.

**Managing offer availability from suppliers** You can use tags to determine the suppliers whose offers are available to a particular customer or for a particular sales channel. All possible options are listed in the table below.

  -----------------------------------------------------------------------------------------------------------------------------
  **Offers from the suppliers that need to be displayed**         **Tag that needs to be specified in the contract settings**
  --------------------------------------------------------------- -------------------------------------------------------------
  From all the suppliers (both external and your own suppliers)   \*:public,public

  From all external suppliers                                     public

  From one of the external suppliers                              :public,supplier:SupplierСode

  From all direct contracted suppliers                            \*:public

  From one of the direct contracted suppliers                     SupplierTag:public
  -----------------------------------------------------------------------------------------------------------------------------

**Table comments:** The supplier code for external suppliers and GDSs cannot be ascribed manually in the profile of a supplier. To determine the external supplier whose products are available for a particular customer or sales channel, in the contract settings of the customer, use the respective code that corresponds to the particular external supplier (see the table below).

  --------------------------------------------
  Supplier               Code (SupplierCode)
  ---------------------- ---------------------
  Abreu                  abreu

  Academservice          academ

  Aeroexpress            aeroexpres

  Alphastrakhovanie      alpha

  Amadeus                amadeus

  Air Canada Vacations   ACV

  A&A                    aeroclub

  Alean                  alean

  AmandaTour             amanda

  CarDelMar              cardelmar

  CarTrawler             cartrawler

  Diethelm               diethelm

  Dolphin                dolphin

  DOTW                   dotw

  Eurotours              eurotours

  Expedia                expedia

  Galileo                galileo

  GoGlobal               goglobal

  GTA                    gta

  Generation-P           gp

  HBSi                   hbsi

  Hotelbeds              hotelbeds

  HotelsPro              hotelspro

  Hotusa                 hotusa

  iWay                   iway

  JacTravel              jacob

  Jumeirah               jumeirah

  Kandagar               kandagar

  Kuoni                  kuoni

  Miki                   miki

  Multitur               multitur

  Novasol                novasol

  ATS Pacific            pacific

  RoomsXML               rooms

  RCR                    rcr

  Roza Vetrov            roza

  Sirena travel          sirena

  Terramar               terramar

  Tourico                tourico

  TOWERS                 towers

  Travco                 travco

  Viator                 viator
  --------------------------------------------

For your own contracted suppliers, you can specify the Supplier code manually by entering the tag prefix in the profile of a direct contracted supplier.

1.  On the Navigation bar, point to **Suppliers** and click **Suppliers**.
2.  In the **Name** column, click the supplier of your choice.
3.  On the **Supplier** page, click **Edit** to switch to editing mode.
4.  Locate mouse pointer into the **Tag prefix** box and type the supplier code.
5.  Click **Save.**

Let us consider an example of tag application for external and direct contracted suppliers.

- To ensure the availability of offers from the external Hotelbeds supplier only, in the client contract settings (Navigation bar - Clients - Contract - Tags), add the following tag:

![image-20201003-135623.png](/assets/image-20201003-135623.png)

- To ensure the availability of offers from the direct contracted Travel Guard supplier only, in the client contract settings, add the following tag: supplier:travelguard or travelguard:public

![image-20201008-121338.png](/assets/image-20201008-121338.png)

**Restricting the number of offers displayed** The availability of services and products for a particular customer depends on the correlation of tags specified in the product tariff settings and in the contract with the customer. Consider the following case when two tags are used to label products: "public" for generally accessible products and "private" for products that should have limited access. The possible tag combinations are illustrated in the table below.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Contract tags     Product tariff tags   Display in search results
  ----------------- --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
  public            public                All results are displayed because the product and contract tags coincide completely.

  private           private               All results are displayed because the product and contract tags coincide completely.

  public            private               The results are not displayed because the product with this tag is not registered in the contract.

  private           private               The results are not displayed because the product with this tag is not registered in the contract.

  private, public   public                The results are displayed because the product with this tag is registered in the contract.

  private, public   private               The results are displayed because the product with this tag is registered in the contract.

  private, public   private, public       All results are displayed because the product and contract tags coincide completely.

  public            private, public       Only products with the \"public\" tag are displayed, because availability of the products with other tags (\"private\") is not registered in the contract.

  private           private, public       Only products with the \"private\" tag are displayed, because availability of the products with other tags (\"public\") is not registered in the contract.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Searching products with tags** As it was previously mentioned, the tags in the product tariff settings should coincide with the respective tags in the customer\'s contract. Some typical examples of sales regulations with the help of tagging are shown in the table below.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task                                                                                                                                                                    | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Results                                                                                                                                                                           |
+=========================================================================================================================================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+===================================================================================================================================================================================+
| Task 1 Create different tags for one and the same selfoperated product to restrict its availability for certain customers.                                              | 1.  Create your own hotel Hotel 2. Label it with the \"OwnHotel\" tag. 3. Create another hotel Hotel 4. Leave its tag field empty (the system automatically assigns the \"public\" tag to this hotel). 5. Open the Contract tab of Customer A and specify that products with the "OwnHotel" or "public" tags are available to the customer. 6. Do not add any extra tags to the contract of Customer B. By default all products tagged as "public" are available to this Customer. 7. Log into the system by using the log in and password of Customer A. Search for a hotel offer and check the results. 8. Log into the system by using the log in and password of Customer B. Search for a hotel offer and check the results. | - Search results for Customer A include both hotels: Hotel 1 and Hotel 2. \* Search results for Customer B include only Hotel 2.                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task 2 Create different tariffs for one and the same self-operated hotel so that you can sell the rooms at different rates to the local residents and foreign citizens. | 1.  Create a hotel and specify two tariffs for it: one for the local residents with the "Residents" tag, the other for the foreign citizens with the "Non-residents" tag. 2. Create a B2C-site and specify the "Residents" tag in the B2C contract settings. 3. Create another B2C-site and specify the "Non-residents" tag in the B2C contract settings. 4. Launch the first B2C-site, search for an offer and check the results. 5. Launch the second B2C-site, search for an offer and check the results.                                                                                                                                                                                                                     | - the first B2C-site should contain rates calculated by using the "Residents" tariff. \* The second B2C-site should contain rates calculated by using the "Non-residents" tariff. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task 3 Exclude certain regions from search for certain customers.                                                                                                       | 1.  Create your own hotel Hotel 1 and add the \"Berlin\" tag to it. 2. On the Contract tab of the Customer A, specify that the products with the "Berlin" tag are restr 3. Log into the system by using the log in and password of Customer A. Search for a hotel offer and check the results.icted for this customer.                                                                                                                                                                                                                                                                                                                                                                                                           | Hotel 1 is not be displayed in search results for Customer A.                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Here you can allow users to change their settings:

![image-20201008-121837.png](/assets/image-20201008-121837.png)

There is a possibility to set up service fee by category:

- By supplier
- By group of tags
- By product type
- By country

![image-20220218-063311.jpg](/assets/image-20220218-063311.jpg)

The following logic can be applied for Service fee calculation:

- As percentage %

![image-20220218-063446.png](/assets/image-20220218-063446.png)

- As fixed amount

![image-20220218-063527.png](/assets/image-20220218-063527.png)

Also there is an option of split payment: service fee can be paid separately for Immediate payment.

![image-20220218-063609.png](/assets/image-20220218-063609.png)

Service fee is the fee that to be collected by Tour Operator for provided service despite the final status of booking (Confirmed or Cancelled). This means service fee is a non-refundable amount (except reservations with status Rejected) and it is shown in cancellation charges and applied during cancellation

![image-20220218-063827.jpg](/assets/image-20220218-063827.jpg)
