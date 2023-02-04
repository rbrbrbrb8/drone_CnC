import React, { useContext, useState } from 'react';

const ModeContext = React.createContext();
const SetModeContext = React.createContext();

export function useModeContext() {
  return useContext(ModeContext);
}

export function useSetMode() {
  return useContext(SetModeContext);
}

export function ModeProvider({ children }) {
  const [mode, setMode] = useState('Guided');

  return (
    <ModeContext.Provider value={mode}>
      <SetModeContext.Provider value={setMode}>
        {children}
      </SetModeContext.Provider>
    </ModeContext.Provider>
  )
}