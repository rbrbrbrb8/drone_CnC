import React, { useState } from 'react';
import { Box, Typography, Slider } from '@mui/material';
import { useRateContext, useSetRate } from '../../../context/RateContext';

function RateControl() {
  const rate = useRateContext();
  const setRate = useSetRate();
  const changeRate = (e) => {
    setRate(e.target.value)
  }
  return (
    <Box sx={{ width: 250 }}>
      <Typography id="speed-display" gutterBottom>
        Rate: {rate}
      </Typography>
      <Slider
        value={rate}
        marks
        min={100}
        step={50}
        max={400}
        onChange={changeRate}
        valueLabelDisplay="auto"
        aria-labelledby="speed-slider"
      />
    </Box>
  );
}

export default RateControl;