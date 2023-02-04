import React, { useState } from 'react';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Dialog from '@mui/material/Dialog';
import { Button, DialogActions, DialogContent, DialogTitle, TextField } from '@mui/material';
import axios from 'axios';
import { useSetMode } from '../../context/ModeContext';

function TakeoffDialog({ open, setOpen }) {
  const setMode = useSetMode();
  const [alt, setAlt] = useState(0)

  const handleClose = () => {
    setOpen(false);
  }
  const takeoff = () => {
    console.log(alt);
    axios.post('/takeoff', { "alt": alt }).then(res => {
      setMode('Guided');
      console.log(res.data);
      setOpen(false);
      console.log('yes')
    })
  }

  const handleChange = (e) => {
    console.log(e.target.value);
    setAlt(e.target.value)
  }
  return (
    <Dialog open={open} onClose={handleClose} maxWidth='xs' fullWidth>
      <DialogTitle textAlign='center' color='black'>Enter Altitude</DialogTitle>
      <DialogContent sx={{ justifyContent: 'center' }}>
        <Grid container justifyContent='center' alignItems='center'>
          <Grid item>
            <TextField
              autoFocus
              margin='dense'
              variant='outlined'
              type='number'
              InputProps={{ inputProps: { min: 1 } }}
              value={alt}
              onChange={handleChange}
            />
          </Grid>
        </Grid>
      </DialogContent>
      <DialogActions style={{ justifyContent: 'center' }}>
        <Button variant='contained' onClick={takeoff}>confirm</Button>
      </DialogActions>
    </Dialog>
  );
}

export default TakeoffDialog;