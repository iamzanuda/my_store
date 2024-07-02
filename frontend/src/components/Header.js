import React from 'react';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@mui/material';
import LanguageIcon from '@mui/icons-material/Language';

function Header() {
  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Clothing Store
        </Typography>
        <Button color="inherit">Login</Button>
        <Button color="inherit">Register</Button>
        <IconButton color="inherit">
          <LanguageIcon />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
