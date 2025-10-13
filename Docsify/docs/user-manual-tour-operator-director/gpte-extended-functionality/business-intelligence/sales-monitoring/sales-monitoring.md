# Sales Monitoring

Business Intelligence module provides advanced system analytics in real time.

The first version of this module furnishes monitoring of products sales.

## **Enabling and navigation**

Business Intelligence → Monitoring module can be enabled/disabled on the installation under ASP.

If the option is enabled, the functionality is available and displayed as **BI**menu:

![2024-11-25_09-55-27.jpg](/assets/2024-11-25_09-55-27.jpg)

Currently BI feature is available only for Tour Operator Level 1, director and supervisor roles.

To view products sales analytics, navigate to BI menu → Monitoring:

![image-20241125-063614.jpg](/assets/image-20241125-063614.jpg)

![image-20241125-063727.jpg](/assets/image-20241125-063727.jpg)

## **Sales analytics visualization**

Sales analytics is displayed in the following way:

![image-20241125-063754.png](/assets/image-20241125-063754.png)

1.  Menu bar: the enabled on installation products are displayed -- activities, flights, transfers, hotels.
2.  Filter block: collapsed by default, analytics for upcoming 2 weeks is displayed. When expanding the filter, it is possible to set the following parameters:

<!-- -->

a.  Dates from/to (it's possible to select dates both in future and in the past)
b.  Location (country and city selection).

![image-20241125-063917.jpg](/assets/image-20241125-063917.jpg)

1.  Dates bar: the dates in future with required products are displayed in ascending order.
2.  Product name and location: the product name represents a link to the product. Location is displayed only for activities. For transfers: only shared transfers are displayed.
3.  Analytics cell: the following data are provided:

<!-- -->

a.  Total amount of allotments for the indicated date

b. Amount of sold allotments (in green)

c. Amount of the allotments to sell (in red)

d. Sales % = sold / total

e.  Gross sales -- final sale values (brutto)

f. Price from -- minimum product price for the indicated date from the base price-list for adults (without discounts)

- In case there are several product services for a certain date, the Total amount is calculated for all services.
- In case there are sold services from allotments and on request, Total value is calculated for the amount of sold allotments.

1.  Chart icon: Switching to the detailed sales analytics for the indicated date.

## **Visualization of detailed sales analytics by day**

Sales dynamics analytics by days can be provided in addition to the summary analytics by products and dates.

*For example, an excursion is planned for the 10th of June, 50 seat allotments are allocated for it. The first sale is executed on the 1st*\* of May. After that the Tour Operator initiates promotional campaigns and analyses their results -- what amount is sold every day.\*

When navigating to the section with detailed analytics (clicking on a chart icon), the sales progress for a certain date is displayed -- from the moment of the first reservation appearing till the current moment (or event time if its date is in the past).

The chart displays the sales state for dates in the past and allows to understand how effective particular advertising impacts are.

![image-20241125-064022.png](/assets/image-20241125-064022.png)

*The provided chart shows that on 07.01.2023 the product sales indicator was 0, after that the product started to be gradually sold, and it is possible to trace sales quantity by days till 20.02.2023.*

The chart is displayed chronologically:

a. on the horizontal axis -- dates in ascending order from the moment of the first sale till the current moment / event date;

b. on the vertical axis -- the sold product units amount

The set allotment as a target value for sales is displayed with a horizontal line at the top (green line on the chart).

It is possible to point to a certain date and see sales quantity for this date.

*The example of chart data displaying:*

- *07.01 --2 excursion seats are sold*
- *10.01 -- 4 excursion seats are sold*
- *14.01 -- 1 excursion seat is cancelled*
- *22.01 -- 2 excursion seats are sold*

*Hence it is shown on the chart in the following way:*

- *07.01 -- 2*
- *10.01 -- 6*
- *14.01 -- 5*
- *22.01 -- 7*
