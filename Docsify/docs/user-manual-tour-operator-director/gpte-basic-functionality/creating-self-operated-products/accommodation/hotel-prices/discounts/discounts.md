# Discounts

You can provide discounts and special offers for tourists booking your selfoperated services. A discount is a reductions to the basic prices of booked services.

With GP Travel Enterprise you can create and use the following types of discounts:

- Supplier discount: is offered by a service supplier. This discount is calculated from the net price.
- Tour operator discount: a discount that you provide to your clients. The discount is calculated from the gross price; the commission that you receive from the supplier is calculated from the net price of the service.

When creating a discount in GP Travel Enterprise, the following parameters are considered:

- The period when the discount is active
- Target audience (The number and type of tourists)
- Conditions and amount of the discount
- Calculation basis

**Creating New Discounts** To create a new discount,

1.  Open the profile of the required accommodation.
2.  On the **Prices** tab, **Discounts** sub-tab, click **Create**. *Discount creating* page appears:

![2024-11-16_12-03-54.jpg](/assets/2024-11-16_12-03-54.jpg)

![2024-11-16_12-04-04.jpg](/assets/2024-11-16_12-04-04.jpg)

1.  On the *Discount creating* page, locate mouse pointer into the **Name** box and type the name of the discount plan.
2.  Select the **visualization icon** to display on Search results page OR select *Don't show the discount to a customer* option.
3.  **Discount is equal to**: specify the amount of the discount. From the drop-down, select whether to calculate the discount in per cents or in currency units. Then locate mouse pointer into the box and type the value itself.
4.  In the **Discount period** group set the period when the discount is active: 1. specify the tariff to be applied; 2. specify **dates from ... to** for discount period; 3. choose one option from the list **Apply this discount**. *Optional: This discount is applied in accordance with the conditions configured in the \"Discounts\" section of this tariff; Always:***\*This is discount applies regardless of tariff;\* 4. choose the option from the list**Discount type\*\* who will be provided by. *Supplier\'s discount: A discount that is provided by a supplier and is calculated from the net price; Tour operator\'s discount: A discount that is provided by a tour operator and is calculated from the gross price. Tour operator\'s commission is calculated from the net price*
5.  **Terms of use**: specify the discount conditions.
6.  In the **Discount on** group specify if discount is applicable to each Membership level and Device type, is there is any Limits of citizenship.
7.  **Restrictions on tourists**: specify whether the discount is applied for all tourists or for particular tourist categories.
8.  Click **Save**.

**The following sections of Discount creating page are currently available via administration panel:**

- **Discount on** group: discount can be applicable for room type, guests type, allocation and meal types.
- **Discount conditions and calculation basis** group, set the terms and conditions upon which the discount is applied. You can select the following types: 1. Free nights (days): every night with a certain index number is offered at a lower price. For instance, if you set a 100% discount for every 7th night, then a tourist that books a room for the 7 days, only pays for 6 nights. 2. Discount for following nights (days): a discount for accommodation is applied after tourists stays for several nights at the hotel. For instance, a 10% discount is provided for every night after the 9th night. 3. Discount for the cheapest nights in the range (for hotels only): the discount on the room rate is calculated from the cost of the cheapest night in the period. For example, if a tourist books a room for 3 nights, and the first night costs 50 EUR, the second - 40 EUR, and the third - 30 EUR, then the price of the third night (30 EUR) is used for the calculation of the discount. The discount can be applied either once or for an unlimited number of times as a tourist complies with the requirements of the hotel staying.
- **Calculate discount from**group: for self-operated hotels specify the basis of the discount calculation. The discount can be calculated from the cost of: \* Accommodation + meals \* Accommodation only \* Meals only.

**Rules for discount Calculation** A discount amount for each travel service depends on the type of the discount (supplier's discount or tour operator's discount), by the terms specified when the discount is created, and also on method of calculation of the basic service price (type of a used price list).

Let's study the following examples of the discounts calculation rules.

