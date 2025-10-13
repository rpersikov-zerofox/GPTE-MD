# PNR Import

Most Tour Operators are used to book flights in GDS terminal. After the booking is made they need to copy terminal to the system.

This is possible via PNR Import functionality.

When user clicks **PNR Import** - the system opens a pop-up with suggestion of GDSs for which this functionality is available (turned ON under ASP) and field to enter PNR Ref #.

![2024-12-24_16-21-30.jpg](/assets/2024-12-24_16-21-30.jpg)

After clicking **Import** the system imports data from GDS (current architecture assumes the flow of requests: Front -\> API Back -\> API Hub -\> API GDS).

All content is pre-populated in Extra Service form.

1.  Status - Quote, Prebooking or Confirmed (depending on PNR status).
2.  Name - made by default by airport codes (e.g. CDG-LHR-CDG for return flight CDG-LHR and back).
3.  Ref \# - PNR.
4.  Supplier - GDS, from which this import was made.
5.  Dates - based on "date from" / "date to" of flights in PNR, are set automatically.
6.  Quantity of pax - based on quantity of travelers in PNR.
7.  Details - flights departures and arrivals from GDS.
8.  Description - fare rules.
9.  Supplier price - price from GDS.
10. Client price - markup is added automatically and price is calculated automatically.
11. Travelers - are taken from PNR.

If user wants - he can change any fields on this form.

Additional button **Update PNR from GDS** that updates the form with actual information from GDS is added on this form.
