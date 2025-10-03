---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# !Tourist booking fields settings

{% hint style="warning" %}
This functionality is currently available via administration panel.
{% endhint %}

You can configure and make the list of booking fields more flexible by defining mandatory and optional fields reqired for tourists.

1.  On the general settings menu, click **Tourist booking fields settings**:

    ![](blob:https://gp-team.atlassian.net/c25d7bdd-8a11-4641-bc0a-7ff48276b1ae#media-blob-url=true\&id=a39484fb-fd22-42e9-aa2c-b04972e9c518\&collection=contentId-1922256387\&contextId=1922256387\&width=233\&height=358\&alt=)
2.  On the window appear select the product you would like to configure the list of fields and click **Edit:**

    ![](blob:https://gp-team.atlassian.net/092dcc60-7ff4-41bd-a701-ce45499e1527#media-blob-url=true\&id=fe059d40-c633-4109-abe4-e71e4eb082e2\&collection=contentId-1922256387\&contextId=1922256387\&width=946\&height=830\&alt=)

    &#x20;

#### Extension of configuration of tourist's fields for booking <a href="#extension-of-configuration-of-tourists-fields-for-booking" id="extension-of-configuration-of-tourists-fields-for-booking"></a>

We have expanded the settings of the tourist’s fields by adding a choice for whom the fields should be available or hidden:

✔ For main tourist

✔ For child

✔ For all tourists

The logic of the functionality “**Tourist booking fields settings” is extended and improved** for the main types of products.&#x20;

You can specify which fields are Mandatory, Optional or Disabled for the Main tourist, All tourists and/or Children. The fields on booking will be displayed according to this configuration.

3\. Choose **Mandatory**, **Optional** or **Disabled** option.

4\. Click **Save**.

&#x20;

**Tourist booking fields settings can be relate** not to the whole type of products, but **to some of them based on certain characteristics** either of product or sales channel, e.g.:

_Different settings for PRIVATE and SHARED transfers and excursions;_

_Different settings for hotels in different COUNTRIES;_

_Different settings for LOCAL flights and INTERNATIONAL etc._

Within the details of each rule, the user can set the fields and conditions, when this rule applies.

![](blob:https://gp-team.atlassian.net/63e1b72e-86de-4420-ba54-5509e01cf5d8#media-blob-url=true\&id=4c2be42e-6dce-47c0-89ab-700ac45a0f7b\&collection=contentId-1922256387\&contextId=1922256387\&width=1124\&height=500\&alt=)![](blob:https://gp-team.atlassian.net/c928f483-59a9-4b40-adfd-79dd1ffafa8c#media-blob-url=true\&id=b3b77c7f-0ffb-4ab0-b121-ed1718563b90\&collection=contentId-1922256387\&contextId=1922256387\&width=921\&height=624\&alt=)

&#x20;As a result of **Tourist booking fields settings** made in the back office **the API returns** for each offer for the booking page a list of required fields and blocks of information about travelers. The front end capture this information and show only corresponding fields.

{% hint style="success" %}
External suppliers have their own rules for required booking details. Supplier settings override the defaults and can be combined with the Tour Operator settings.
{% endhint %}
