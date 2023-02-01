import createTheme from '@mui/material/styles/createTheme';

const theme = createTheme({
  palette: {
    primary: {
      main: '#ED523E'
    },
    text: {
      primary: '#ED523E',
      black:'#FFFFFF'
    }
  },
  typography: {
    fontFamily: ['Oswald',
      'sans-serif'
    ].join(',')
  },
  paper: {
    fontFamily: ['Oswald',
      'sans-serif'
    ].join(',')
  }
});

export default theme;