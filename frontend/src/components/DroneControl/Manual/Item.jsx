import React from 'react';
import Grid from '@mui/material/Grid'
import { Card,CardActionArea } from '@mui/material';
import axios from 'axios'
import { useRateContext } from '../../../context/RateContext';

function Item({ item }) {
  const rate = useRateContext()
  const move = () => {
    //send api request
    axios.post('/changeDirection',{
      pitch:item.pitch*rate,
      roll:item.roll*rate
    }).then(res => {
      console.log(res.data.res)
    })
    // console.log({pitch:item.pitch*200,roll:item.roll*200})
  }
  const brake = () => {
    //send api request
    axios.post('/changeDirection',{
      pitch:0,
      roll:0
    }).then(res => {
      console.log(res.data.res)
    })
    // console.log({pitch:item.pitch*0,roll:item.roll*0})
  }
  return (
      item.icon ?
        <Card>
          <CardActionArea onMouseDown={move} onMouseUp={brake}>
            <Grid container direction='row' alignItems='center' justifyContent='center'>
              {item.icon}
            </Grid>
          </CardActionArea>
        </Card> :
        {...item.centerIcon}
  );
}

export default Item;