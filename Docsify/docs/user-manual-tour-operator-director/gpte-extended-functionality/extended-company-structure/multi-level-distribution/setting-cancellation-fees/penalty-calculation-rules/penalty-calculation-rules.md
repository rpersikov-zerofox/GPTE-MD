# Penalty calculation rules

**This functionality is currently available via administration panel.**

Supposing a travel agency books a hotel room from your company for June 1-5, 2022. The total room rate from the supplier is 200 EUR and the markup is 20%, thus the service is sold to the travel agency for 240 EUR (which makes EUR 60 per night). The initial cancellation terms set by the supplier include penalty charges of 50 per cent of the total service rate if the booking is canceled seven or fewer days before the service start date.

**Case 1.**

## **Cancellation terms are not specified in the contract**

If you specify no values either for independent cancellation terms or for supplier penalty charges, the initial cancellation terms set by the supplier are applied.

![image-20200922-111824.jpg](/assets/image-20200922-111824.jpg)

In our case this means that the penalty charges are applied on May 25, 2022. If the travel agency cancels the reservation within the period from May 25-31, it pays you 120 EUR of penalty charge (50% of the supplier rate including the markup 240 EUR). In your turn, you pay 100 EUR to your supplier (50% of the supplier rate). 20 EUR difference is your company profit.

**Case 2.**

## Cancellation terms are specified for supplier penalty charges only

If you enter no values for independent cancellation terms, but set up the shift of deadlines and increase of the initial supplier penalty charge, then the supplier penalty charges are applied in accordance to your settings.

![image-20200922-112003.jpg](/assets/image-20200922-112003.jpg)

Thus, if you set the shift of the cancellation deadline for 3 days and set the increase of the penalty charge to 10 per cent, then the penalty period will be extended to 10 days:

- Cancellation period = 7 days according to supplier's terms + 3 days according to your terms.

The penalty period starts on May 22, that is 3 days before the supplier\'s cancellation terms start. At the same time the amount of penalty charge additionally increases by 10 per cent of the initial supplier penalty charge including the markup of the tour operator. In this case if a reservation is canceled within the period from May 22 to May 31, the travel agency pays the penalty charge of 132 EUR.

- 120 EUR (50% of the initial supplier\'s penalty charge including the tour operator\'s markup) + 10% (penalty increase) = 132 EUR Penalty charge

You pay 100 EUR to the supplier. The remaining amount of 32 EUR is your company profit. Similarly you can configure supplier\'s penalty terms by changing only the deadline shifts or the penalty charge increase.

**Case 3.**

## Only independent (your own) cancellation terms are set up.

If you set up only your custom cancellation terms and they overlap with the initial penalty charge terms set by a supplier for some dates, stricter penalty rules are applied for these dates.

**Example А.**

Assume that you set up a 100 per cent penalty charge if the service is canceled five days before it is rendered.

![image-20200922-112259.jpg](/assets/image-20200922-112259.jpg)

In this case:

- If the service is canceled during the period from May 25 to May 26, the travel agency pays you the penalty charge of 120 EUR (according to the supplier cancellation terms).
- If the service is canceled during the period from May 27 to May 31, the travel agency pays you the penalty fees of 240 EUR (according to your independent cancellation terms, because they are stricter than those applied by the supplier).

**Example B.**

Suppose you set stricter conditions, according to which the cancellation of the service 10 days before it is rendered results in 100% penalty charge.

![image-20200922-112403.jpg](/assets/image-20200922-112403.jpg)

In this case if the service is canceled during the period from May 22 to May 31, the travel agency pays you a penalty charge of 240 EUR (your independent cancellation conditions are applied since they are stricter than those of the supplier throughout the whole penalty period).

You can configure the calculation of penalty charge by using the percentage of the *total price* of the service as well as that of the\* first night\*.

**Example C.**

Suppose you set up a rule according to which a penalty charge of 100% of the price of the first night is charged if the service is canceled five days before it is rendered.

![image-20200922-112601.jpg](/assets/image-20200922-112601.jpg)

In this case:

- If the service is canceled during the period from May 25 to May 26, the travel agency pays you 120 EUR of penalty fees (according to the supplier cancellation terms).
- If the service is canceled during the period from May 27 to May 31, the travel agency pays you the same 120 EUR of penalty fees, since the supplier cancellation fees are stricter than yours.

**Example D.**

Suppose you set up a condition according to which the penalty of 100% of the price of the first night is charged if the service is canceled 10 days before it is rendered.

![image-20200922-112702.jpg](/assets/image-20200922-112702.jpg)

In this case:

- If the service is canceled during the period from May 22 to May 24, the travel agency pays you 60 EUR penalty fees (according to your own terms, since the terms of the supplier are not yet active).
- If the service is canceled during the period from May 25 to May 31, the travel agency pays you 120 EUR penalty charge (the supplier cancellation are applied since they are stricter than yours).

**Case 4.**

## All possible cancellation terms are set up

You can set up custom cancellation conditions and change the cancellation conditions of the supplier at the same time. In this case stricter penalty conditions are used to determine the amount of charge and the deadline.

**Example A.**

Suppose you set up a rule, according to which a penalty of 100% of the total service price is applied if the the service is canceled five days before it is rendered. Additionally you shift the supplier's penalty deadline by 3 days and increase the penalty charge by 25%.

![image-20200922-112830.jpg](/assets/image-20200922-112830.jpg)

In this case the shifted penalty deadline attaches from May 22 and if the service is canceled during the period from May 22 to May 26, the travel agency pays you 150 EUR of penalty charge (0,5\*240+25%). Your custom penalty charges take effect starting from May 27 and since it is stricter than that of the supplier, if the service is canceled within the period from from May 27 to May 31, the travel agency pays you 240 EUR.

**Example B.**

Suppose you set up a condition, according to which the cancellation that occurs five days before the service is rendered results in 100% penalty fee of the first night. Additionally you shift the supplier's penalty deadline by 3 days and increase the penalty charge by 25%.

![image-20200922-113050.jpg](/assets/image-20200922-113050.jpg)

In this case the shifted supplier\'s penalty charges take effect from May 22 and if the service is canceled within the period from May 22 to May 26, the travel agency pays 150 EUR (0,5\*240 +25%) to you. You custom cancellation terms take effect starting from May 27 (that include the penalty charge of 60 EUR payable by the travel agency), but since your conditions are less strict than those of the supplier (150 EUR), if the service is canceled within the period from May 27 to May 31, the conditions of the supplier are still active and the travel agency pays 150 EUR to you.
