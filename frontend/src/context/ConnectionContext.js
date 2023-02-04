import React, { useContext, useState } from 'react';

const ConnectionContext = React.createContext();
const SetConnectionContext = React.createContext();

export function useConnectionContext() {
  return useContext(ConnectionContext);
}

export function useSetConnection() {
  return useContext(SetConnectionContext);
}

export function ConnectionProvider({ children }) {
  const [connection, setConnection] = useState(false);

  return (
    <ConnectionContext.Provider value={connection}>
      <SetConnectionContext.Provider value={setConnection}>
        {children}
      </SetConnectionContext.Provider>
    </ConnectionContext.Provider>
  )
}