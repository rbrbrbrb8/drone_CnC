import React, {useEffect, useState} from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import axios from 'axios';

function AltitudeInfo() {

  const [currentAlt,setCurrentAlt] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      axios.get('/getAltitude').then(res=>{
        setCurrentAlt(res.data);
      })
    },1000);
    return () => {
      clearInterval(interval);
    }
  },[])

  return (
    <Card sx={{ minWidth: 275, minHeight: 171 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Current Altitude (M)</Typography>
        <Typography sx={{ fontSize: 48 }} className='align-center alt-number'>{currentAlt}</Typography>
        <Grid container direction='row' alignItems='center' justifyContent='center' className='refresh-rate'>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Refresh Rate: 1 sec</Typography>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default AltitudeInfo;