import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';

function AltitudeInfo() {
  return (
    <Card sx={{ minWidth: 275, minHeight: 171 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Current Altitude (M)</Typography>
        <Typography sx={{ fontSize: 48 }} className='align-center alt-number'>0.000</Typography>
        <Grid container direction='row' alignItems='center' justifyContent='center' className='refresh-rate'>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Refresh Rate: 0.5 sec</Typography>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default AltitudeInfo;