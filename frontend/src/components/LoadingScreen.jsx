import React,{useEffect,useRef} from 'react';
import { Grid, Typography } from '@mui/material';
import '../css/loadingScreen.css'

function LoadingScreen() {
  const loadingGifRef = useRef(null);

  useEffect(() => {
    const loadingGif = loadingGifRef.current;
    const loadingImage = new Image();
    loadingImage.src = loadingGif.src;
    loadingImage.onload = function() {
      loadingGif.src = loadingImage.src;
    };
  }, []);
  return (
    <Grid container justifyContent='center' alignItems='center' direction='column' sx={{minHeight:800}} spacing={2}>
      <Grid item>
        <img src="./static/images/loading_screen.gif" className='loading_img' ref={loadingGifRef}/>
      </Grid>
      <Grid item>
        <Typography variant='h3'>Connecting to Drone...</Typography>
      </Grid>
    </Grid>
  );
}

export default LoadingScreen;