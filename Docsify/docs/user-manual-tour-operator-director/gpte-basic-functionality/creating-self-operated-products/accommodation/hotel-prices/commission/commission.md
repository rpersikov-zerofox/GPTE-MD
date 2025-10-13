# Commission

When you sign contract with suppliers, you can agree on getting commission from them. In this case you sell offers at the supplier\'s price and get commission for this.

![2024-11-16_13-10-01.jpg](/assets/2024-11-16_13-10-01.jpg)

As soon as different commissions can be applied depending on the reservation time (for example, during high and low season), allocation (main bed or extra bed), meal type, extra services, etc. - you can create several commission plans and then apply them to the required tariffs.

- validity period (usually divided into high / low season and coincides with the validity period of the tariff and price list)
- commissions for accommodation (main bed, extrabed, sharing)
- meal commissions
- additional services
- service commissions

**Creating Commission** To create a commission plan:

1.  Navigate to **Products** menu - **Hotels** tab and select the required hotel.
2.  Go to the **Prices** tab - **Commission** sub-tab.
3.  Click **Create**. The following window appeared:

![2024-11-16_13-10-11.jpg](/assets/2024-11-16_13-10-11.jpg)

![image-20200928-104858.jpg](/assets/image-20200928-104858.jpg)

4.  Specify the **name** of a commission plan, tariff and availability period when it can be applied (**Commissions are active during** section).
5.  **Description**: enter the commission plan description.
6.  Specify amount and terms of the commission: 1. **Currency for commission calculation** - is the currency in which the commission is set. By default the base currency of the hotel is used. But you can change it to any other value. 2. **Commission per tourist**: specify value for commission per tourist. 3. **Commission applied for the following room types:** specify the room types for which the commission is applied. 4. Additionally you can specify **commission for extra service** - this is one time amount that a tour operator gets for the whole booking, is the commission value for all additional services that can be booked within the hotel. 1. Base commission - is used by default for all new additional services. In this case after you create a new extra service, the system displays a warning message about adding it to the base commission. 2. If you want to specify different commissions for different additional services, enter the required value manually into the corresponding fields. If the commission is not paid for some service, leave zero (0 in the corresponding cell). 5. **Commission per**(**This section is currently available via administration panel.**): 1. accommodation - specify different commissions for allocation and meal; 2. service - specify single commission for the whole service including both allocation and meal. After you select the required option, you can specify different commission values for Main Bed, Extrabed and Sharing bed.
7.  Click **Save**.

**Conditional Commissions for Hotels** --- is an alternative way of tracking commissions being obtained from suppliers for selfoperated products. To the contrary of regular commissions that can be specified as a part of tariffs and are calculated for every reservation, the conditional commissions depend on turnovers -- the more you sell, the higher commission you get.

**This functionality is currently available via administration panel.**

**To create Conditional commissions,**

1.  Open the profile of the required self-operated product.
2.  On the **Information** tab, in the **Conditional commissions** group, click **Create**. The New conditional commissions window appears:

![image-20201002-101658.png](/assets/image-20201002-101658.png)

3.  In the New conditional commissions window, specify the following information: 1. **Name:** locate mouse pointer into the box and type the name of the commission. 2. **Commission amount:** specify the amount of the commission. 3. **The commission is active:** specify the active period of conditional commission. 4. **Description:** locate mouse pointer into the text field and describe the category you are creating.
4.  Click **Save** and **Close**.

**Calculating Commission** When the order price is calculated, all commissions sums for all offer are summed up.

The price for a SNGL room with an extra bed for 2 adults is calculated in the following way:

Price and commission:

![image-20201002-103641.png](/assets/image-20201002-103641.png)

In this case:

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
  The total price of all booked services is:                  500 EUR + 200 EUR + 10 EUR = 710 EUR

  The price to be paid by a tour operator to a supplier is:   (500 EUR --10%) + (200 EUR -- 5%) + (10 EUR -- 0%) -- 10 EUR = = 450 EUR + 190 EUR + 10 EUR -- 10 EUR = 640 EUR

  The tour operator gets the following commission:            710 EUR -- 640 EUR = 70 EUR
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------

Let's consider the same example but in this case the meal is charged separately.

Price and commission

![image-20201002-104151.png](/assets/image-20201002-104151.png)

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  The price to be paid by a tour operator to a supplier is:   (500 EUR --10%) + (200 EUR -- 5%) + 100\*2 + (10 EUR -- 10%) -- 10 EUR= = 450 EUR + 190 EUR + 200 EUR + 9 EUR -- 10 EUR = 839 EUR

  The total price of all booked services is:                  500 EUR + 200 EUR + 200 EUR + 10 EUR = 910 EUR

  The tour operator gets the following commission:            910 EUR -- 839 EUR = 71 EUR
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
