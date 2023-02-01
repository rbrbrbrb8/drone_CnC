import React, {useState} from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import '../../css/mainSection.css';
import AltitudeInfo from './AltitudeInfo';
import ModeCard from './ModeCard';
import { CardActionArea } from '@mui/material';
import axios from 'axios';
import TakeoffDialog from './TakeoffDialog';

function MainSection() {

  const [takeoffOpen,setTakeoffOpen] = useState(false);

  const land = () => {
    axios.post('/land',{}).then(res => {
      console.log(res.data);
    })
  }

  const openTakeoffDialog = () => {
    setTakeoffOpen(true)
  }

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
            <CardActionArea className='takeoff' onClick={openTakeoffDialog}>
              <Grid sx={{ minHeight: 171 }} container direction='row' alignItems='center' justifyContent='center'>
                <Typography sx={{ fontSize: 36 }} className='align-center takeoff-land-text'>TAKEOFF</Typography>
              </Grid>
            </CardActionArea>
          </Card>
        </Grid>
        <Grid item>
          <Card sx={{ minWidth: 275, minHeight: 171 }} >
            <CardActionArea className='land' onClick={land}>
              <Grid sx={{ minHeight: 171 }} container direction='row' alignItems='center' justifyContent='center'>
                <Typography sx={{ fontSize: 36 }} className='align-center takeoff-land-text'>LAND</Typography>
              </Grid>
            </CardActionArea>
          </Card>
        </Grid>
      </Grid>
      <TakeoffDialog open={takeoffOpen} setOpen={setTakeoffOpen}/>
    </Grid>
  );
}

export default MainSection;