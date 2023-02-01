import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Switch from '@mui/material/Switch';

function ModeCard() {
  return (
    <Card sx={{ minWidth: 275, minHeight: 171 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Current Mode</Typography>
        <Typography sx={{ fontSize: 48 }} className='align-center alt-number'>Guided</Typography>
        <Grid container direction='row' justifyContent='center'>
          <Grid item><Switch color='default' /></Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default ModeCard;