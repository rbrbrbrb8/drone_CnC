import React from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Switch from '@mui/material/Switch';
import { useModeContext, useSetMode } from '../../context/ModeContext';
import axios from 'axios';

function ModeCard() {
  const mode = useModeContext();
  const setMode = useSetMode()
  const modeKeys = {
    'Manual':'ALT_HOLD',
    'Guided':'GUIDED'
  }

  const changeMode = (e) => {
    const modeName = e.target.checked ? 'Manual' : 'Guided'
    const modeKey = modeKeys[modeName];
    axios.post('/changeMode',{'mode':modeKey}).then(res => {
      console.log(res.data);
      setMode(modeName)
    })
  }

  return (
    <Card sx={{ minWidth: 275, minHeight: 171 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" className='align-center'>Current Mode</Typography>
        <Typography sx={{ fontSize: 48 }} className='align-center alt-number'>{mode}</Typography>
        <Grid container direction='row' justifyContent='center'>
          <Grid item><Switch color='default' checked={mode === 'Manual'} onChange={changeMode} /></Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default ModeCard;