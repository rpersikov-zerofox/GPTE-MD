# KPIs

In order to achieve certain goals SMART approach shows good results, when concrete and measurable goals are defined in advance and then we just monitor how we approach to them. The same logic is implemented within Business Intelligence → **KPI module**.

*Note: In the current version of the system this feature will be available only for***\*TO1**\*\*users director and supervisor. In future it will be extended with possibility to setup KPI by agents and also for clients - to monitor their progress by themselves.\*

## **Enabling and navigation**

KPI module can be enabled/disabled on the installation under ASP.

If the option is enabled, the functionality is available and displayed under **BI**menu. To view KPI data, navigate to BI menu → **KPIs**:

![2024-11-25_10-01-31.jpg](/assets/2024-11-25_10-01-31.jpg)

![image-20241125-070228.png](/assets/image-20241125-070228.png)

## **Create / edit KPI**

To create KPI, click on **Create** button and fill the following fields:

![image-20241125-070331.png](/assets/image-20241125-070331.png)

- **Title**: enter the name of the KPI.
- **Period**: indicate the from - to period which this KPI relates to. The period cannot exceed 1 year.
- **Based on**: choose what should be the base for KPI calculation: \* Booking dates (means that monitoring is executed based on the date of booking). \* Start dates (means that only services that start (e.g. check in) during defined period - will be used in calculations of KPI). \* End dates (means that only services that finish (e.g. check out) during defined period - will be used in calculations of KPI).
- **Set KPI for the following**: set the KPI parameters that need to be tracked. In the current version - choice is between Turnovers and Income (at least one of KPI parameters should be defined, in future more parameters can be added: *e.g. also Quantity of trips, Quantity of services booked, Active Travelers, Active Clients, etc*). Default currency is set by default, but user can change it if needed.
- **Compare with historical data**: check this option in case it's required to show additionally historical data for similar period past years (up to 2 years).
- **Internal note**: enter any notes into the text area.

Click **Save**. New KPI is added to the KPIs table.

To edit existing KPI, click on the KPI title link:

![image-20241125-070658.png](/assets/image-20241125-070658.png)

## **KPI Monitoring**

Within KPI module it is possible to check what percentage of KPIs is already completed and what is the current progress of sales (how much sold and due to sell).

KPI monitoring information can be accessed by clicking on a chart icon on KPIs page:

![image-20241125-070758.png](/assets/image-20241125-070758.png)

The tab "BI" of KPI with the following information on how KPI is performed is opened:

![image-20241125-070832.png](/assets/image-20241125-070832.png)

- **% done**: indicates what percent is already achieved
- **Sold**: indicates how much already sold
- **Due to sell**: indicates how much due to sell
- **% from historical data**: if historical data period has been set, percentage of this KPI growth is calculated as compared with it. The percentage from historical data is calculated for KPI, not for current status of sales. Statistics is shown based on last 2 years in descending year (e.g. in 2023 turnover was EUR 4 000 000, in 2024 the goal for turnover is EUR 5 000 000 - this means 125% growth).