The system does not check if the price-list types correspond to the discount calculation rules. When creating a discount, you can specify any possible rules for its calculation.

When using the Pensionate price list, meals are included in the accommodation price. In view of that, the discount, based on the \"Accommodation + meals\" calculation, is applied to the hotels with the Pensionate price-lists in most cases.

Assume that, you create an accommodation discount for the Early booking tariff, where the discount is not applicable to meals. Here the following conditions should be met:

- Tourist type: adult
- Room type: double, main bed (1 000 EUR)
- Board type (by default): RO (0 EUR)
- Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO

The accommodation discount for adults that book main bed in a double room - 20%. The discount calculation is based on accommodation price only. A tourist books main bed accommodation in a double room with breakfast. We need to calculate the amount of the discount.

  -------------------------------------------------------------------------------------------- -------------------------------
  The amount of accommodation discount:                                                        1 000 EUR \* 20% = 200 EUR

  The price of accommodation minus accommodation discount with the standard board type (RO):   1 000 EUR - 200 EUR = 800 EUR

  The price of accommodation minus accommodation discount but including breakfast price:       800 EUR + 300 EUR = 1 100 EUR
  -------------------------------------------------------------------------------------------- -------------------------------

Thus, if the RO board type was set by default, the system still views it as one of the board types that can also be used to calculate a discount.

Assume that we need to create an accommodation discount that does not include meals. Here the following conditions should be met:

- Tourist type: adult
- Room type: double, main bed accommodation, BB (1 300 EUR)
- Board type (optional): dinner (+ 300 EUR)
- Early booking tariff settings: always offer BB board type

The accommodation discount for adults booking main bed accommodation in a double room - 20%. The discount calculation is based on accommodation price only. A tourist books a double room with breakfast, main bed accommodation. We need to calculate the amount of the discount. In this case the correct calculation of the accommodation discount for the default board type (BB) is not possible, because in the Pensionate price-list meals are included in the room price. The discount is calculated according to the method described above in Example A

Assume that we need to create a board discount meeting the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): RO (0 EUR) Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO board type

The board discount for adults who book main bed accommodation in a double room - 20%. The discount is calculated on the basis of the price of the meals. A tourist books a double room with breakfast and main bed accommodation. We need to calculate the amount of the discount:

  ------------------------------------------- --------------------------------
  Board price:                                300 EUR

  The amount of the board discount:           300 EUR \* 20% = 60 EUR

  Accommodation price minus board discount:   1 300 EUR - 60 EUR = 1 240 EUR
  ------------------------------------------- --------------------------------

Assume that we need to create an accommodation discount that is based on the accommodation price as well as on the board price and should meet the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): RO (0 EUR)
- Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO board type

The board and accommodation discount for adults who books main bed accommodation in a double room - 20%. The discount is calculated on the basis of the prices of meals and accommodation put together. A tourist books a double room with breakfast and main bed accommodation. We need to calculate the amount of the discount.

  ----------------------------------------------------------------- ---------------------------------
  Board and accommodation price:                                    1 000 EUR + 300 EUR = 1 300 EUR

  The amount of the board and accommodation discount:               1300 EUR \* 20% = 260 EUR

  The accommodation price minus board and accommodation discount:   1 300 EUR - 260 EUR = 1 040 EUR
  ----------------------------------------------------------------- ---------------------------------

**Calculating discounts for the Pensionate price-list** When using the Pensionate price list, meals are included in the accommodation price. In view of that, the discount, based on the \"Accommodation + meals\" calculation, is applied to the hotels with the Pensionate price-lists in most cases.

Assume that, you create an accommodation discount for the Early booking tariff, where the discount is not applicable to meals. Here the following conditions should be met:

- Tourist type: adult
- Room type: double, main bed (1 000 EUR)
- Board type (by default): RO (0 EUR)
- Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO

The accommodation discount for adults that book main bed in a double room - 20%. The discount calculation is based on accommodation price only. A tourist books main bed accommodation in a double room with breakfast.

