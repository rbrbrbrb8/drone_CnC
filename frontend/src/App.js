import React from 'react';
import Nav from './components/Nav';
import MainSection from './components/MainSection/MainSection';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import theme from './theme/theme';
import { ModeProvider } from './context/ModeContext';
import DroneControl from './components/DroneControl/DroneControl';
import { RateProvider } from './context/RateContext';

function App() {
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

export default App;