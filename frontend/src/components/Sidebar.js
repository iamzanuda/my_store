import React from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';

function Sidebar() {
  return (
    <div>
      <Typography variant="h6">Categories</Typography>
      <List>
        <ListItem button>
          <ListItemText primary="Category 1" />
        </ListItem>
        <ListItem button>
          <ListItemText primary="Category 2" />
        </ListItem>
        {/* Add more categories as needed */}
      </List>
    </div>
  );
}

export default Sidebar;
