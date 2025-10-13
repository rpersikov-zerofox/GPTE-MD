# Creating Room Types

You need to specify the room types that will be available to tourists in a self-operated hotel. For each room you can define it's description, as well as limitations on how many travelers can be allocated in this room (on main beds, extra beds or sharing places).

To add a new room type:

1.  Open the required accommodation.
2.  On the **Information** tab → **Room types** sub-tab, click **Create**. *Room service* page appears:

![2024-11-15_11-34-39.jpg](/assets/2024-11-15_11-34-39.jpg)

1.  Enter the necessary information: 1. **Name:** full name of a room type as provided by a hotel (*for example, Double Standard Room, Double Deluxe Room, Family Sea View*). 2. **Room code**: code of accommodation type (*for example*, *DBL*) 3. **Accommodation:** the allocation of guests a room is suitable for (*for example, Single or Double*). 4. **Category:** the category of the room (*for example, Standard or Deluxe, etc.*) 5. **Short description:** brief description of a room type. It will be shown in the search results. 6. **Description:** detailed description of a room type. It will be shown in the separate window with room details. 7. **Room capacity:** the boxes in the group are filled in by default when you select accommodation type (e.g. for a single room it will be specified that there is 1 main bed within it; for a double room there are 2 main beds, etc.), but you can specify the number of available main beds, extra beds and sharing places manually. It is possible to add the number of bedrooms and the number of bathrooms in the Capacity and beds section. The information on the number of bedrooms and the number of bathrooms you can also see in reservation.

![2024-11-15_11-35-38.jpg](/assets/2024-11-15_11-35-38.jpg)

h.  **Bed types:** specify the bed types that are available in the room (if supplier provides this information). Click the option of your choice. It is possible to add multiple bed types in each of block (basic and alternate). In case of added settings on bed types (both basic and alternate) information will be displayed in created reservation.
i.  **Options of guests allocation in the room:**while creating your own hotel, you can specify the acceptable number of guests: children and adults separately. Also, for children, you can specify the age.
j.  **Room services:** select the room services that are available for the room type.

![2024-11-15_11-36-08.jpg](/assets/2024-11-15_11-36-08.jpg)

![2024-11-15_11-36-18.jpg](/assets/2024-11-15_11-36-18.jpg)

1.  Click **Save**.

It's very important to correctly specify room capacity, because based on it system automatically identifies what rooms should be offered for the requested quantity of travelers.

For example, if it is configured that Single Room is for 1 guest and Double Room is for 2 guests -- then when user makes search for 1 traveler, system will only propose Single Room among available options. In case when rooms have both main beds, extra beds and sharing places, please, be aware that while searching for available accommodation, the system always calculates the accommodation capacity of the room in the following sequence:

- Main beds
- Extra beds
- Sharing places

The system first checks the availability of beds to accommodate adults and then checks the allocation availability for children. The total accommodation capacity consists of all main beds, extra beds and sharing places put together. According to the current rule, the system checks up available bed spaces in the following sequence:

- First, the system checks if the mail beds are available. In case the rates for them are specified in a price-list, these beds are considered available. You can book them for 2 adults.
- After this, the system checks the availability of extra beds and then - their rates. If the rate is specified in a price-list, this bed space is considered available. You can book the extra bed for an adult.
- Finally the system checks the availability of the sharing place along with its rate. If the rate is specified in a price-list, this accommodation type is considered available. You can book a sharing place for a child.
- Since you can accommodate 4 persons in the room and the price-list features all the respective rates, this option is considered available and the room is displayed in the search results.

Please note that the allocation options are only available for booking if the rates for each accommodation type are specified in a price-list. Otherwise, such accommodation types are not displayed in the search results.

:   To see the example go to
