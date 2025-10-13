# Price Lists of Hotels

In order to specify the rates for accommodation, you should create a pricelist.

To create a price-list,

1.  Go to **Products** and click **Hotels**.
2.  In the list of created self-operated accommodations, click the required one.
3.  On the Prices tab, click **Price-lists**, and then click **Create.**

:::: note
::: title
Note
:::

Missing image: d7a80f8f-fbd8-4c2d-a331-237e2cf739cb (dimensions: 1008x756) *Check the attachments folder for available images and update the mapping.*
::::

4.  While creating price-lists for accommodation, the first step is to select a price-list type.
5.  There are the following price-list types to choose from: 1. **\*Original**\*\* \*\*\*\*(price per pax, board type inclusive)\*\*\*\*: *prices are calculated for an adult tourist, the board type is already included in the allocation price. Prices for allocating different tourist types on extra places are calculated from the price per an adult with the same board type and accommodation. 2.Pensionate (price per pax, board type inclusive): prices are set per tourist, the board type is already included. Prices for allocating different tourist types on extra places are calculated from the price per the same board type for an adult on the main place. 3.Pensionate*\* **(price per room, board type inclusive)**: prices are set per room independently from the number of tourists, the board type is already included. Allocation prices for different board types are calculated from the prices per basic board type of the room. 4. **Hotel** **(price per room, extra charge for board type)**: prices are set per room independently from the number of tourists. Boarding prices are set separately from allocation prices. 5. **Hotel (price per pax, extra charge for board type)**: prices for different board types are calculated per tourist and are set separately from the accommodation price. Allocation prices for different tourist types on extra places are calculated from prices per an adult on the main place. 6. **Hotel (price per room with multiple occupancy)**: prices are set for rooms with multiple occupancy and for extra person on extra bed separately from the accommodation prices with default board type. 7. **Hotel (package price per room with multiple occupancy)**. 8. **Hotel (price per room per allocation; extra charge for board types):**it is useful for the situation when hotel provides so sophisticated price list which cannot be specified as "price per pax" or "price per room", but instead gives all possible combinations of guests and prices for them.
6.  Click the required price-list type and click **Continue**. Price-list page appears:

:::: note
::: title
Note
:::

Missing image: cd0eb52c-2f2c-4458-8cc7-ab8814523cdb (dimensions: 1373x511) *Check the attachments folder for available images and update the mapping.*
::::

:::: note
::: title
Note
:::

Missing image: 3e3be024-d322-4f77-81c5-d4f84e65664b (dimensions: 1350x593) *Check the attachments folder for available images and update the mapping.* On the Price-list page, the information to be specified is arranged in two sections: 1. General Information; 2. Prices.
::::

To proceed with a price-list creation,

1.  In the General information section, specify the following information: \* **Name**: locate mouse pointer into the box and type the name of the price list. \* **Price list is active during**: fill in the required information in the table. Specifically, \* From the **Tariff** drop-down, select the tariff to connect the price-list to. In case you did not create any tariffs and decided to start with creating other constituent, select the default Standard item. \* In the **Date from\... to\...** group specify the period of the price-list validity. \* In the **Days of the week** group, select the days on which the price-list will be applied. For example, you can create different price-lists for week days and week-ends. \* To create a copy of the period, click **Copy**. The identical table line will be created. It may particularly useful in case you create several price-lists with minor differences. It is easier to copy an existing price-list period and make some corrections. \* **Description**: locate mouse pointer onto the text field and enter the price-list description.

If you want to use different rates for work days and week-ends during one season (for example, from September 1 to December 31, 2025) you should create two price-lists with the same duration terms but configured for different days of the week.

1.  In the first price-list (for week days) you should select days from Monday to Friday and select week-ends only in the second one:

:::: note
::: title
Note
:::

Missing image: 7c039d03-efa0-431b-ad74-b3be13deb4a0 (dimensions: 1028x358) *Check the attachments folder for available images and update the mapping.*
::::

2.  In the **Prices** section, specify the prices for services:

:::: note
::: title
Note
:::

Missing image: e32cd398-5c19-475f-8398-241dd29cb887 (dimensions: 1345x282) *Check the attachments folder for available images and update the mapping.*
::::

**The following functionality (mathematical functions for prices calculation) is currently available via administration panel.**

