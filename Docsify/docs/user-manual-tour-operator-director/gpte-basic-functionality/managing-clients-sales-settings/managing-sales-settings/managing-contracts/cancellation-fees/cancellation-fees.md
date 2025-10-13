# Cancellation Fees

**This functionality is currently available via administration panel.**

With the cancellation fees configuration, you can add additional logic to the terms and conditions for canceling services that are being automatically received from suppliers.

- Independent (own) cancellation policies: In this group, specify the duration of the penalty period, the per cent rate of the cancellation fee, and the price from which the cancellation fee is calculated (usually total cost; for hotels the one night option is available). Also please pay attention that if you set this option the system will choose the most strict cancellation rules - either supplier\'s cancellation rules or your own cancellation rules.

Supposing a travel agency books a hotel room from your company for June 1-5, 2022. The total room rate from the supplier is 200 EUR and the markup is 20%, thus the service is sold to the travel agency for 240 EUR (which makes EUR 60 per night). The initial cancellation terms set by the supplier include penalty charges of 50 per cent of the total service rate if the booking is canceled seven or fewer days before the service start date. Assume that you set up a 100 per cent penalty charge if the service is canceled five days before it is rendered. In this case:

- If the service is canceled during the period from May 25 to May 26, the travel agency pays you the penalty charge of 120 EUR (according to the supplier cancellation terms).
- If the service is canceled during the period from May 27 to May 31, the travel agency pays you the penalty fees of 240 EUR (according to your independent cancellation terms, because they are stricter than those applied by the supplier).

![image-20201005-194406.jpg](/assets/image-20201005-194406.jpg)

- **Management of supplier cancellation policies:** In this group, specify the shift of deadline and the value by which the cancellation fee increases. For example, If you enter no values for independent cancellation terms, but set up the shift of deadlines and increase of the initial supplier penalty charge, then the supplier penalty charges are applied in accordance to your settings.

![image-20201005-194442.jpg](/assets/image-20201005-194442.jpg)

Thus, if you set the shift of the cancellation deadline for 3 days and set the increase of the penalty charge to 10 per cent, then the penalty period will be extended to 10 days: **cancellation period = 7 days according to supplier's terms + 3 days according to your terms.**

The penalty period starts on May 22, that is 3 days before the supplier\'s cancellation terms start. At the same time the amount of penalty charge additionally increases by 10 per cent of the initial supplier penalty charge including the markup of the tour operator.

In this case if a reservation is canceled within the period from May 22 to May 31, the travel agency pays the penalty charge of 132 EUR. **120 EUR (50% of the initial supplier\'s penalty charge including the tour operator\'s markup) + 10% (penalty increase) = 132 EUR Penalty charge**

You pay 100 EUR to the supplier. The remaining amount of 32 EUR is your company profit. Similarly you can configure supplier\'s penalty terms by changing only the deadline shifts or the penalty charge increase.

![image-20201005-194607.jpg](/assets/image-20201005-194607.jpg)

To set these cancellation fees,

1.  Go to the contract, tab **Cancellation fees**.
2.  Click **Edit** to switch to editing mode.
3.  Specify the required data - the cancellation period, the cancellation fee, and set the increase of fees.
4.  Click **Save**.
