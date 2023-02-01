import React from 'react';
import Nav from './components/Nav';
import MainSection from './components/MainSection/MainSection';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import theme from './theme/theme';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <Nav />
        <MainSection />
      </div>
    </ThemeProvider>
  );
}

export default App;