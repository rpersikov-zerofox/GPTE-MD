# Custom fields

**This functionality is currently available via administration panel.**

To configure custom fields for a corporate client,

1.  In the list of corporate clients, click a corporate client of your choice.
2.  In the client profile, go to the **Settings** tab and click **Custom** fields.
3.  On the **Custom fields** tab, click **Create**. The New Custom Field window appears:

![image-20200922-171739.jpg](/assets/image-20200922-171739.jpg)

In the new custom field window the configuration is realized through 3 steps:

- Information.
- Values.
- Conditions.

4.  On the **Information** tab, specify general information:

- **Label**: type the label for the custom field, e.g. *trip reason, trip leader*, etc.
- Object: select either **Reservation** for custom fields that apply to reservations (e.g. *trip type*) or **Person**for custom fields that apply to staff management (e.g. *trip leader. department*, etc.);
- **Type**: select whether the custom field is displayed as a drop-down or as a text box.
- **Required**: specify whether the custom field is to be filled mandatory or optionally.
- **Settings**: configure the custom field display while booking a service.
- **Comments**: leave any additional comments on the custom field.

5.  Click **Save** and go to the **Values** tab.
6.  On the Values tab, for the custom fields of drop-down type, specify the items to display in the drop-down.

- Click **Create**. The New Value window appears:

![image-20200922-173934.jpg](/assets/image-20200922-173934.jpg)

- In the New Value window, specify the values for a drop-down item.

7.  Click **Save** and go to the **Conditions** tab.
8.  On the **Conditions** tab you can set the conditions of displaying custom fields.

![image-20200922-174049.jpg](/assets/image-20200922-174049.jpg)

For example, if a corporate user books a business trip, you want them to specify the department they work at. Then for the Department custom field you apply the following conditions:

![image-20200922-174138.png](/assets/image-20200922-174138.png)

To set the custom field conditions,

- On the **Conditions** tab, click **Edit**.
- Depending on the condition you want to apply, select the required form to fill in: person or reservation. If you want to restrict the application of the current custom field by trip type, trip reason, cost center, budget group, etc. - select the **reservation** **form**. If you wan to restrict the application of the current custom field by department, occupation, trip leader, etc. - select the **person form**.
- From the\*\* Field \*\*drop-down, select the custom field by which the application of the current one will be conditioned.
- From the **Condition** drop-down, select either **equal** or **not equal**. In case you select **equal**, the current custom field will be applied only if the conditional custom field is filled in with the specified value. In case **not equal** is selected, the current custom field will be applied always, except when the conditional custom field is filled in with the specified value.
- In case you wan to add multiple conditions, click and repeat the procedure.

9.  Click **Save** and click **Close** to finish the procedure.