We need to calculate the amount of the discount.

  -------------------------------------------------------------------------------------------- -------------------------------
  The amount of accommodation discount:                                                        1 000 EUR \* 20% = 200 EUR

  The price of accommodation minus accommodation discount with the standard board type (RO):   1 000 EUR - 200 EUR = 800 EUR

  The price of accommodation minus accommodation discount but including breakfast price:       800 EUR + 300 EUR = 1 100 EUR
  -------------------------------------------------------------------------------------------- -------------------------------

Thus, if the RO board type was set by default, the system still views it as one of the board types that can also be used to calculate a discount.

Assume that we need to create an accommodation discount that does not include meals. Here the following conditions should be met:

- Tourist type: adult
- Room type: double, main bed accommodation, BB (1 300 EUR)
- Board type (optional): dinner (+ 300 EUR)
- Early booking tariff settings: always offer BB board type

The accommodation discount for adults booking main bed accommodation in a double room - 20%. The discount calculation is based on accommodation price only. A tourist books a double room with breakfast, main bed accommodation. We need to calculate the amount of the discount. In this case the correct calculation of the accommodation discount for the default board type (BB) is not possible, because in the Pensionate price-list meals are included in the room price. The discount is calculated according to the method described above in Example A.

Assume that we need to create a board discount meeting the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): RO (0 EUR)
- Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO board type

The board discount for adults who book main bed accommodation in a double room - 20%. The discount is calculated on the basis of the price of the meals. A tourist books a double room with breakfast and main bed accommodation.

We need to calculate the amount of the discount:

  ------------------------------------------- --------------------------------
  Board price:                                300 EUR

  The amount of the board discount:           300 EUR \* 20% = 60 EUR

  Accommodation price minus board discount:   1 300 EUR - 60 EUR = 1 240 EUR
  ------------------------------------------- --------------------------------

Assume that we need to create an accommodation discount that is based on the accommodation price as well as on the board price and should meet the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): RO (0 EUR)
- Board type (optional): BB (+ 300 EUR)
- Early booking tariff settings: do not offer RO board type

The board and accommodation discount for adults who books main bed accommodation in a double room - 20%. The discount is calculated on the basis of the prices of meals and accommodation put together. A tourist books a double room with breakfast and main bed accommodation.

We need to calculate the amount of the discount.

  ----------------------------------------------------------------- ---------------------------------
  Board and accommodation price:                                    1 000 EUR + 300 EUR = 1 300 EUR

  The amount of the board and accommodation discount:               1300 EUR \* 20% = 260 EUR

  The accommodation price minus board and accommodation discount:   1 300 EUR - 260 EUR = 1 040 EUR
  ----------------------------------------------------------------- ---------------------------------

**Calculating discounts for the Hotel price-list** In the Hotel price-list the board and accommodation prices are set separately.

Assume that we need to create an accommodation discount for the Early booking tariff. It is based on the accommodation price only and should meet the following conditions: Tourist type: adult Room type: double, main bed accommodation (1 000 EUR) Board type (by default): BB (300 EUR) Early booking tariff settings: do not offer RO board type

The accommodation discount for adults who book main bed accommodation in a double room - 10%. The discount is calculated on the basis of the accommodation price. A tourist booked a double room with breakfast, main bed accommodation.

We need to calculate the amount of the discount.

  -------------------------------------------------------------------------------- --------------------------------------------
  The amount of the accommodation discount:                                        1 000 EUR \* 10% = 100 EUR

  The accommodation price minus the accommodation discount plus breakfast price:   1 000 EUR -- 100 EUR + 300 EUR = 1 200 EUR
  -------------------------------------------------------------------------------- --------------------------------------------

Assume that we need to create a board discount, that should meet the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): BB (300 EUR)
- Early booking tariff settings: always offer BB board type

The board discount for adults who book main bed accommodation in a double room - 10%. The discount is calculated on the basis of the board price. A tourist books a double room with breakfast and main bed accommodation.

