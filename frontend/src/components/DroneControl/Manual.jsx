import React, {useEffect, useState} from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import { Button } from '@mui/material';

function Manual() {
  const directions = {
    forward:{
      pitch:1,
      roll:0
    },
    back:{
      pitch:-1,
      roll:0
    },
    left:{
      pitch:0,
      roll:-1
    },
    right:{
      pitch:0,
      roll:1
    }
  }
  return (
    <Grid container justifyContent='center'>
      <Grid item>
        <Button>test</Button>
      </Grid>
    </Grid>
  );
}

export default Manual;