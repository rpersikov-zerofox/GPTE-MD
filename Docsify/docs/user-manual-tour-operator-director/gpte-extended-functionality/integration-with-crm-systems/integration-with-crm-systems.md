# Integration with CRM Systems

For **GP Travel Enterprise** it is possible to integrate with external **CRM Systems** (ex. *Salesforce*) in terms of data synchronization between systems in a certain volume.

To configure connection to a CRM system,

1.  Navigate to admin panel ASP → CRM tab:

![2024-11-26_10-35-16.jpg](/assets/2024-11-26_10-35-16.jpg)

1.  Enable Active checkbox for CRM activation.
2.  Verify the name of integrated CRM systems in the **CRM** column.
3.  Indicate the data for connection to CRM in **Credentials** column. When hovering over a icon, view clarification about the parameters:

![2024-11-26_11-08-11.png](/assets/2024-11-26_11-08-11.png)

1.  View available mappings for CRM connection:

![2024-11-26_11-09-05.png](/assets/2024-11-26_11-09-05.png)

For basic model of integration the following options are supported:

1.  data transmission when creating new private client or company (transfer of values to CRM according to defined fields\* into corresponding CRM base fields without customization);
2.  data transmission when editing existing private client or company.

\*private client profile fields: First name, Last name, E-mail, Country, City, Address, Postal code, Phone, Mobile phone, Date of birth, Citizenship, Active.

company profile fields: Name, Type, Country, City, Address, Postal code, Postal address, Contact Person First name, Contact Person Last name, Phone, Fax, E-mail, Web-site URL, Active.

Custom objects configuration is also possible → it is possible to define own fields for a certain object. For maintaining flexible fields mapping from CRM to GPTE fields in private client and company profiles, there is a possibility to get an object model in order to output the list of fields available for mapping, so that a user can select some of available values.

The volume of integration is defined in each specific case according to the needed requests.
