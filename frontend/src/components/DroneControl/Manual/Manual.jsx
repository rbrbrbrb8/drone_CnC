import React, { useState } from 'react';
import Grid from '@mui/material/Grid'
import { WestOutlined, NorthOutlined, SouthOutlined, EastOutlined, NorthWestOutlined, NorthEastOutlined, SouthWestOutlined, SouthEastOutlined, RocketLaunchOutlined } from '@mui/icons-material';
import Row from './Row';

import '../../../css/manual.css';
import RateControl from './RateControl';

function Manual() {

  const directions = {
    top: [{
      pitch: 1,
      roll: -1,
      icon: <NorthWestOutlined sx={{ fontSize: 48 }} />
    }, {
      pitch: 1,
      roll: 0,
      icon: <NorthOutlined sx={{ fontSize: 48 }} />
    }, {
      pitch: 1,
      roll: 1,
      icon: <NorthEastOutlined sx={{ fontSize: 48 }} />
    }],
    middle: [{
      pitch: 0,
      roll: -1,
      icon: <WestOutlined sx={{ fontSize: 48 }} />
    }, {
      centerIcon: <RocketLaunchOutlined color='inherit' sx={{ fontSize: 48 }} />,
      pitch: 0,
      roll: 0
    }, {
      pitch: 0,
      roll: 1,
      icon: <EastOutlined sx={{ fontSize: 48 }} />
    }],
    bottom: [{
      pitch: -1,
      roll: -1,
      icon: <SouthWestOutlined sx={{ fontSize: 48 }} />
    }, {
      pitch: -1,
      roll: 0,
      icon: <SouthOutlined sx={{ fontSize: 48 }} />
    }, {
      pitch: -1,
      roll: 1,
      icon: <SouthEastOutlined sx={{ fontSize: 48 }} />
    },]
  }
  return (
    <Grid container className='manual-container' direction='row' justifyContent='space-around'>
      <Grid item container direction='column' justifyContent='center' alignItems='center' xs={5} spacing={1}>
        {Object.keys(directions).map(key => (
          <Row key={key} items={directions[key]} />
        ))}
      </Grid>
      <Grid item container justifyContent='center' alignItems='center' xs={5}>
          <RateControl />
      </Grid>
    </Grid>
  );
}

export default Manual;