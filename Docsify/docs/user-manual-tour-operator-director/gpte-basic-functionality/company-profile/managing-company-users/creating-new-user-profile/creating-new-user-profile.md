# Creating New User Profile

Add new users to your GP Travel Enterprise system by creating user profiles with appropriate roles and permissions.

## Prerequisites

Before creating a user:

- You must have Director or Supervisor role permissions
- Determine the appropriate user role for the new user
- Have the user's basic information ready (name, email, contact details)

## Create a New User

1. Navigate to **My Company** > **Users**.

2. Click **New User Profile**.

   ![New User button](/assets/new-user-1.png)

3. Complete the required fields marked with an asterisk (*).

   ![New User form](/assets/new-user-2.png)

### Required Information

**Basic Details:**
- **First Name** - User's given name
- **Last Name** - User's family name
- **Email** - User's email address for notifications
- **Phone** - Contact phone number

**Login Credentials:**
- **Login** - Username for system access (cannot be changed after creation)
- **Password** - Initial password (user should change after first login)
- **Role** - Determines user permissions and access level

**Additional Information:**
- **Position** - User's job title or role in the company
- **Department** - Organizational unit
- **Active** - Check to enable the account immediately

### Important Field Notes

**Role Selection:**
The role determines what the user can access and do in the system. Choose carefully based on job responsibilities.

See [User Roles](user-roles/user-roles.md) for detailed role descriptions and permissions.

**Login Username:**
- Must be unique across your company
- Cannot be changed after the user is created
- Used for system authentication
- Case-sensitive in some configurations

**Password:**
- Set a temporary password
- User should change it on first login
- Follow your organization's password policy

### Login Requirements

To access the system, users need three pieces of information:

1. **Company Code (or Alias)** - Your company's unique identifier
2. **Username** - The login you create
3. **Password** - The user's password

**Finding Your Company Code:**

Your company code and alias appear on the user profile page below the **Active** checkbox.

![Company code location](/assets/new-user-role.png)

You can also set a memorable alias instead of using the auto-generated company code. Configure this in [Configuring Company Information](../../configuring-information-about-the-company/configuring-information-about-the-company.md).

4. Click **Save** to create the user account.

## After Creating the User

Once the account is created:

1. **Notify the User** - Provide login credentials securely (company code/alias, username, temporary password)
2. **First Login** - User should log in and change their password
3. **Verify Access** - Confirm the user can access appropriate system areas
4. **Configure Preferences** - User can customize their profile and settings

## Next Steps

After creating the user account:

- [Upload User Avatar](../uploading-user-avatar/uploading-user-avatar.md) - Add a profile picture
- [Upload User Documents](../uploading-user-documents/uploading-user-documents.md) - Attach relevant documents
- [Modifying Users](../modifying-users/modifying-users.md) - Update user information as needed

## Troubleshooting

**Login Already Exists:**
- Choose a different username
- Check if the user already has an account

**User Cannot Log In:**
- Verify company code/alias is correct
- Check username spelling and case
- Confirm password was entered correctly
- Ensure the Active checkbox is selected

**User Has Wrong Permissions:**
- Review the assigned role
- Modify the user account to change the role
- See [Modifying Users](../modifying-users/modifying-users.md)

## Related Topics

- [User Roles](user-roles/user-roles.md) - Available roles and their permissions
- [Managing Company Users](../managing-company-users.md) - User management overview
- [Modifying Users](../modifying-users/modifying-users.md) - Edit existing user accounts
