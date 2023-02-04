import React from 'react';
import Grid from '@mui/material/Grid'
import Item from './Item';

function Row({items}) {
  return (
    <Grid item container direction='row' alignItems='center' justifyContent='center' spacing={1}>
      {items.map((item,i) => (
        <Grid item>
          <Item key={i} item={item} />
        </Grid>
      ))}
    </Grid>
  );
}

export default Row;