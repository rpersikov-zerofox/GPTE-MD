# Feedback and Reviews

**Reviews and feedback** module gives the possibility to provide and to view feedbacks on services.

Currently a basic implementation is available (for hotels and private clients). In future it is planned to be extended for other products and for more review options.

## Send review invitation

For all bookings made by B2C users after **check-out date** - the user should receive invitation to write feedback how was his trip.

**Default text:**

![2024-11-25_11-09-12.jpg](/assets/2024-11-25_11-09-12.jpg)

It is possible to customize text in the default template via General settings → Templates within "Tourist Email templates" section:

![2024-11-25_11-14-42.jpg](/assets/2024-11-25_11-14-42.jpg)

The e-mail, containing a "Give Feedback" button (leading to the page for reviews), is sent to client e-mail.

## Write review

User can follow the link and write down review of hotel.

When user follows the link via e-mail - the reviews form should open, where he can give feedback:

![2024-11-25_11-22-31.jpg](/assets/2024-11-25_11-22-31.jpg)

It's not necessary to sign in to the system - the link should be available and contain unique token to identify user, booking and hotel.

Additionally user should be able to rate hotel immediately from his own cabinet clicking the icon "Review" within any of the past reservations with status "Confirmed":

![2024-11-25_11-23-32.jpg](/assets/2024-11-25_11-23-32.jpg)

The following questions are currently supported in the review submission form:

a.  Overall impression - between 1 to 10
b.  Would you recommend this hotel? - with Yes/No options
c.  What did you like? - Positive textual feedback
d.  What would you suggest to improve? - Negative textual feedback

After user clicks "Submit Feedback", the feedback is created in the system.

In future reviews will be extended with more questions - like "How did you like meal in the hotel" or "How do you estimate concierge service", etc. - they will depend on certain product type (e.g. can be hotel-specific).

## View feedbacks by TO1

Once the review is submitted - it immediately influences on total score for the product and can be viewed on the web site.

At the same time TO1 *supervisor* and *director* users can view all reviews and total internal rating score, and activate/deactivate them. To view all reviews and feedbacks, navigate to **My Company** → **Reviews and feedback**:

![2024-11-25_12-15-33.jpg](/assets/2024-11-25_12-15-33.jpg)

![2024-11-25_12-17-31.jpg](/assets/2024-11-25_12-17-31.jpg)

The table contains all reviews that were given, but default sorted by date/time of submission by decrease. Detailed pages for each feedback are not available, all information can be shown just in the table.

**Filter** section contains the following fields:

1.  Travel date from/to.
2.  Created date from/to.
3.  Modified date from/to (modification currently means activation or deactivation of feedback, in future it will be possible to modify text by moderator).
4.  Status (on review / published / declined). The status can be updated in the list of feedbacks by selecting an adequate value from *Status* dropdown:

![2024-11-25_12-36-39.png](/assets/2024-11-25_12-36-39.png)

![2024-11-25_12-36-57.png](/assets/2024-11-25_12-36-57.png)

1.  Client name.
2.  Service name.

## View total internal score during search&book

If there is internal rating for any hotel, it is shown during search&book in the same way like external ratings are currently being shown:

The offers can be filtered by **Review score.**If there are multiple reviews available for certain hotel, all of them are shown one after another in different lines (e.g. Tripadvisor and Internal review)\*\*:\*\*

Near the review score the information is added based on how many reviews this score is calculated and presented as a link to view detailed reviews. When user clicks it, all reviews are shown one-by-one in chronological order starting from the most recent (based on Creation date):
