# Calculating Accommodation capacity for Tours

While searching for available accommodation, the system always calculates the accommodation capacity of the room in the following sequence:

- Capacity (main beds)
- Extra beds
- Sharing places

The system first checks the availability of beds to accommodate adults and then checks the allocation availability for children. The total accommodation capacity consists of all capacity, extra beds and sharing places put together.

**Example 1** Assume that you create a room where 4 people can be accommodated with three bed types available: two main beds, one extra bed. Moreover there is a possibility to accommodate one person without a bed:

![2024-11-13_10-41-17.png](/assets/2024-11-13_10-41-17.png)

You need to accommodate three adults and one child in this room. According to the current rule, the system checks up available bed spaces in the following sequence:

- First, the system checks if the mail beds are available. In case the rates for them are specified in a price-list, these beds are considered available. You can book them for 2 adults.
- After this, the system checks the availability of extra beds and then - their rates. If the rate is specified in a price-list, this bed space is considered available. You can book the extra bed for an adult.
- Finally the system checks the availability of the sharing place along with its rate. If the rate is specified in a price-list, this accommodation type is considered available. You can book a sharing place for a child.
- Since you can accommodate 4 persons in the room and the price-list features all the respective rates, this option is considered available and the room is displayed in the search results.

**Example 2** Let us have a look at the above described example from another respective. Assume we need to accommodate three adults. The price-list however does not contain rates for an extra bed for an adult.

When the system successfully checks the availability of two main beds, it proceeds to extra beds. Since the price-list does not include rates for an extra bed for an adult, this accommodation type is considered unavailable. So is the whole room. In theory however the room can accommodate three adult guests on the following conditions: two guests on the main bed spaces + one person without a bed. Such a room is not displayed in the search results.

**Example 3** When you accommodate children, there can be an exception from the rule described in example 2. For instance, you need to accommodate two adults and two children in a room with two standard beds, one extra bed and one shared space (accommodation without a bed). Then, even when the price-list rates are specified for adults, but the adult age category allows to classify children as adults (for example, when the adult age category ranges from 0 to 90 years old), both children can be accommodated in the room but at the rates provided for adults.

**Example 4** Assume that you want to create a family room where children can be accommodated on a sharing place.

![2024-11-13_10-43-06.png](/assets/2024-11-13_10-43-06.png)

The total number of available bed spaces of the room in order to avoid 3 adults from booking this room type you can use options of guest allocation in the room.

**This functionality is currently available via administration panel.**

![2024-11-13_10-41-17.png](/assets/2024-11-13_10-41-17.png)

Please note that there is a necessity to list all possible allocation variations.