We need to calculate the amount of the discount:

  --------------------------------------- ------------------------------------------
  Board price:                            300 EUR

  Board discount amount:                  300 EUR \* 10% = 30 EUR

  Accommodation price minus board type:   1 000 EUR + 300 EUR - 30 EUR = 1 270 EUR
  --------------------------------------- ------------------------------------------

Assume that we need to create an accommodation discount that is based on the accommodation price as well as on the board price and should meet the following conditions:

- Tourist type: adult
- Room type: double, main bed accommodation (1 000 EUR)
- Board type (by default): BB (300 EUR)
- Early booking tariff settings: always offer BB board type

The board and accommodation discount for adults who book main bed accommodation in a double room - 20%. The discount is calculated on the basis of the prices of board and accommodation put together. A tourist books a double room with breakfast and main bed accommodation.

We need to calculate the amount of the discount:

Board and accommodation price: 1 000 EUR + 300 EUR = 1 300 EUR The amount of the board and accommodation discount: 1300 EUR \* 20% = 260 EUR The accommodation price minus accommodation and board discount: 1 300 EUR - 260 EUR = 1 040 EUR

  ----------------------------------------------------------------- ---------------------------------
  Board and accommodation price:                                    1 000 EUR + 300 EUR = 1 300 EUR

  The amount of the board and accommodation discount:               1300 EUR \* 20% = 260 EUR

  The accommodation price minus accommodation and board discount:   1 300 EUR - 260 EUR = 1 040 EUR
  ----------------------------------------------------------------- ---------------------------------

**Calculating supplier's discount** Assume that the supplier offers a double room with a 10 per cent discount - at the price of 1 000 EUR. The commission of the tour operator is 20%.

We should calculate the room price for the tourists and the amount to be paid to the supplier.

  --------------------------------------------------------------------------- ------------------------------
  Room price for a tourist (amount that a tourist pays to a tour operator):   1 000 EUR -- 10% = 900 EUR

  Amount to be paid to a supplier:                                            900 EUR -- 20% = 720 EUR

  The tour operator's revenue:                                                900 EUR -- 720 EUR = 180 EUR
  --------------------------------------------------------------------------- ------------------------------

**Calculating tour operator's discount** Assume that the supplier offers a double room at 1 000 EUR with no discounts, but the tour operator provides a tourist with a 25% discount at his own expense. The tour operator's commission here is 20%.

We need to estimate the room price for a tourist and the amount due to be paid to the supplier.

  --------------------------------------------------------------------------------- --------------------------------
  Room price for the tourist (amount that the tourist pays to the tour operator):   1 000 EUR -- 25% = 750 EUR

  The amount due to be paid to the supplier:                                        1 000 EUR -- 20% = 800 EUR

  Expenses of the tour operator:                                                    750 EUR -- 800 EUR = -- 50 EUR
  --------------------------------------------------------------------------------- --------------------------------

As we see, such a great discount costs only 50 EUR to the tour operator.

If two discounts (the tour operator's discount and supplier's one) are added to the tariff, and the Apply first discount that was found rule is enabled, then the calculation is based on the first discount found according to one of the schemes described above.

If the Apply all discounts rule is enabled when the discounts are added to the tariff, the final price of the service is calculated according to the following scheme:

- Supplier's price for a double room: 1 000 EUR
- Supplier's discount for a double room: 10%
- Commission to the tour operator: 20%
- Tour operator's discount for a double room: 25%

Discount calculation:

  --------------------------------------------------------------------------------- -----------------------------------
  Room price for the tourist (amount that the tourist pays to the tour operator):   1 000 EUR -- 10% -- 25% = 675 EUR

  Amount due to the supplier:                                                       1 000 EUR -- 10% -- 20% = 720 EUR

  Expenses of the tour operator:                                                    675 EUR -- 720 EUR = -- 45 EUR
  --------------------------------------------------------------------------------- -----------------------------------
