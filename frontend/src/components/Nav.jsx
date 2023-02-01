import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import '../css/nav.css'

function Nav() {
  return (
    <Grid container justifyContent='center'>
      <Typography variant='h4' className='headline'>Drone Command And Control</Typography>
    </Grid>
  );
}

export default Nav;