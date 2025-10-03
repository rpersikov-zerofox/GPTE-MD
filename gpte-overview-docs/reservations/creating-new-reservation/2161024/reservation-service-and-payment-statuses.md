# Reservation, Service and Payment Statuses

Last Modified: 2022-08-29T12:58:15.959Z\
Version: 6\
Page ID: 1936424994

***

## Reservation, Service and Payment Statuses

GP Travel Enterprise supports the following reservation statuses (set manually) and service statuses (set automatically) that are related to some actions with them in the system.

### Reservation statuses in GP Travel Enterprise

| Booking status                     | Description                                                                                                                                                                                      | Permissions                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New**                            | Is assigned in case of creating an empty reservation request to add booking later                                                                                                                | - Add services                                                                                                                                        |
| **In Progress**                    | Default status when at least one service is added and when staff is still working with a reservation                                                                                             | <p>- Can add additional services<br>- Can create vouchers<br>- Can modify and cancel services<br>- Accountable</p>                                    |
| **Completed**                      | When work with a reservation is done, e.g. no need to add any services or issue invoices                                                                                                         | <p>- Can add additional services<br>- Can create vouchers<br>- Can modify and cancel services<br>- Accountable</p>                                    |
| **Completed and revision is done** | When work with a reservation and additional revision / reconciliation is done, e.g. by accounting team; usually such state is related to additional automatic movement of reservation to Archive | <p>- Can add additional services<br>- Can create vouchers<br>- Can modify and cancel services<br>- Accountable<br>- Can be restricted for editing</p> |
| **Cancelled**                      | When all the services within reservation are cancelled                                                                                                                                           | - N/A                                                                                                                                                 |

### Service (booking) statuses in GP Travel Enterprise

| Service status                 |                                                                                                                                                                                                   Description | Permissions                                                                                                             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------------------------------- |
| **Estimated**                  |                                                                                                                                                                                     Service added to a basket | - Can be booked                                                                                                         |
| **Quotation / Saved order**    |                                                                                                    Service that is saved as an offer but request to book is not sent to supplier or decreased from allotments | <p>- Can be booked<br>- Can be cancelled</p>                                                                            |
| **Confirmation pending**       |                                                                                                                                                         The service is pending confirmation from the supplier | <p>- Can be modified (confirmed or rejected)<br>- Accountable</p>                                                       |
| **Reservation check required** | Status when some internal or external error during booking, modification or cancellation occurred and requires check with external supplier. Also assigned in case when booking is moved to manual correction | <p>- Can be restored manually<br>- Status can be checked via API with external suppliers<br>- Accountable</p>           |
| **Confirmed**                  |                                                                                                                  Status when service is confirmed by supplier via API or decreased from guaranteed allotments | <p>- Can create vouchers<br>- Can be modified<br>- Can be cancelled<br>- Can be corrected manually<br>- Accountable</p> |
| **Rejected**                   |                                                                                                                                   Status when service is not confirmed by supplier after confirmation pending | - Can be corrected manually                                                                                             |
| **Cancelled**                  |                                                                                                                                                                              Status when booking is cancelled | <p>- Can be corrected manually<br>- Accountable</p>                                                                     |
| **No Show**                    |                                                                                                                                           Status for hotels only to mark that guest has not appeared at hotel | <p>- Can be corrected manually<br>- Accountable</p>                                                                     |

{% hint style="info" %}
Note: In case of need to have additional statuses the discussion is required as all the statuses are related to some actions and can affect the current processes.
{% endhint %}

### Payment statuses in GP Travel Enterprise

| ICON | PAYMENT status          | Description                                                                                                                   | Permissions                                                                                                            |
| ---: | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
|      | **Not invoiced**        | Invoice it not issued yet                                                                                                     | - Invoice can be issued                                                                                                |
|      | **Not fully invoiced**  | Invoice is issued partly, e.g. for some amount on individual booking or for one or several services in booking                | <p>- Invoice can be issued for remaining amount<br>- Issued invoice can be deleted<br>- Issued invoice can be paid</p> |
|      | **Invoiced**            | Invoice is issued for full amount of one service in case of individual booking or for all services in booking                 | <p>- Issued invoice(s) can be deleted<br>- Issued invoice(s) can be paid</p>                                           |
|      | **Waiting**             | Invoice should be uploaded to the system from external application via API in case of integration with some accounting system | - N/A                                                                                                                  |
|      | **Transfer in process** | Invoice has been paid by client (e.g. Travel Agent) and marked as money transfer is on its way                                | - Status can be changed to paid by TO1 staff                                                                           |
|      | **Payment is overdue**  | When due date had passed but invoice wasn’t paid                                                                              | - New invoice can be issued                                                                                            |
|      | **Partly paid**         | When issued invoice is paid partly                                                                                            | <p>- Remaining invoice can be deleted<br>- Remaining invoice can be paid</p>                                           |
|      | **Paid**                | When invoice is fully paid                                                                                                    | - N/A                                                                                                                  |
