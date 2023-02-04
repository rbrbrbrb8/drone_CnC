import React from 'react';
import Grid from '@mui/material/Grid';
import { useModeContext } from '../../context/ModeContext';
import Manual from './Manual/Manual';
import Guided from './Guided/Guided';

function DroneControl() {
  const mode = useModeContext();
  return (
    mode === 'Manual' ? <Manual /> : <Guided />
  );
}

export default DroneControl;