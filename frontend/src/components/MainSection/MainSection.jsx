import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import '../../css/mainSection.css';
import AltitudeInfo from './AltitudeInfo';
import ModeCard from './ModeCard';
import { CardActionArea } from '@mui/material';

function MainSection() {
  return (
    <Grid container direction='column' justifyContent='center' className='main-section-container' spacing={1}>
      <Grid item container justifyContent='center' direction='row' spacing={1}>
        <Grid item>
          <AltitudeInfo />
        </Grid>
        <Grid item>
          <ModeCard />
        </Grid>
      </Grid>
      <Grid item container justifyContent='center' direction='row' spacing={1}>
        <Grid item>
          <Card sx={{ minWidth: 275, minHeight: 171 }}>
            <CardActionArea  className='takeoff'>
              <Grid sx={{ minHeight: 171 }} container direction='row' alignItems='center' justifyContent='center'>
                <Typography sx={{ fontSize: 48 }} className='align-center takeoff-land-text'>TAKEOFF</Typography>
              </Grid>
            </CardActionArea>
          </Card>
        </Grid>
        <Grid item>
          <Card sx={{ minWidth: 275, minHeight: 171 }} >
            <CardActionArea className='land'>
              <Grid sx={{ minHeight: 171 }} container direction='row' alignItems='center' justifyContent='center'>
                <Typography sx={{ fontSize: 48 }} className='align-center takeoff-land-text'>LAND</Typography>
              </Grid>
            </CardActionArea>
          </Card>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default MainSection;