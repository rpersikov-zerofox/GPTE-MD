# Modifying Users

Update existing user accounts to change roles, contact information, permissions, or account status. Manage your complete user directory from the Users page.

## Access the Users List

Navigate to **My Company** > **Users** to view all user accounts.

![Company Users List](/assets/company-users-list.png)

## User Management Capabilities

From the Users page, you can:

- **Browse Users** - View all company user accounts
- **Search Users** - Find users by name or role
- **Add New Users** - Create additional user accounts
- **Edit Details** - Update user information and settings
- **Change Roles** - Modify user permissions
- **Activate/Deactivate** - Enable or disable user access
- **Export List** - Download user list as Excel file
- **Import Users** - Upload user list to system configuration

## Edit User Information

To modify a user account:

1. On the **Users** page, locate the user you want to edit
2. Click the user's name to open their profile
3. Update the required fields:
   - Name and contact information
   - Email address and phone number
   - Role and permissions
   - Position and department
   - Active status
4. Click **Save** to apply changes

## Change User Role

To update a user's permissions:

1. Open the user's profile
2. Locate the **Role** field
3. Select a new role from the dropdown
4. Click **Save**

The user's access and permissions update immediately based on the new role.

See [User Roles](../creating-new-user-profile/user-roles/user-roles.md) for role descriptions and permissions.

## Search for Users

Use search filters to find specific users:

**Search by Name:**
1. Enter the user's name in the search field
2. The list filters to show matching results

**Filter by Role:**
1. Select a role from the role filter dropdown
2. The list displays only users with that role

## Export User List

Download your user directory:

1. On the **Users** page, click the **Export** button
2. The system downloads an Excel file (XLS/XLSX format) containing:
   - All user names
   - Email addresses
   - Assigned roles
   - Active status
   - Other user details

Use this export for reporting, backup, or bulk updates.

## Import User List

Upload a user list to quickly configure multiple accounts:

1. Prepare an Excel file with user data
2. On the **Users** page, click the **Import** button
3. Select your prepared file
4. The system uploads and processes the user list

**Note:** Contact technical support for the correct import file format and field requirements.

## Deactivate Users

Temporarily disable user access without deleting the account:

1. Open the user's profile
2. Toggle the **Active** switch to OFF

   ![Deactivate user toggle](/assets/company-user-deact.png)

3. Click **Save**

The user can no longer log in to the system.

### Deactivation Rules

- You can deactivate any user **except users with Director role**
- Deactivated accounts remain in the system
- User data and history are preserved
- Accounts can be reactivated at any time

## View Archived Users

Access deactivated user accounts:

1. On the **Users** page, click **Archive** at the top of the list
2. The system displays all inactive users
3. To reactivate a user:
   - Open the archived user's profile
   - Toggle the **Active** switch to ON
   - Click **Save**

The user can immediately log in again.

## Configure User Notifications

Set up email notifications and alerts for users. Configure notification preferences to control what emails users receive from the system.

For detailed instructions, see the Notifications section in [General Settings](../../../general-settings/notifications/notifications.md).

## Best Practices

### User Account Management

- **Review regularly** - Audit user accounts quarterly
- **Remove access promptly** - Deactivate accounts for employees who leave
- **Update roles** - Adjust permissions when job responsibilities change
- **Verify contact info** - Ensure email addresses are current for notifications

### Security Considerations

- **Limit Director roles** - Only assign to senior management
- **Use appropriate roles** - Match permissions to job requirements
- **Monitor active users** - Review who has system access
- **Check archived users** - Periodically review deactivated accounts

## Troubleshooting

**Cannot Modify User:**
- Check your own role permissions (requires Director or Supervisor)
- Cannot modify Director users if you have Supervisor role

**Changes Not Saving:**
- Verify required fields are completed
- Check for error messages
- Ensure unique username is maintained

**Cannot Deactivate User:**
- Director roles cannot be deactivated
- Check if you have appropriate permissions

## Related Topics

- [Creating New User Profile](../creating-new-user-profile/creating-new-user-profile.md) - Add new users
- [User Roles](../creating-new-user-profile/user-roles/user-roles.md) - Role permissions reference
- [Upload User Avatar](../uploading-user-avatar/uploading-user-avatar.md) - Add profile pictures
- [Upload User Documents](../uploading-user-documents/uploading-user-documents.md) - Attach user files
