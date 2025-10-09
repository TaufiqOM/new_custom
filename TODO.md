# ITCustom_HideButton Modifications

## Completed Improvements to Make Usage Easier for Users

### 1. Added Button Assignment Wizard
- **File**: `models/button_assignment_wizard.py`
- **Purpose**: Provides an easy way to assign buttons to users via a wizard instead of manual selection.
- **Features**:
  - Shows available buttons not yet assigned to the user.
  - Allows selecting multiple buttons to assign at once.
  - Opens from the user form with a "Assign Buttons" button.

### 2. Improved User Interface in User Form
- **File**: `views/res_users_views.xml`
- **Changes**:
  - Added "Assign Buttons" button to open the assignment wizard.
  - Changed hide_button_ids field to use `many2many_tags` widget for better display and management.

### 3. Enhanced Button Management Views
- **File**: `views/itcustom_button_views.xml`
- **Changes**:
  - Added tree view for listing buttons with search and filter capabilities.
  - Updated form view to include active field.
  - Modified action to support tree and form views.

### 4. Added Wizard Views
- **File**: `views/button_assignment_wizard_views.xml`
- **Purpose**: UI for the button assignment wizard with available and selected buttons.

### 5. Updated Module Manifest
- **File**: `__manifest__.py`
- **Changes**: Added the new wizard view to data files.

## How to Use the Improved Module

1. **Discover Buttons**: Use the "Discover Buttons" menu under Administration > Buttons to Hide to scan for available buttons.
2. **Assign Buttons to Users**:
   - Go to Settings > Users & Companies > Users.
   - Open a user form.
   - In the "Hide Specific Buttons" tab, click "Assign Buttons".
   - Select buttons from the available list and assign them.
3. **Manage Buttons**: Use the "Buttons to Hide" menu to view, edit, or deactivate buttons.

## Benefits
- Easier button assignment through wizard interface.
- Better UI with tags and tree views.
- Simplified workflow for administrators.
