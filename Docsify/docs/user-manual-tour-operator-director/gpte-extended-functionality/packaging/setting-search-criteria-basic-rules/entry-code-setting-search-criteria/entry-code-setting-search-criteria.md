# Entry code: Setting Search criteria

In case the first part is any entry code (e.g. **E1, T1, F2**. etc) including also manually entered codes, the search criteria of the component under configuration will depend on the conditions specified for other services of the same package.

**Example:** In the package there are flight and accommodation components. The check-in date for accommodation is June, 1 - the same date the flight touches down. Thus for the accommodation component, the service start date can be set *F1.arrival_date*. It means that the check in date will adjust to the flight arrival date specified by a tourist.
