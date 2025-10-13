# Tourist booking fields settings

**This functionality is currently available via administration panel.**

For flexibility to be able to customize what data about travelers is required on booking threre is the ability to configure the list of fields, and whether they are mandatory or optional.

To configure the list of fields,

1.  On the general settings menu, click **Tourist booking fields settings**:

![image-20201029-092324.png](/assets/image-20201029-092324.png)

2.  On the window appear select the product you would like to configure the list of fields and click **Edit:**

![image-20201029-092348.png](/assets/image-20201029-092348.png)

## Extension of configuration of tourist\'s fields for booking

We have expanded the settings of the tourist's fields by adding a choice for whom the fields should be available or hidden:

✔ For main tourist

✔ For child

✔ For all tourists

The logic of the functionality "**Tourist booking fields settings" is extended and improved**for the main types of products.

It is possible to specify which fields are Mandatory, Optional or Disabled for Main tourist, All tourists and Children. Depending on this configuration fields are shown in the proper way on booking.

3.  Depend on your needs, select Mandatory, Optional or Disabled option.
4.  Click **Save**.

Now **Tourist booking fields settings can relate** not to the whole type of products, but **to some of them based on certain characteristics** either of product or sales channel, e.g.:

*Different settings for PRIVATE and SHARED transfers and excursions;*

*Different settings for hotels in different COUNTRIES;*

*Different settings for LOCAL flights and INTERNATIONAL etc.*

Within the details of each rule, the user can set the fields and conditions, when this rule applies.

![image-20201029-093608.png](/assets/image-20201029-093608.png)

![image-20201029-093612.png](/assets/image-20201029-093612.png)

As a result of **Tourist booking fields settings**made in the back office **the API returns** for each offer for the booking page a list of required fields and blocks of information about travelers. The front end capture this information and show only corresponding fields.

**Settings in the back office:**

![image-20201029-093723.png](/assets/image-20201029-093723.png)

*Note! External suppliers have their own rules, on which travelers\' details are required for booking. Supplier settings override the default ones and can be combinable with the settings of Tour Operator.*
