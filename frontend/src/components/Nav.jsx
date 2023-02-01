import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import '../css/nav.css'

function Nav() {
  return (
    <Grid container justifyContent='center' className='nav-container'>
      <Grid item>
        <img src="./static/images/logo.png" className='nav-logo' />
      </Grid>
    </Grid>
  );
}

export default Nav;