While adding prices, you can use fixed rates or mathematical functions. In the former case, the cell that is basic for further calculations, is highlighted in gray. When applying functions the basic rules are as follows:

- Every new room type is considered a basic cell. The basic sell is the sell used for further calculation.

:::: note
::: title
Note
:::

Missing image: 6215d4c5-35cd-4acc-b67b-f104f77b0f9a (dimensions: 812x500) *Check the attachments folder for available images and update the mapping.*
::::

- The price of every further board type withing the current room type is calculation the base of the default board type in the group:

:::: note
::: title
Note
:::

Missing image: 5c914507-3175-4c11-985b-b928505d8271 (dimensions: 812x166) *Check the attachments folder for available images and update the mapping.*
::::

- The price for children, seniors or any other tourist categories, except from the default one (usually, adult) is calculated form the price for an adult for the same room and board type

:::: note
::: title
Note
:::

Missing image: c338a533-6d01-4bc4-b043-b72fd193e3da (dimensions: 808x64) *Check the attachments folder for available images and update the mapping.*
::::

- The price for extra bed both for default and additional tourist categories is calculated from the price of the room type the extra bed belongs in compliance with the board type of the room:

:::: note
::: title
Note
:::

Missing image: 5b342f80-bdec-42aa-8ce7-ee829caf9e9b (dimensions: 818x412) *Check the attachments folder for available images and update the mapping.*
::::

- Please pay attention that in case you enter the wrong data format, for example, a per cent figure into the basic cell, the system will show \"error\" displayed in the rate area.

:::: note
::: title
Note
:::

Missing image: 1d3ab31f-4ea9-4dc1-8c42-bd9e30c655d2 (dimensions: 612x68) *Check the attachments folder for available images and update the mapping.*
::::

When configuring **Original**and **Pensionate (price per pax)** price-lists, the price per room is set for every tourist separately. A cell with a rate for an adult on a main bed is used to calculate accommodation price for a particular room. The rates for other types of tourists, room types and board types are calculated in compliance with the above mentioned rules.

When creating Original or Pansionate price-lists, you need to fill in the rates for every existing room and board type for every tourists category. Locate mouse pointer into the corresponding boxes and type the rate to apply for the calculation for a certain room/board/tourist type.

:::: note
::: title
Note
:::

Missing image: e32cd398-5c19-475f-8398-241dd29cb887 (dimensions: 1345x184)

*Check the attachments folder for available images and update the mapping.*
::::

With the **Pensionate (price per room**) price-list you can set one accommodation price irrespective of tourist categories and the number of guests. In such a price-list you can set accommodation prices for every room type. The price for allocation with the basic board type already includes the board type cost. If the hotel provides tourists with additional board types (for example, half board) the accommodation price is displayed separately. When calculating the cost of extra meals that are not included in the accommodation rate, the cell with the extra meal rate for an adult with a standard bed accommodation is used as a basis.

Locate mouse pointer into the respective box and type the rates for a certain room type.

:::: note
::: title
Note
:::

Missing image: f7c23c4e-97a0-4275-99cd-f7912c7fdcbb (dimensions: 428x186)

*Check the attachments folder for available images and update the mapping.*
::::

For the hotel price-list (price per room) you can specify common prices for every room type irrespective of the tourist categories. The board type price is specified separately. The calculation of board rates for different tourist categories is based on the standard board rates for an adult. In the Prices section, fill in the data in the Base allocation prices group.

Locate mouse pointer into the respective box and type the rates for a certain room type.

:::: note
::: title
Note
:::

Missing image: 71f6d8a0-7080-4d5b-9e66-49f07bdfc093 (dimensions: 475x476)

*Check the attachments folder for available images and update the mapping.*
::::

Then, click the Extra charge for board type bar to specify the extra charges for board type. In the Extra charge for board type group, enter the rates for board types for every tourist category. To apply the entered figure to all the board types for a certain tourist category, click the downward arrow symbol. The data entered into the basic cell will be transferred to all other meal types within a certain tourist category.

:::: note
::: title
Note
:::

Missing image: 4611ef7a-4a2e-46f5-9c8f-3218615e2585 (dimensions: 812x189)

*Check the attachments folder for available images and update the mapping.*
::::

