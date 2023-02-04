import React, { useEffect, useState, Fragment,useRef } from 'react';
import MainScreen from './components/MainScreen';
import LoadingScreen from './components/LoadingScreen';
import { Fade } from '@mui/material';
import axios from 'axios';

function App() {
  const [connected, setConnected] = useState(false);
  const [twoSecMark, setTwoSecMark] = useState(false)
  const appRef = useRef(null);
  useEffect(() => {
    console.log('connecting');
    axios.post('/connect',{}).then(res => {
      console.log(res.data);
      setConnected(true);
    })
    setTimeout(() => {
      setTwoSecMark(true);
    }, 2000)
  }, [])
  useEffect(() => {
    if (appRef.current) {
      appRef.current.scrollTop = 0;
    }
  }, [appRef]);
  return (
    <div>
      {(connected && twoSecMark) ?
        <div>
          <Fade in={connected && twoSecMark} timeout={500}>
            <div ref={appRef}>
              <MainScreen />
            </div>
          </Fade>
        </div>
        : <LoadingScreen />}
    </div>
  );
}

export default App;