# Documentation Standards & Terminology Glossary

**Created:** 2025-10-08
**Scope:** user-manual-tour-operator-director/gpte-basic-functionality
**Folders:** company-profile, reservations, general-settings

---

## Terminology Standards

### Core Terms (Use Consistently)

| **Use This** | **Not This** | **Context** |
|-------------|-------------|-------------|
| **reservation** | booking, order | Primary term for travel bookings |
| **traveler** | tourist, passenger | People who travel/book services |
| **user** | system user | People who use the system (employees, agents) |
| **company** | organisation, organization | Business entity |
| **My Company** | Company Profile, My company | Menu name (exact case) |
| **Reservations** | reservations | Menu name (capitalized) |
| **General Settings** | General settings, general settings | Menu name (title case) |

### UI Navigation Standards

**Menu Paths:**
- Format: `**Menu Name** > **Submenu** > **Page**`
- Example: `**My Company** > **Users**`
- Always bold menu/button names
- Use `>` with spaces for menu navigation

**Buttons and UI Elements:**
- Always bold: `**Save**`, `**Edit**`, `**Upload**`
- Include icon references only when functionally important

**Field References:**
- Bold field names: `**Name**`, `**Email**`, `**Type**`
- Use present tense for instructions: "Enter the name" not "Enter name"

---

## Formatting Standards

### Procedural Steps

```markdown
1. Navigate to **Menu** > **Submenu**.

   The **Page Name** opens.

2. Click **Button**.
3. Complete the required fields.
```

**Rules:**
- One action per numbered step
- Add blank line after step with outcome description
- Use present tense: "The page opens" not "will open"
- Active voice: "Click Save" not "The Save button should be clicked"

### Lists

**Unordered lists:**
```markdown
- **Term** - Description of the term.
- **Another Term** - Another description.
```

**When to use:**
- Field descriptions
- Feature lists
- Non-sequential items

### Notes and Warnings

```markdown
**Note:** This setting does not affect existing reservations.
```

---

## Image Placeholder Format

All images replaced with:

```markdown
[IMAGE_PLACEHOLDER: descriptive-filename.png | Alt: Descriptive text explaining what the image shows]
```

**Examples:**
```markdown
[IMAGE_PLACEHOLDER: company-info-form.png | Alt: Company information form showing fields for name, address, and contact details]

[IMAGE_PLACEHOLDER: upload-document-dialog.png | Alt: Upload document dialog with document type dropdown and validity period fields]
```

---

## Common Fixes Applied

### 1. Escape Sequences
- ❌ `In the\*\* Field \*\*enter`
- ✅ `In the **Field** enter`

### 2. External Links
- ❌ `https://gp-team.atlassian.net/wiki/...`
- ✅ Removed or replaced with internal references

### 3. Stub Files
- Completed with actual content or marked for removal

### 4. Navigation Consistency
- ❌ `On the Reservations menu`
- ✅ `Navigate to **Reservations** > **View Reservations**`

### 5. Terminology
- ❌ "tourist booking"
- ✅ "traveler reservation"

---

## Writing Style

- **Voice:** Active
- **Tense:** Present
- **Tone:** Professional, direct, helpful
- **Audience:** Tour operator directors and administrators (end users)
- **Perspective:** Second person ("you" and "your")

### Examples

❌ **Avoid:**
> The reservation can be edited by clicking on the Edit button which will open a dialog.

✅ **Use:**
> Click **Edit** to modify the reservation.

---

## File Naming Convention (for screenshots you'll create)

**Pattern:** `[section]-[feature]-[view].png`

**Examples:**
- `company-profile-info-form.png`
- `reservations-search-results.png`
- `general-settings-currency-rates.png`

Use lowercase with hyphens, descriptive but concise.

---

## Cross-References

When referencing other documentation:

```markdown
For more information, see [Page Title](../path/to/page.md).
```

Not: ~~*see Page Title section*~~

---

This glossary ensures consistency across all 58 files processed in this cleanup.