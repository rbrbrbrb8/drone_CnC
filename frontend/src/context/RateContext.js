import React, { useContext, useState } from 'react';

const RateContext = React.createContext();
const SetRateContext = React.createContext();

export function useRateContext() {
  return useContext(RateContext);
}

export function useSetRate() {
  return useContext(SetRateContext);
}

export function RateProvider({ children }) {
  const [rate, setRate] = useState(100);

  return (
    <RateContext.Provider value={rate}>
      <SetRateContext.Provider value={setRate}>
        {children}
      </SetRateContext.Provider>
    </RateContext.Provider>
  )
}