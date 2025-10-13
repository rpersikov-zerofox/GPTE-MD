# Setting Cancellation fees

**This functionality is currently available via administration panel.**

With the cancellation fees configuration, you can specify the terms and conditions for canceling services booked by agencies/distributors. You can set your own cancellation conditions and adjust the cancellation conditions of suppliers:

- **Independent (own) cancellation policies:** In the group, specify the duration of the penalty period, the per cent rate of the cancellation fee, and the price from which the cancellation fee is calculated (usually total cost; for hotels the one night option is available).
- **Management of supplier cancellation policies:** In the group, specify the shift of deadline and the value by which the cancellation fee increases.

![image-20200925-070853.jpg](/assets/image-20200925-070853.jpg)

The **duration** of the penalty period is specified in the number of days before the date when the service is rendered or the product is used. In GP Travel Enterprise system, the penalty period start date sets by supplier shifts for one day automatically. This shift helps tour operators and their partners avoid penalty charges caused by time lag.

**For example**, a supplier specifies that penalty charges are imposed if a reservation is canceled starting December 12, 2025 after 12:00. The penalty charges come to power on the previous day, that is December 11, 2025 in GP Travel Enterprise system.

Assume that the supplier's time zone is GTM+4 and the Tour operator's time zone is GTM+1. In this case, if the Tour Operator cancels the booking at 11:00 local time (an hour before the penalty charges are imposed), it's already 14:00 in the supplier's time zone, and for the supplier the penalty period has already started, so the supplier can demand penalty charges. To avoid this, a 24-hour shift is used.

- The agency\'s penalty charge is set in percent from the full price of a product or service or the price of the product for the first night, including the tour operator's markup.
- To configure the deadline and the amount of a penalty charge you can set up your own terms of the penalty application and connect these to the penalty charges applied by the supplier.
- The strictest penalty provisions have the highest priority, that is those with higher penalty charge or that are applied earlier.
