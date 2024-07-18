import React from 'react';

// Create a context for sharing data
const Context = React.createContext();

function App() {
    // Set some initial data in the context
    const data = {
        message: 'Hello, world!'
    };

    return (
        // Privide the data to the components inside the Provider
        <Context.Provider value={data}>
            <Component />
        </Context.Provider>
    );
}

function Component() {
    // Use the useContext Hook to access the data in the context
    const context = React.useContext(Context);

    return (
        <p>{context.message}</p>
    )
}