For this price-list, the hotel rates for extra meals are the same for all room types and are specified separately from the basic accommodation rates. In this case the calculation of the accommodation rates for different tourist categories and rates for extra bed accommodation is based on the rates for main accommodation of an adult in the room. The calculation of board rates for different tourist categories and for extra bed accommodation is based on the standard board rates for an adult.

In the Prices section, fill in the data in the Base allocation prices group. Locate mouse pointer into the respective boxes and type the rates for room types for every tourist category.

:::: note
::: title
Note
:::

Missing image: fc89b09b-9dd0-40a8-a371-10750a2714e6 (dimensions: 826x182)

*Check the attachments folder for available images and update the mapping.*
::::

Then, click the Extra charge for board type bar to specify the extra charges for board type. In the Extra charge for board type group, enter the rates for board types for every tourist category.

:::: note
::: title
Note
:::

Missing image: bade3c47-cb44-4d2b-8a52-b62f591a21e6 (dimensions: 804x190)

*Check the attachments folder for available images and update the mapping.*
::::

To apply the entered figure to all the room/board types for a certain tourist category, click the downward arrow symbol. The data entered into the basic cell will be transferred to all other board/meal types within a certain tourist category.

After the price-list is set, click **Save**. The price-list is added to the directory and can be used for making up a tariff.

With GP Travel Enterprise you can calculate the total price of accommodation in two different ways depending on the accommodation unit:

- for the whole period of stay by the price of each night: the accommodation price for the whole period of stay includes the price of every single night.
- for the whole period of stay by the price of the first night: the accommodation price for the whole period of stay consists of the price of the first night multiplied by the number of booked nights.

Let's examine the difference between two pricing approaches on the following example:

For example a tourist books a single room for the period from April 1 to 5. The price of every single night here is:

:::: note
::: title
Note
:::

Missing image: c34c29b4-6ef5-48b4-9531-5de3858e6397 (dimensions: 726x103)

*Check the attachments folder for available images and update the mapping.*
::::

When the total accommodation price is calculated by addition of all nights, the total accommodation price for a tourist is calculated by addition of the prices of every night: 200 EUR + 120 EUR + 120 EUR + 120 EUR + 120 EUR = 680 EUR

If the total accommodation price is calculated by the price of the first night, the total accommodation price for a tourist is calculated by the price of the first night multiplied by the number of nights of stay: 200 EUR \* 5 nights = 1000 EUR

The price calculated on this stage is displayed to a tourist on the hotel search results page. Let's examine the way each pricing method works.

**Accommodation rates displayed in the hotel search results** On the hotel search results, a tourist can see the price that is calculated according to the pricing method that you specify in the tariff.

- If the price calculation is based on the sum of the prices for every night, the offer price is EUR 680.
- If the price calculation is based on the price of the first night, the accommodation price for a tourist is EUR 1 000.

There also exists a possibility to set daily rates for self-operated hotels. The functionality is particularly suitable for those who offer their clients the rooms, prices of which change within the daytime. It can significantly broaden the range of the offers.

**This functionality is currently available via administration panel.**

To configure calculation of the total price according to the price of every night, you should specify this condition in the tariff settings.

1.  In the Price-lists section, select By each night.

:::: note
::: title
Note
:::

Missing image: 886f701a-9736-4d94-b46c-6b7d44faa04e (dimensions: 521x244) *Check the attachments folder for available images and update the mapping.* Add the required price-list (or several price-lists) to the tariff.
::::

2.  Click Save.

**This functionality is currently available via administration panel.**

1.  In the Price-lists section, select By first night.

:::: note
::: title
Note
:::

Missing image: 7250ca24-55f6-4a65-9961-7e716df9da8e (dimensions: 715x185) *Check the attachments folder for available images and update the mapping.*
::::

2.  Add the required price-list (or several price-lists) to the tariff.
3.  Click Save.

## Upload prices from XLSX

**This functionality is currently available via administration panel.**

It is possible to upload prices from XLSX for Own Hotels. This way can be applied to type of the price-list "pensionate, per room" only.

XLSX file must be consist of basic information:

● tariff name

● periods

● room types

● meal types

:::: note
::: title
Note
:::

Missing image: aff6eeb7-b98a-4fa4-a474-fb2f6c40039f (dimensions: 1016x480)

*Check the attachments folder for available images and update the mapping.*
::::
