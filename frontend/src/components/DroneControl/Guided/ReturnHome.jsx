import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import axios from 'axios';
import { Card, CardActionArea } from '@mui/material';

function ReturnHome() {
  const home = () => {
    axios.post('/changeMode',{'mode':'RTL'}).then(res => {
      console.log(res.data);
    })
  }
  return (
    <Grid container justifyContent='center' className='ReturnHome-container'>
      <Grid item>
        <Card sx={{ minWidth: 275, minHeight: 171 }} >
          <CardActionArea onClick={home}>
            <Grid sx={{ minHeight: 171 }} container direction='row' alignItems='center' justifyContent='center'>
              <Typography sx={{ fontSize: 36 }} className='align-center'>HOME</Typography>
            </Grid>
          </CardActionArea>
        </Card>
      </Grid>
    </Grid>
  );
}

export default ReturnHome;