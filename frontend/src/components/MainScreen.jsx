import React,{useEffect,useState} from 'react';
import Nav from './Nav';
import MainSection from './MainSection/MainSection';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import theme from '../theme/theme';
import { ModeProvider } from '../context/ModeContext';
import DroneControl from './DroneControl/DroneControl';
import { RateProvider } from '../context/RateContext';

function MainScreen() {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <Nav />
        <ModeProvider>
          <RateProvider>
            <MainSection />
            <DroneControl />
          </RateProvider>
        </ModeProvider>
      </div>
    </ThemeProvider>
  );
}

export default MainScreen;